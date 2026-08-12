import os
import glob
import re
import pandas as pd
from typing import List, Dict, Any

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# 한국어 조사 및 어미 제거용 정규식
KOREAN_PARTICLES = re.compile(r'(은|는|이|가|을|를|의|에|에서|과|와|도|만|으로|로|대해|대한|인지|인가요|이야|야|무엇인지|무엇|뭐|알려줘|어떻게|등|\?|\!|\.)+$')

def load_all_datasets() -> pd.DataFrame:
    """data/ 폴더 내의 모든 CSV 파일들을 불러와 하나의 통합 데이터프레임으로 결합합니다."""
    csv_files = glob.glob(os.path.join(DATA_DIR, '*.csv'))
    combined_dfs = []
    
    for file in csv_files:
        try:
            df = pd.read_csv(file, encoding='utf-8-sig').fillna('')
            df['source_file'] = os.path.basename(file)
            
            # 스키마 정규화 (assets.csv 등 항목/파일명/검색키워드 구조 대응)
            if '항목' in df.columns:
                df['질문'] = df.apply(lambda r: f"{r.get('대분류명','')} {r.get('항목','')} ({r.get('파일명','')})", axis=1)
                df['키워드'] = df.get('검색키워드', '')
                df['답변'] = df.apply(lambda r: f"[{r.get('대분류명','')}] {r.get('항목','')} - {r.get('파일명','')} (확장자: {r.get('보유확장자','')})", axis=1)
                
            combined_dfs.append(df)
        except Exception as e:
            print(f"Error loading {file}: {e}")
            
    if not combined_dfs:
        return pd.DataFrame(columns=['ID', '질문', '키워드', '답변', '링크', 'source_file'])
        
    unified_df = pd.concat(combined_dfs, ignore_index=True).fillna('')
    for col in ['질문', '키워드', '답변', '링크']:
        if col in unified_df.columns:
            unified_df[col] = unified_df[col].fillna('').astype(str).str.replace('\\n', '\n', regex=False)
    return unified_df

def clean_token(token: str) -> str:
    """토큰에서 조사 및 어미를 제거하여 어근만 추출합니다."""
    cleaned = KOREAN_PARTICLES.sub('', token).strip()
    return cleaned if len(cleaned) >= 2 else token

def search_csv(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    """
    한국어 조사 처리 및 양방향 가중치 키워드 매칭 알고리즘:
    - 정확한 단어 일치 가산점: +5점
    - '질문' 컬럼 매칭: 3점
    - '키워드' 컬럼 매칭: 2점
    - '답변' 컬럼 매칭: 1점
    - 노이즈 감소를 위해 상위 top_k(기본 3개) 검색 결과 추출
    """
    df = load_all_datasets()
    if not query or pd.isna(query) or not str(query).strip():
        return []
        
    query_clean = str(query).strip().lower()
    raw_tokens = [token.strip() for token in query_clean.split() if len(token.strip()) > 0]
    
    # 원본 토큰 및 어근 토큰 추출
    query_tokens = set()
    for t in raw_tokens:
        query_tokens.add(t)
        stem = clean_token(t)
        if stem:
            query_tokens.add(stem)
            
    results = []
    
    for idx, row in df.iterrows():
        score = 0
        match_details = []
        
        q_text = str(row.get('질문', '')).lower()
        k_text = str(row.get('키워드', '')).lower()
        a_text = str(row.get('답변', '')).lower()
        
        q_words = set(re.findall(r'\w+', q_text))
        k_words = set(re.findall(r'\w+', k_text))
        a_words = set(re.findall(r'\w+', a_text))
        all_row_words = q_words | k_words | a_words
        
        # 0. 정확한 단어 일치 가산점 (+5점)
        for token in query_tokens:
            if not token or len(token) < 2:
                continue
            if token in all_row_words:
                score += 5
                match_details.append(f"정확한 단어 일치 '{token}'(+5)")
        
        # 1. 구문 및 키워드 상호 매칭
        if query_clean in q_text or q_text in query_clean:
            score += 5
            match_details.append("질문 구문일치(+5)")
        if any(kw in query_clean for kw in k_words if len(kw) >= 2):
            score += 4
            match_details.append("키워드 매칭(+4)")
        if query_clean in a_text:
            score += 2
            match_details.append("답변 완전일치(+2)")
            
        # 2. 토큰별 양방향 매칭 (질문: 3점, 키워드: 2점, 답변: 1점)
        for token in query_tokens:
            if not token or len(token) < 2:
                continue
                
            # 질문 매칭 (+3점)
            if token in q_text or any(token in qw for qw in q_words if len(qw) >= 2):
                score += 3
                match_details.append(f"질문키워드 '{token}'(+3)")
                
            # 키워드 필드 매칭 (+2점)
            if token in k_text or any(token in kw or kw in token for kw in k_words if len(kw) >= 2):
                score += 2
                match_details.append(f"키워드필드 '{token}'(+2)")
                
            # 답변 본문 매칭 (+1점)
            if token in a_text:
                score += 1
                match_details.append(f"답변본문 '{token}'(+1)")
                
        if score > 0:
            results.append({
                'id': row.get('ID', idx),
                'question': row.get('질문', ''),
                'keyword': row.get('키워드', ''),
                'answer': row.get('답변', ''),
                'link': row.get('링크', ''),
                'source': row.get('source_file', ''),
                'score': score,
                'match_details': list(set(match_details))
            })
            
    results.sort(key=lambda x: (
        x['score'],
        10 if ('하나투어 브랜드' in str(x['question']) or '하나투어 로고' in str(x['question'])) else 0,
        5 if ('공식인증' in str(x['question']) or 'ci/bi' in str(x['question']).lower()) else 0
    ), reverse=True)
    return results[:top_k]

if __name__ == "__main__":
    test_queries = ["강조색상이 뭐야?", "강조색상이 무엇인지 질문대 대한 답변은 왜 없어?", "간판 규정 알려줘"]
    for q in test_queries:
        res = search_csv(q)
        print(f"=== Query: '{q}' ===")
        for r in res[:2]:
            print(f"  Score {r['score']}: [{r['question']}] Details: {r['match_details']}")
