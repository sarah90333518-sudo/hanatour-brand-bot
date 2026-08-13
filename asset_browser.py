"""
asset_browser.py v2.0 — 브랜드/거점별 + 유형별 듀얼 탭 에셋 브라우저
하나투어 브랜드 똑순이 웹 앱용 Streamlit 컴포넌트
"""
import streamlit as st
import pandas as pd
import os

# ──────────────────────────────────────────────
# 1. 데이터 로드
# ──────────────────────────────────────────────
@st.cache_data
def load_asset_data():
    """data/ 폴더에서 에셋 CSV를 로드한다."""
    csv_path = os.path.join(os.path.dirname(__file__), "data", "assets.csv")
    if not os.path.exists(csv_path):
        csv_path = os.path.join(os.path.dirname(__file__), "data", "하나투어_에셋_최종_v2_키워드보강.csv")
        if not os.path.exists(csv_path) and os.path.exists("data"):
            for f in os.listdir("data"):
                if "에셋" in f and f.endswith(".csv"):
                    csv_path = os.path.join("data", f)
                    break
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    return df


# ──────────────────────────────────────────────
# 2. 브랜드/거점별 분류 로직 (10개 그룹)
# ──────────────────────────────────────────────
BRAND_GROUPS = {
    "본사": {
        "icon": "🏢",
        "description": "하나투어 본사 CI·로고·서체·응용시스템·광고·디지털",
        "subcategories": {
            "기본시스템 (로고·심벌·서체)": lambda df: df[
                (df["대분류코드"] == "01_BS") &
                (~df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "응용시스템 (사무용품)": lambda df: df[
                (df["대분류코드"] == "03_AS") &
                (~df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "광고": lambda df: df[df["대분류코드"] == "04_AD"],
            "사인시스템 (본사)": lambda df: df[df["대분류코드"] == "05_SS"],
            "디지털": lambda df: df[df["대분류코드"] == "06_DS"],
            "브랜드규정 (통합·기타)": lambda df: df[
                df["대분류코드"].isin(["브랜드규정_통합", "브랜드규정_기타"])
            ],
        },
    },
    "공식인증예약센터": {
        "icon": "🏪",
        "description": "공식인증예약센터 전용 BI·사무용품·인쇄홍보물·간판·규정",
        "subcategories": {
            "BI (로고)": lambda df: df[
                (df["대분류코드"] == "01_BS") &
                (df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "사무용품": lambda df: df[
                (df["대분류코드"] == "02_AS") &
                (df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "인쇄·홍보물": lambda df: df[
                (df["대분류코드"] == "03_AS") &
                (df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "사인시스템 (간판)": lambda df: df[
                (df["대분류코드"] == "04_SS") &
                (df["검색키워드"].astype(str).str.contains("공식인증예약센터|예약센터", na=False))
            ],
            "브랜드규정": lambda df: df[
                df["대분류코드"] == "브랜드규정_공식인증예약센터"
            ],
        },
    },
    "DMC": {
        "icon": "🌍",
        "description": "DMC 전용 디자인 파일 (명함·명찰·현수막·X배너·차량 등)",
        "filter": lambda df: df[df["대분류코드"] == "02_DMC"],
    },
    "T데스크": {
        "icon": "🖥️",
        "description": "T데스크 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "04_T데스크"],
    },
    "T라운지": {
        "icon": "✈️",
        "description": "T라운지 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "03_T라운지"],
    },
    "해외지사": {
        "icon": "🗺️",
        "description": "해외지사 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "01_해외지사"],
    },
    "하나팩프리미엄": {
        "icon": "💎",
        "description": "하나팩프리미엄 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "01_하나팩프리미엄"],
    },
    "제우스월드": {
        "icon": "⚡",
        "description": "제우스월드 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "03_제우스월드"],
    },
    "밍글링투어": {
        "icon": "🎭",
        "description": "밍글링투어 전용 디자인 파일",
        "filter": lambda df: df[df["대분류코드"] == "02_밍글링투어"],
    },
    "글로벌네트워크": {
        "icon": "🔗",
        "description": "글로벌네트워크 가이드라인",
        "filter": lambda df: df[df["대분류코드"] == "브랜드규정_글로벌네트워크"],
    },
}


# ──────────────────────────────────────────────
# 3. 유형별 분류 로직 (기존 v1 호환)
# ──────────────────────────────────────────────
TYPE_GROUPS = {
    "기본시스템 (로고·심벌·서체)": {
        "icon": "🎨",
        "filter": lambda df: df[df["대분류코드"] == "01_BS"],
    },
    "응용시스템 (사무용품·기타)": {
        "icon": "📋",
        "filter": lambda df: df[df["대분류코드"] == "02_AS"],
    },
    "응용시스템 (인쇄·홍보물)": {
        "icon": "🖨️",
        "filter": lambda df: df[df["대분류코드"] == "03_AS"],
    },
    "광고": {
        "icon": "📢",
        "filter": lambda df: df[df["대분류코드"] == "04_AD"],
    },
    "사인시스템 (간판)": {
        "icon": "🪧",
        "filter": lambda df: df[df["대분류코드"].isin(["04_SS", "05_SS"])],
    },
    "디지털": {
        "icon": "💻",
        "filter": lambda df: df[df["대분류코드"] == "06_DS"],
    },
    "브랜드규정": {
        "icon": "📖",
        "filter": lambda df: df[df["대분류코드"].astype(str).str.startswith("브랜드규정")],
    },
    "DMC": {
        "icon": "🌍",
        "filter": lambda df: df[df["대분류코드"] == "02_DMC"],
    },
    "T라운지": {
        "icon": "✈️",
        "filter": lambda df: df[df["대분류코드"] == "03_T라운지"],
    },
    "T데스크": {
        "icon": "🖥️",
        "filter": lambda df: df[df["대분류코드"] == "04_T데스크"],
    },
    "해외지사": {
        "icon": "🗺️",
        "filter": lambda df: df[df["대분류코드"] == "01_해외지사"],
    },
    "하나팩프리미엄": {
        "icon": "💎",
        "filter": lambda df: df[df["대분류코드"] == "01_하나팩프리미엄"],
    },
    "제우스월드": {
        "icon": "⚡",
        "filter": lambda df: df[df["대분류코드"] == "03_제우스월드"],
    },
    "밍글링투어": {
        "icon": "🎭",
        "filter": lambda df: df[df["대분류코드"] == "02_밍글링투어"],
    },
}


# ──────────────────────────────────────────────
# 4. 에셋 카드 렌더링
# ──────────────────────────────────────────────
def render_asset_card(row):
    """개별 에셋 항목을 카드 형태로 렌더링"""
    item_name = row["항목"]
    file_name = row["파일명"]
    extensions = row["보유확장자"] if pd.notna(row["보유확장자"]) else "—"
    link = row["링크"] if pd.notna(row["링크"]) else None

    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{item_name}**")
            st.caption(f"📄 {file_name}　|　{extensions}")
        with col2:
            if link and str(link).strip() and str(link) != 'nan':
                st.link_button("다운로드", str(link), use_container_width=True)
            else:
                st.button("링크 없음", disabled=True, use_container_width=True,
                          key=f"no_link_{row.get('id', 0)}_{file_name}_{row.name}")
        st.divider()


def render_asset_table(filtered_df):
    """에셋 목록을 테이블 형태로 표시"""
    if filtered_df.empty:
        st.info("해당 그룹에 디자인 파일이 없습니다.")
        return

    # 항목별 그룹핑 (같은 항목의 여러 파일을 묶어서 표시)
    unique_items = filtered_df["항목"].unique()
    st.caption(f"총 {len(unique_items)}개 항목 · {len(filtered_df)}건 파일")

    for item in unique_items:
        item_df = filtered_df[filtered_df["항목"] == item]
        for _, row in item_df.iterrows():
            render_asset_card(row)


# ──────────────────────────────────────────────
# 5. 검색 기능
# ──────────────────────────────────────────────
def search_assets(df, query):
    """키워드로 에셋 검색 (항목명, 파일명, 검색키워드 대상)"""
    if not query or not query.strip():
        return pd.DataFrame()

    query_lower = query.strip().lower()
    mask = (
        df["항목"].astype(str).str.lower().str.contains(query_lower, na=False) |
        df["파일명"].astype(str).str.lower().str.contains(query_lower, na=False) |
        df["검색키워드"].astype(str).str.lower().str.contains(query_lower, na=False) |
        df["대분류명"].astype(str).str.lower().str.contains(query_lower, na=False)
    )
    return df[mask]


# ──────────────────────────────────────────────
# 6. 메인 뷰 렌더링
# ──────────────────────────────────────────────
def render_brand_view(df):
    """브랜드/거점별 보기"""
    for group_name, config in BRAND_GROUPS.items():
        icon = config["icon"]

        if "subcategories" in config:
            # 서브카테고리가 있는 그룹 (본사, 공식인증예약센터)
            total = sum(len(fn(df)) for fn in config["subcategories"].values())
            with st.expander(f"{icon} {group_name} ({total}건)", expanded=False):
                st.caption(config["description"])
                for sub_name, filter_fn in config["subcategories"].items():
                    sub_df = filter_fn(df)
                    if not sub_df.empty:
                        st.markdown(f"**{sub_name}** ({len(sub_df)}건)")
                        render_asset_table(sub_df)
        else:
            # 단순 필터 그룹
            filtered = config["filter"](df)
            total = len(filtered)
            if total > 0:
                with st.expander(f"{icon} {group_name} ({total}건)", expanded=False):
                    st.caption(config["description"])
                    render_asset_table(filtered)


def render_type_view(df):
    """유형별 보기"""
    for group_name, config in TYPE_GROUPS.items():
        icon = config["icon"]
        filtered = config["filter"](df)
        total = len(filtered)
        if total > 0:
            with st.expander(f"{icon} {group_name} ({total}건)", expanded=False):
                render_asset_table(filtered)


# ──────────────────────────────────────────────
# 7. 메인 엔트리포인트 (Dual Tab Browser)
# ──────────────────────────────────────────────
def render_asset_browser():
    """에셋 브라우저 메인 함수 — 듀얼 탭 모드"""
    st.subheader("📁 하나투어 브랜드 디자인 파일 저장소")

    # 데이터 로드
    try:
        df = load_asset_data()
    except Exception as e:
        st.error(f"디자인 파일 CSV 로드 실패: {e}")
        return

    # 검색창
    search_query = st.text_input(
        "🔍 디자인 파일 검색",
        placeholder="로고, 명함, X배너, 간판 등 키워드 입력...",
        key="asset_search_main"
    )

    if search_query:
        results = search_assets(df, search_query)
        st.markdown(f"**검색 결과: {len(results)}건**")
        if not results.empty:
            render_asset_table(results)
        else:
            st.info("검색 결과가 없습니다. 다른 키워드로 시도해 보세요.")
        return

    # 탭 전환 (브랜드별 / 유형별)
    tab_brand, tab_type = st.tabs(["📂 브랜드별 보기 (10개 그룹)", "📋 유형별 보기 (14개 그룹)"])

    with tab_brand:
        st.caption("브랜드·거점별로 디자인 파일을 분류하여 표시합니다.")
        render_brand_view(df)

    with tab_type:
        st.caption("디자인 파일 유형별로 분류하여 표시합니다.")
        render_type_view(df)


def render_asset_sidebar():
    """사이드바 진입 버튼"""
    st.divider()
    st.markdown("##### 📂 브랜드 디자인 파일 저장소")
    if st.button("📁 디자인 저장소 열기 (듀얼 탭)", key="btn_open_asset_browser", use_container_width=True):
        st.session_state["asset_panel_mode"] = "active"
        st.rerun()


def render_asset_panel() -> bool:
    """메인 패널 호환 함수"""
    if st.session_state.get("asset_panel_mode") == "active":
        col_t, col_c = st.columns([5, 1])
        with col_c:
            if st.button("✕ 챗봇으로 돌아가기", key="btn_close_asset_browser", use_container_width=True):
                st.session_state["asset_panel_mode"] = None
                st.rerun()
                return False
        
        render_asset_browser()
        return True
    return False


# 직접 실행 시 테스트용
if __name__ == "__main__":
    st.set_page_config(page_title="에셋 브라우저 v2.0", layout="wide")
    render_asset_browser()
