import os
import streamlit as st
import pandas as pd
from search_engine import search_csv, load_all_datasets
from gemini_client import generate_brand_response, check_fixed_answer
from asset_browser import render_asset_sidebar, render_asset_panel

# ─────────────────────────────────────
# Streamlit 페이지 기본 설정
# ─────────────────────────────────────

st.set_page_config(
    page_title="하나투어 브랜드 똑순이 AI 챗봇",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────
# 커스텀 CSS (하나투어 브랜드 디자인 시스템: 퍼플 #5E2BB8, 민트 #08D1D9)
# ─────────────────────────────────────

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    /* 상단 헤더 배너 */
    .brand-header {
        background: linear-gradient(135deg, #5E2BB8 0%, #3D197A 50%, #08D1D9 100%);
        border-radius: 16px;
        padding: 28px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px rgba(94, 43, 184, 0.25);
    }
    .brand-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .brand-subtitle {
        font-size: 15px;
        opacity: 0.9;
        font-weight: 400;
    }
    .badge-status {
        background-color: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    /* 버튼 스타일 */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        border-color: #5E2BB8;
        color: #5E2BB8;
    }

    /* 챗 메시지 커스텀 */
    .stChatMessage {
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
    }

    /* 카드 스타일 */
    .sidebar-card {
        background-color: #F8F9FA;
        border-left: 4px solid #5E2BB8;
        padding: 14px;
        border-radius: 8px;
        margin-bottom: 16px;
    }
    
    .weight-badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 700;
        color: white;
        margin-right: 4px;
    }
    .w-q { background-color: #5E2BB8; }
    .w-k { background-color: #08D1D9; color: #111; }
    .w-a { background-color: #6C757D; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────
# 세션 상태 초기화
# ─────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """안녕하세요! 하나투어 브랜드 똑순이입니다. 👋

하나투어의 **브랜드 가이드라인, 로고, 컬러 규정, 폰트, 공식인증예약센터 간판/템플릿, SNS 수칙, 브랜드정의** 등에 대해 질문해 주세요."""
        }
    ]

# ─────────────────────────────────────
# 사이드바 구성
# ─────────────────────────────────────

with st.sidebar:
    st.markdown("### ✈️ 하나투어 브랜드 센터")
    st.caption("하나투어 임직원 전용 브랜드 가이드라인 챗봇")
    
    st.divider()
    
    # 1. 퀵 질문 버튼 (핵심 카테고리별 분류)
    st.markdown("#### ⚡ 자주 묻는 브랜드 질문")
    
    categorized_queries = {
        "🎨 브랜드 기본 자산": [
            ("🏷️ 로고 CI/BI 다운로드", "로고 다운로드"),
            ("🎨 브랜드 컬러 규정", "컬러 가이드 규정 알려줘"),
            ("🔤 지정 폰트 다운로드", "하나투어 폰트 지정서체 다운로드"),
            ("🖼️ 브랜드 이미지 (446컷)", "브랜드 이미지 다운로드"),
        ],
        "🏪 매장 & 대리점 지원": [
            ("🏪 대리점 간판 설치 규정", "대리점 간판 설치 CI 사용 규정"),
            ("📄 대리점 PPT 템플릿", "공식인증예약센터 대리점 템플릿"),
            ("📱 SNS 및 콘텐츠 운영 규정", "SNS 운영 규정 알려줘"),
        ],
        "✈️ 브랜드 체계 & 라인업": [
            ("📐 브랜드 체계 (4계층)", "하나투어 브랜드 체계 아키텍처"),
            ("✈️ 하나프리팩 소개", "하나프리팩 소개 알려줘"),
            ("👑 제우스월드 소개", "제우스월드 브랜드 라인업"),
        ],
        "📞 운영 & 홍보 지원": [
            ("🔔 비즈링(통화연결음) 신청", "비즈링 통화연결음 신청 방법"),
            ("🏆 주요 수상 및 인증 실적", "수상 내역 실적 알려줘"),
        ]
    }

    for cat_name, queries in categorized_queries.items():
        with st.expander(cat_name, expanded=True):
            for label, query_text in queries:
                if st.button(label, key=f"btn_preset_{label}", use_container_width=True):
                    st.session_state.pending_query = query_text
                    st.session_state["asset_panel_mode"] = None

    # 2. 에셋 다운로드 브라우저 사이드바 모듈
    render_asset_sidebar()

    st.divider()

    # 3. 담당자 문의처 카드
    st.markdown("""
    <div class="sidebar-card">
        <strong>📞 브랜드 담당자 문의처</strong><br/>
        <small>
        • <strong>브랜드 검수·디자인</strong>: 이승현G 선임(6725) / 백솜이 선임(7051)<br/>
        • <strong>수상인증·비즈링·브랜드체계</strong>: 천성해 선임(1911)
        </small>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────
# 메인 영역 (에셋 다운로드 센터 또는 챗봇 UI)
# ─────────────────────────────────────

if not render_asset_panel():
    # ─────────────────────────────────────
    # 메인 헤더
    # ─────────────────────────────────────

    st.markdown("""
    <div class="brand-header">
        <div class="brand-title">
            <span>✈️ 하나투어 브랜드 똑순이</span>
            <span class="badge-status">🟢 Live</span>
        </div>
        <div class="brand-subtitle">
            하나투어 브랜드 규정 · 로고 · 컬러 · 간판 · 폰트 · 제우스월드 안내 시스템
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────
    # 챗 히스토리 출력
    # ─────────────────────────────────────

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"].replace('\\n', '\n'))

    # ─────────────────────────────────────
    # 챗 입력 처리 (퀵 버튼 또는 사용자 텍스트)
    # ─────────────────────────────────────

    input_query = st.chat_input("하나투어 브랜드 가이드라인에 대해 물어보세요...")

    if hasattr(st.session_state, 'pending_query') and st.session_state.pending_query:
        input_query = st.session_state.pending_query
        st.session_state.pending_query = None

    if input_query:
        # 1. 사용자 메시지 기록 및 출력
        st.session_state.messages.append({"role": "user", "content": input_query})
        with st.chat_message("user"):
            st.markdown(input_query)

        # 2. CSV 가중치 검색 수행
        search_results = search_csv(input_query, top_k=5)
        
        # 3. Gemini API / FIXED-ANSWER 답변 생성
        with st.chat_message("assistant"):
            with st.spinner("하나투어 브랜드 가이드라인 검색 및 답변 생성 중..."):
                answer = generate_brand_response(input_query, search_results).replace('\\n', '\n')
                st.markdown(answer)
                            
        # 4. 챗 세션 저장
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
