import os
from typing import List, Dict, Any

# ─────────────────────────────────────
# FIXED-ANSWER 사전 정의 (토씨 하나까지 100% 원문 일치)
# ─────────────────────────────────────

FIXED_ANSWERS = {
    "로고": """하나투어 및 브랜드별 로고(CI/BI) 파일에 대해 안내해 드립니다.

하나투어 로고는 H 모양의 심벌, '하나투어' 글자 로고, 심벌과 글자를 함께 사용한 가·세로형 로고, 슬로건 로고 등으로 구성되어 있으며, 일반적으로 심벌과 글자가 함께 있는 **조합형 로고**를 사용합니다. 웹 및 SNS용으로는 **RGB(또는 배경이 투명한 PNG)**, 일반 인쇄용으로는 **CMYK**, 대형 출력물 등 고품질이 필요한 경우에는 **AI(원본) 파일**을 용도에 맞게 선택하여 사용해 주시기 바랍니다. (※ 구버전 로고는 사용하지 않도록 유의해 주세요.)

> 💡 **용어 안내** 쉽게 말해 **CI**는 회사 전체 식별체계를, **BI**는 개별 브랜드·서비스 식별체계를 의미합니다. **워드마크**는 글자형 로고, **심벌마크**는 상징 도형·아이콘이며, **에셋**은 이러한 로고·이미지·폰트 등의 디지털 자산을 뜻합니다.

아래 표에서 필요하신 로고를 확인하고 다운로드하실 수 있습니다.

| 구분 | 파일명·형식 | 추천 용도 | 다운로드 링크 |
|---|---|---|---|
| CI | 하나투어 로고 (인쇄/웹/투명배경/AI원본) | 회사 전체 식별 (인쇄물, 웹사이트, 문서 등) | [다운로드](https://drive.google.com/drive/folders/1OKh9Wc0-cWhVVqOqXahnI0bjyBSUUVLU?usp=drive_link) |
| BI | 제우스월드(ZEUS WORLD) 로고 | 럭셔리 브랜드 상품 홍보 및 관련 제작물 | [다운로드](https://drive.google.com/drive/folders/1fMsurSu9XRqtjf61s08mDf1RDFC2P_tF?usp=sharing) |
| BI | 밍글링투어 로고 | 밍글링투어 상품 홍보 및 관련 제작물 | [다운로드](https://drive.google.com/drive/folders/1r-PxJ9uGICdFtsf2KF1rtpZcE7aZmY5g?usp=sharing) |
| BI | 하나팩 프리미엄 로고 | 하나팩 프리미엄 상품 홍보 및 관련 제작물 | [다운로드](https://drive.google.com/drive/folders/1GOOU6b2emM0nW7MTcEBPwU5-xbJgYq6N?usp=sharing) |
| BI | 티라운지 로고 | 티라운지 시설 및 서비스 식별용 | [다운로드](https://drive.google.com/drive/folders/1Smkpl_S1L1hCpvedU9iS8Rjt32oeul74?usp=sharing) |
| BI | 티데스크 로고 | 티데스크 시설 및 서비스 식별용 | [다운로드](https://drive.google.com/drive/folders/1Prp1znFrVg90bu0aWL3rUElQf23qkLyM?usp=sharing) |
| BI | 공식인증예약센터 BI | 공식인증예약센터 승인 매장 및 간판/제작물 | [다운로드](https://drive.google.com/drive/folders/1zRkMhpqlwnyiSYOdZkzWxwwCDp7BuyAd?usp=sharing) |

▶ 디자인·로고·브랜드 가이드라인·브랜드 자산(에셋)·검수 관련 문의 이승현G 선임(6725), 백솜이 선임(7051)""",

    "컬러": """하나투어 브랜드 컬러를 안내해 드립니다.

▶ [컬러 한눈에 보기](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQCW09j1uWNaRYjTsAvIMShgAag2mDUE_WHjPN3aw72BXdA?e=fxGT7P)

**[색상 사용 원칙]**

**1. 기본 규칙**
하나투어의 모든 브랜드 접점(광고, 인쇄물, 디지털 등)에 이 가이드라인을 동일하게 적용합니다.
브랜드 메시지를 전달하는 제작물은 이 색상 규정을 우선 따라야 합니다.
단, 아래의 경우는 가이드라인 외 색상도 사용할 수 있습니다.
- 배경 사진, 일러스트, 삽화 위의 그래픽·텍스트 및 시즌 이미지
- 메뉴·썸네일·라벨 등 UI 요소에서 콘텐츠 구분이나 가독성이 필요한 경우

**2. 대표·확장 색상 (= 메인 컬러)**

- 대표·확장 색상은 브랜드를 대표하는 주(主) 색상이므로, 모든 시각물에 기본적으로 적용합니다.
- 강조 색상과 함께 쓸 때 → 대표·확장 색상이 면적의 **40% 이상**을 차지해야 합니다.
- 로고에는 대표 색상과 흑백만 적용 가능합니다. (확장 색상은 로고에 사용 불가)
- 확장 색상은 단독으로도 활용 가능하며, 콘텐츠 성격에 따라 주 색상으로 쓸 수 있습니다.

**3. 파생·보조 색상 (= 보완 컬러)**

- 파생·보조 색상은 반드시 대표·확장 색상과 함께 활용해야 합니다. (단독 사용 불가, 흑백 규정은 예외)
- 디자인 구성에 따라 활용 비율을 유연하게 조정할 수 있습니다.

**4. 강조 색상 (= 포인트 컬러)**

- 강조 색상은 대표·확장 색상을 보조하는 역할이며, 강조 색상만 단독으로 쓰는 것은 불가합니다.
- 대표·확장 색상과 함께 쓸 때 → 강조 색상은 면적의 **15% 미만**이어야 합니다.
- 배경에는 사용 불가합니다. 텍스트, 아이콘, 라벨, 포인트 그래픽 등 '포인트 요소'에만 사용합니다.
- 타 여행사의 상징 색상으로 오인되지 않도록, 활용 비율과 적용 범위를 엄격히 관리합니다.

**[컬러 스펙]**

| 컬러 | HEX | CMYK(별색기준 G) | CMYK(일반 C) | RGB | PANTONE |
|---|---|---|---|---|---|
| 퍼플 (Purple) | #5E2BB8 | 86/97/0/0 | 86/99/0/0 | 94/43/184 | 2091 C |
| 민트 (Mint) | #08D1D9 | 70/0/15/0 | 70/0/11/0 | 8/209/217 | 3115 C |
| 블랙 (Black) | #000000 | 0/0/0/100 | 0/0/0/100 | 0/0/0 | Black C |
| 화이트 (White) | #FFFFFF | 0/0/0/0 | 0/0/0/0 | 255/255/255 | - |

▶ 다운로드
• [외부용 컬러가이드라인 다운로드](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQA8JmSJmH2vRq_2vX8UBKTFAej-sOvPNuUojzr72uFV8FY?e=YiJv5q)
• [내부용 컬러가이드라인 다운로드](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQAP1u1hzQ9LQrFL37y2QQEfAdjMmEm8YLAxnTAAJ47NSSg?e=fArioJ)
• [컬러 활용안 예시](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQCF7gd8rLcPS7ovJGtm2YKmAQuzZHbqFUJvOtF6iub_qKo?e=kNW1Xa)

▶ 디자인·로고·브랜드 가이드라인·브랜드 자산(에셋)·검수 관련 문의 이승현G 선임(6725), 백솜이 선임(7051)""",

    "간판": """하나투어 공식인증예약센터 및 매장 유형별 간판 제작 및 CI 사용 규정을 안내해 드립니다.

하나투어는 브랜드 일관성과 왜곡 방지를 위해 매장 유형(공식인증예약센터, 일반 대리점, 해외 DMC 등)에 따라 간판 설치 및 CI 사용 권한을 엄격하게 구분하여 적용하고 있습니다.

**매장 유형별 간판 및 CI 사용 규정**

| 매장 유형 | 간판 설치 및 CI 사용 규정 | 상태 |
|---|---|---|
| 공식인증예약센터 | • 하나투어 CI 간판 설치 및 사용 가능 (입체판류형, 바타입, 세로형 플렉스 3종 사용 가능) • 매장 내 간판, POP, 브로슈어 등에 공식 CI/BI 적용 가능 | 🟢 사용 가능 |
| 일반 대리점 | • 하나투어 CI 및 BI 사용 불가 (자체 상호만 사용하여 간판 제작 및 운영) • 하나투어 브랜드를 임의로 사용하거나 명칭을 넣은 홍보물 제작 불가 | 🔴 사용 불가 |
| 해외 DMC | • 하나투어 CI 간판 설치 및 사용 불가 (명함, 홍보자료, 온라인 채널 포함) • 본사가 운영하는 사무실처럼 오인될 수 있는 CI 간판 설치 불가 | 🔴 사용 불가 |
| 외부 거래처 / 제3자 | • 공식 파트너로 오인될 수 있는 로고 및 CI 사용 불가 • 사전 협의 및 공식 제휴 없이 단순 판매 목적의 로고 노출 불가 | 🔴 사용 불가 |

▶ 바로가기
[공식인증예약센터 간판 예시 이미지 보러가기](https://hanatour0.sharepoint.com/:i:/s/msteams_7d230d/IQCE5NfwfphRR5_0TaaWewOuAVir4jJoxs-pRbQvqrwM3Ts?e=rWOUKU)

▶ 다운로드
[공식인증예약센터 가이드라인](https://drive.google.com/drive/folders/1kne86RM4MgaVIaugm7sEBz2VzMjoTGKl?usp=sharing)

─── 사인시스템 디자인 파일 ───

공식인증예약센터 등 CI 사용 승인 매장에 한해 적용되는 간판 및 사인시스템 제작용 가이드라인 및 디자인 파일 다운로드 링크를 안내해 드립니다.
용도에 맞춰 필요한 디자인 파일을 확인해 보시기 바랍니다.

**1. 사인 요소**

| 항목 | 다운로드 |
|---|---|
| SS2 현판사인 | [다운로드](https://drive.google.com/drive/folders/1HCYZyPvz4fchMjm1iNACvjebCsWTATzH?usp=sharing) |
| SS3 윈도우그래픽 | [다운로드](https://drive.google.com/drive/folders/1NxNU9f1mCEvl-iNLpDhpWEiFBPmhzIo3?usp=sharing) |
| SS4 윈도우그래픽상단 | [다운로드](https://drive.google.com/drive/folders/1YZIQnZ_cCsBPOhuQJPhoHWpLuzrxOlcp?usp=sharing) |
| SS5 이미지월 | [다운로드](https://drive.google.com/drive/folders/1xT8OpAgsEQygJJTAZcO_QhpEHxPyM0vH?usp=sharing) |
| SS6 층별안내 | [다운로드](https://drive.google.com/drive/folders/1uaiwvlKzzjQlvziHLaFztFgliRzr68Fl?usp=sharing) |

**2. 간판류**

| 항목 | 다운로드 |
|---|---|
| SS7 조합형로고 | [다운로드](https://drive.google.com/drive/folders/19XFqPVdm6fDGHIS-0s4OMfwk4h6WV0hr?usp=sharing) |
| SS8 조명돌출형 | [다운로드](https://drive.google.com/drive/folders/1ttLobWsunB0a2pP4B91Tg7y1VeiQGqNR?usp=sharing) |
| SS9 가로입체판류형 | [다운로드](https://drive.google.com/drive/folders/1ee4cCPtZNzK5GDcCAly4GuE6L_TCJ0va?usp=sharing) |
| SS10 가로대형판류형 | [다운로드](https://drive.google.com/drive/folders/123NMjsve-zaRKyLrT4sxAuVEsgCbhPts?usp=sharing) |
| SS11 가로곡선판류형 | [다운로드](https://drive.google.com/drive/folders/1BARXMOWHj5LvG_5ZTKw-TyCh8Gj5NzIk?usp=sharing) |
| SS12 가로입체BAR형 | [다운로드](https://drive.google.com/drive/folders/1KemxfSBxtFGvH_NlhKxXmtOP4Spm-THq?usp=sharing) |
| SS13 세로플렉스형 | [다운로드](https://drive.google.com/drive/folders/198qYTWRj2sZnjyy5HLVPkF5-jyPEss_s?usp=sharing) |

※ 사인시스템 디자인 파일은 공식인증예약센터 등 CI 사용 승인 매장에 한해 적용됩니다.

▶ 브랜드 검수·디자인 문의: 이승현G 선임(6725) / 백솜이 선임(7051)""",

    "대리점 템플릿": """공식인증예약센터의 브랜드 가치를 높이고 홍보물 제작 효율성을 향상시키기 위해 브랜드 가이드 기반의 공식 템플릿을 개발하였습니다.

실무 활용도를 높이기 위해 디자인 원본 파일이 아닌 PPT 형태로 제공드리며,
배포된 템플릿은 현업에서 문구, 가격, 일정 등 필요한 내용을 직접 수정하여 즉시 활용하실 수 있습니다.

템플릿은 브랜드 가이드라인에 맞춰 제작되어 있어 활용 시 수정 사항을 최소화할 수 있으며, 검수 과정도 보다 신속하게 진행될 수 있습니다.
검수 신청 시에는 디자인이 깨지지 않고 정확하게 확인될 수 있도록 PDF 파일로 전달해 주시면 더욱 원활한 검수가 가능합니다.
다만 PDF 변환이 어려운 경우에는 PPT 파일로 검수 요청해 주셔도 됩니다.

템플릿을 활용해 제작한 홍보물도 기존과 동일하게 브랜드 사용 검수 절차가 필요합니다.

▶ 검수 신청 경로 : 하나샘 > 지식창고 > 게시창고 > 요청신청 > 브랜드 사용 검수

▶ 바로가기
[공식인증예약센터 템플릿 공지](https://sam.hanatour.co.kr/cst/hana/bbs/usr.read.jsp?id=2243715)

▶ 다운로드
[공식인증예약센터 템플릿 다운로드](https://drive.google.com/drive/folders/1tZMcO90Ao0zpjXFUJMkYpDZdSNb-Z3BK?usp=sharing)

▶ 브랜드 검수·디자인 문의: 이승현G 선임(6725) / 백솜이 선임(7051)""",

    "제우스월드 매니페스토": """제우스월드 브랜드 매니페스토를 안내해 드립니다.

**경험의 기준을 높이다 ZEUSworld**

ZEUSworld는
세계 곳곳의 특별한 경험을
당신의 취향과 안목에 맞춰
가장 완성도 높은 형태로 큐레이션합니다.

꿈속 같은 하룻밤,
오감을 깨우는 미식의 향연,
찬란한 예술과 문화의 숨결,
그리고 위대한 자연 속에서의 깊은 탐험까지

우리는 더 많은 곳으로 데려가기보다
가장 높은 기준 위에서
당신이 꿈꾸던 여행을 완성합니다.

ZEUSworld는
여행이 단순한 기억을 넘어
당신의 기준이 되는 경험으로 남도록
처음부터 끝까지 함께하겠습니다.

▶ **다운로드**
• [제우스월드 브랜드 가이드 & 소개 자료 (PPT) 다운로드](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQChHsmdIcH5S4J3k2Tb0C66AaIQ1oG7o3co5p5xCU8Mklk?e=chISpH)

📞 **문의 안내**
• 브랜드 체계·소개·정의: 천성해 선임 (내선 1911)""",

    "제우스월드": """하나투어의 최고급 하이엔드 여행 브랜드, **제우스월드(ZEUSworld)**에 대해 안내해 드립니다.

제우스월드는 글로벌 럭셔리 호텔 및 리조트 네트워크와의 강력한 파트너십을 바탕으로, 단순한 여행을 넘어 고객의 취향과 안목에 맞춘 격이 다른 럭셔리 경험을 선사합니다.

✨ **브랜드 개요 및 슬로건**

> *"경험의 기준을 높이다, ZEUSworld"*

• 쉽게 말해: 여행이 단순한 추억이나 기억으로 끝나는 것이 아니라, 고객 삶의 새로운 기준이 되는 특별한 경험이 되도록 처음부터 끝까지 정교하게 큐레이션하고 케어합니다.
• 브랜드 체계: 하나투어 브랜드 구조상 **'개별 브랜드'**에 속합니다.
• 브랜드 매니페스토 전문이 궁금하시면 **'제우스월드 매니페스토'**로 질문해 주세요.

🗺️ **제우스월드 핵심 라인업 3종**

제우스월드는 고객의 여행 방식과 맞춤화 수준에 따라 다음과 같은 3가지 프리미엄 라인업을 제공합니다.

**1. 제우스 프라이빗 (ZEUS Private) — 맞춤형 럭셔리**
• 오직 한 팀만을 위해 처음부터 끝까지 완전 맞춤으로 설계하는 하이엔드 여행입니다.
• 비즈니스 클래스 항공과 5성급 이상의 최상급 숙소를 기본으로 하며, 일정, 동선, 전담 가이드까지 고객의 요구에 100% 맞춰 설계합니다.

**2. 제우스 시그니처 (ZEUS Signature) — 최상위 패키지**
• 제우스월드가 엄선한 독보적인 일정과 전담 가이드 케어로 완성도를 극대화한 **럭셔리 기획 패키지**입니다.
• 소규모 패키지, 최고급 골프/크루즈/요트 투어, 고품격 액티비티 및 분야별 전문가가 동반하는 테마 여행 등으로 구성됩니다.

**3. 제우스 셀렉트 (ZEUS Select) — 프리미엄 자유여행**
• 비즈니스 클래스 항공과 상위급 럭셔리 호텔을 결합한 자유여행 상품입니다.
• 컨시어지 케어 혜택을 제공하며, 현지 투어, 호텔, 전용 차량 등 원하는 구성만 골라 나만의 럭셔리 여정을 편리하게 설계할 수 있습니다.

▶ **바로가기**
• [제우스 공식 홈페이지](https://zeus.hanatour.com/package/zeus)
• [브랜드 체계 하이어라키 이미지 보기](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQBvyUb-1ucsQKdACA6V57s_AQqdq-SqRwg2fLxMXfLME2Q?e=9m6NAe)

▶ **다운로드**
• [제우스월드 브랜드 가이드 & 소개 자료 (PPT) 다운로드](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQChHsmdIcH5S4J3k2Tb0C66AaIQ1oG7o3co5p5xCU8Mklk?e=chISpH)
• [제우스월드 공식 로고 파일 다운로드 (AI, PNG / CMYK & RGB)](https://drive.google.com/drive/folders/1fMsurSu9XRqtjf61s08mDf1RDFC2P_tF?usp=sharing)

📞 **문의 안내**
• 수상인증·비즈링·브랜드체계 관련 문의: 천성해 선임 (내선 1911)
• 제우스월드 브랜드 로고 사용 및 디자인 검수 문의: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)""",

    "sns": """하나투어 브랜드 안전을 위한 SNS 및 콘텐츠 운영 규정을 안내해 드립니다.

회사와 관련된 모든 대외 콘텐츠(SNS 게시물, 광고, 이벤트 문구, 이미지, 영상, 숏폼, 댓글 등)는 게시 전 반드시 사전에 규정을 점검해야 합니다.

**1. 적용 대상**
- 하나투어 공식 채널 및 고객에게 노출되는 모든 브랜드 콘텐츠(배너, 카드뉴스, 숏폼, 해시태그 등)
- 공식 계약 영업 채널, 공식인증예약센터, DMC(쉽게 말해 현지 여행 협력사입니다) 명의의 SNS 등 영업 목적의 계정
- 프로필, 유니폼, 사무실 이미지 등으로 하나투어와의 협력관계가 드러나는 계정
- 직책, 소속, 업무 등 하나투어와의 관계가 명시된 개인 계정

**2. 콘텐츠 제작·게시 4대 원칙**

| 구분 | 주요 규정 및 금지 사항 | 상태 |
|---|---|---|
| 쟁점 배제 | 사회적 쟁점 및 갈등 유발 요소를 전면 배제합니다. 젠더, 세대, 지역, 종교, 정치 관련 민감한 주제 금지. 참사, 역사적 아픔, 범죄, 인권 이슈를 희화화하거나 가볍게 다루는 행위 금지. | 🔴금지 |
| 차별 금지 | 특정 집단을 차별하거나 비하하는 표현을 절대 금지합니다. 인종, 국적, 장애, 외모, 특정 직업군 등에 대한 조롱 및 고정관념 생산 금지. 온라인 혐오 표현 및 혐오 기반 유행어 배제. | 🔴금지 |
| 밈 금지 | 출처와 원본 맥락이 불분명한 유행어, 밈, 챌린지 사용을 제한합니다. 유행어의 최초 유래나 이면에 숨겨진 비하·부정적 의미가 없는지 철저히 확인. 맥락이 미확인되었거나 의미가 불명확한 표현 사용 금지. | 🔴금지 |
| 법적 리스크 | 법적 리스크를 원천적으로 차단합니다. 이미지, 폰트, 음원 등의 저작권 및 초상권 확보 확인. 타 브랜드 상표권 무단 침해 방지. 개인정보 유출 방지 및 표시광고법 사전 검토. | 🔴금지 |

**3. 게시 전 필수 자가 체크리스트**

콘텐츠를 게시하기 전, 아래 항목 중 **단 하나라도 우려가 되거나 우려 판정을 받은 경우 게시를 즉시 보류**하고 상위 직책자 또는 유관부서에 문의해야 합니다.

| 구분 | 점검 항목 | 상태 |
|---|---|---|
| 공통 | 초상권·선정성/폭력성·사적표현·비방/허위·저작권(폰트 포함)·개인정보·브랜드 이미지 영향 여부 | ✅필수 확인 |
| 사회적 리스크 | 갈등요소·차별/비하·참사/역사/인권 부적절 활용·출처불명 밈/챌린지·맥락 미확인 소재 여부 | ✅필수 확인 |

※ 위 항목 중 하나라도 우려될 시 게시를 보류하고 상위직책자·유관부서에 문의하시기 바랍니다.

**4. 규정 위반 및 민원 발생 시 조치 사항**

원칙과 가이드라인을 준수하지 않아 대내외적 민원 또는 리스크가 발생할 경우, 다음과 같은 조치가 즉각 시행될 수 있습니다.
- 문제 콘텐츠 즉시 삭제 또는 수정
- 시정 요구 및 정식 재발방지대책 제출 요구
- 해당 계정의 운영 제한 또는 폐쇄 조치
- 제휴·영업 계약 조정 및 패널티 부여

▶ 바로가기
[브랜드 안전을 위한 SNS 및 콘텐츠 운영 유의사항 공지](https://sam.hanatour.co.kr/cst/hana/bbs/usr.read.jsp?id=2238797)

▶ 다운로드
[SNS 운영 가이드라인](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQAuHvWKNJOAQ47PAFpOewG2Abcy1ocjQxiGziWt86WFiEk?e=dlyVda)

▶ 브랜드 검수·디자인 문의: 이승현G 선임(6725) / 백솜이 선임(7051)""",

    "폰트": """하나투어에서 사용하는 공식 폰트를 안내해 드립니다.

| 구분 | 서체명 | 용도 | 안내 |
|---|---|---|---|
| 공식 서체 | 여행그자체 | 브랜드 대표 서체 (제한 배포) | 브랜드마케팅팀 이승현G 선임(내선 6725)에게 문의 |
| 지정 서체 (국문) | 본고딕 (Noto Sans KR) | 국문 일반 제작물 | 아래 링크에서 다운로드 |
| 지정 서체 (영문/숫자) | Inter | 영문·숫자 일반 제작물 | 아래 링크에서 다운로드 |

> 💡 **안내**: '여행그자체'는 하나투어 전용 서체로 별도 요청을 통해서만 배포됩니다. 일반 제작물에는 본고딕(국문)과 Inter(영문)를 사용해 주세요.

▶ 다운로드
• [지정서체 다운로드 (본고딕 / Inter)](https://drive.google.com/drive/folders/1ijPYwDnEv3xB9feJThyVdngzjZoBeAwX?usp=drive_link)

▶ 디자인·로고·브랜드 가이드라인·브랜드 자산(에셋)·검수 관련 문의: 이승현G 선임(6725) / 백솜이 선임(7051)""",

    "수상이력": """하나투어의 주요 수상 및 인증 실적을 안내해 드립니다.

**[2026년 · 4건]**

| 시상명(주관처) | 분야/부문 | 수상 내역 |
|---|---|---|
| 제28차 한국산업의 브랜드파워(K-BPI) (한국능률협회컨설팅) | 🟣 브랜드 / 여행사 | 22년 연속(2005~2026) 여행사 부문 1위 |
| 제28회 2026 대한민국 브랜드스타 (브랜드스탁) | 🟣 브랜드 / 여행사 | 22년 연속(05년~26년) 여행사 부문 1위 |
| 제17회 뉴욕페스티벌 대한민국 국가 브랜드 대상 (뉴욕페스티벌) | 🟣 브랜드 / 여행사 | 2015, 2026 여행사 부문 대상 수상(업계 최초) |
| 2026 제9회 국가서비스대상 (산업정책연구원) | 🟢 서비스 / 하이엔드 여행 | 2023(하나팩 2.0) |

**[2025년 · 7건]**

| 시상명(주관처) | 분야/부문 | 수상 내역 |
|---|---|---|
| 2025 대한민국 브랜드스타 (브랜드스탁) | 🟣 브랜드 / 여행사 | 21년 연속(05년~25년) 여행사 부문 1위 |
| 제27차 한국산업의 브랜드파워(K-BPI) (한국능률협회컨설팅) | 🟣 브랜드 / 여행사 | 21년 연속(2005~2025) 여행사 부문 1위 |
| 2025 한국산업의 고객만족도(KCSI) (한국능률협회컨설팅) | 🟢 서비스 / 여행사(해외여행) | 14년 연속 1위(2009~2025) 여행사 부문 1위 |
| 2025 한국서비스품질지수(KS-SQI) (한국표준협회) | 🟢 서비스 / 여행사 | 4년 연속 여행사 부문 1위 |
| 제15회 대한민국 SNS 대상 (한국소셜콘텐츠진흥협회) | 🔵 SNS / 관광 | 관광부문 대상 수상(업계 최초) |
| 제33회 소비자가 뽑은 좋은 광고상 (한국광고주협회) | 🟠 광고 / 디지털 | 하나와 태리(제일기획) |
| 2025 중앙광고대상 (중앙일보) | 🟠 광고 / OOH(옥외광고) | OOH 비주얼 부문 수상 |

**[2024년 · 2건]**

| 시상명(주관처) | 분야/부문 | 수상 내역 |
|---|---|---|
| 한국산업 브랜드파워 (한국능률협회컨설팅) | 🟣 브랜드 / 여행사 부문 | 20년 연속(05년~24년), 여행사 부문 1위 |
| 한국에서 가장 존경받는 기업 (한국능률협회컨설팅) | 🟢 기업평판 / 여행사 서비스업 | 13년 연속(10년~22년), 여행사 부문 1위 |

▶ 수상인증·비즈링·브랜드체계 관련 문의: 천성해 선임 (내선 1911)""",

    "담당자": """브랜드 관련 문의 담당자를 안내해 드립니다.

| 담당 영역 | 담당자 | 내선번호 |
|---|---|---|
| 디자인·로고·가이드라인·브랜드 자산(에셋)·폰트·컬러·검수 | 이승현G 선임 | 6725 |
| 디자인·로고·가이드라인·브랜드 자산(에셋)·폰트·컬러·검수 | 백솜이 선임 | 7051 |
| 브랜드 소개·정의·체계·수상인증·비즈링 | 천성해 선임 | 1911 |

**문의 유형별 안내:**
- **디자인/실물 제작물 관련** (로고 사용, 시안 검수, 폰트, 컬러 규정, 에셋 다운로드, 간판, 가이드라인 등)
  → 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)

- **브랜드 개념/체계 관련** (브랜드 소개, 정의, 브랜드 아키텍처, 수상이력, 비즈링 등)
  → 천성해 선임 (내선 1911)""",

    "비즈링": """비즈링(통화연결음) 신청 방법을 안내해 드립니다.
(쉽게 말해, 전화를 걸 때 상대방에게 들리는 대기음을
하나투어 브랜드 음원으로 설정하는 서비스입니다.)

▶ 바로가기
- [비즈링(16초) 신청 방법 공지](https://sam.hanatour.co.kr/cst/hana/bbs/usr.read.jsp?id=2244057)

▶ 수상인증·비즈링·브랜드체계 관련 문의: 천성해 선임 (내선 1911)""",

    "브랜드 체계": """하나투어 브랜드 체계(4계층 아키텍처)를 안내해 드립니다.

| 계층 | 구분 | 해당 브랜드 |
|---|---|---|
| 1계층 | 기업 브랜드 | 하나투어 |
| 2계층 | 개별 브랜드 | 하나팩, 내나라여행, 제우스월드, 하나프리 |
| 3계층 | 크로스 브랜드 | 우리끼리 (적용: 하나팩~제우스월드, 하나프리 제외) |
| 4계층 | 브랜드 수식어 | 하나팩2.0/세이브/테마, 제우스 3종, 하나프리팩 |

💡 용어 안내
· 크로스 브랜드: 하나의 콘셉트를 여러 제품군에 걸쳐 확장한 브랜드

하나투어 브랜드 체계
①기업 브랜드 l 회사나 회사의 상호를 대신하는 브랜드
②개별 브랜드 l 특정 개별 제품이나 제품군에 붙여진 브랜드
③크로스 브랜드 l 특정 콘셉트를 서로 다른 제품군으로 확장시킨 브랜드
④브랜드 수식어 l 동일 브랜드가 부착된 제품 범주 내에서 제품들 간의 품질, 속성, 기능에서의 차이를 나타내기 위해 사용된 수식어

▶ 개별 브랜드 정의
· 하나팩: 단체 기획 여행 브랜드 (완전 패키지)
· 내나라여행: 국내 프리미엄 브랜드
· 제우스월드: 국내외 하이엔드 여행
- 제우스프라이빗(맞춤) / 제우스시그니처(패키지) / 제우스셀렉트(자유)
· 하나프리: 개별 자유 여행 브랜드 (완전 자유여행)
· 우리끼리: 크로스 브랜드, 프라이빗 여행 브랜드. 특정 콘셉트를 여러 제품군으로 확장한 브랜드. 적용 범위는 하나팩~제우스월드까지이며, 하나프리는 포함되지 않음.
· 하나팩테마: 테마 그 자체가 목적이 되는 여행

▶ 여행 유형 3구분
1. 완전 패키지 2. 패키지+자유 3. 완전 자유여행

▶ 브랜드 체계 원본 도표 보기
[하이어라키 이미지 보기](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQBvyUb-1ucsQKdACA6V57s_AQqdq-SqRwg2fLxMXfLME2Q?e=9m6NAe)

▶ 브랜드 체계·수상이력·비즈링 문의: 천성해 선임 (내선 1911)""",

    "내맘대로": """「내맘대로」 등록상표 사용 규정을 안내해 드립니다.

「내맘대로」는 하나투어가 보유한 39류(여행알선·운송) 등록 이미지 상표입니다.
일상 표현처럼 보이지만 정식 등록·관리 상표이므로, 내부에서 '자유롭게/마음대로' 의미로 반복 사용하면 외부에서도 일반 표현으로 인식돼 상표력이 약해질 수 있습니다. 단품 조합 상품에 한해 일관되게 사용해 주세요.

■ 적용 대상
고객이 항공·호텔 등 [단품+단품]을 직접 골라 자유롭게 조합하는 상품입니다.
사용 범위: 단품의 '자유 조합'으로, 현재는 '내맘대로 항공+호텔'에 한해 사용 가능합니다.

■ 핵심 판단 기준 (사용 전 필수 체크)
'내맘대로'를 빼도 말이 되면 사용하지 않습니다. 고객이 단품을 직접 골라 묶는 조합형 상품의 이름으로만 사용합니다.

■ 상황별 대체 표현 (Do & Don't)
① 일정이 자유로운 경우　(X) 내맘대로 1일 / 내맘대로 자유일정 → (O) 자유일정 / 전일 자유일정 / 여유로운 일정
② 선택관광을 안내할 때　(X) 내맘대로 선택관광 → (O) 선택관광 / 취향대로 선택
③ 옵션을 고르는 경우　　(X) 내맘대로 DIY 여행 → (O) DIY 여행 / 취향대로 선택하는 여행

▶ [내맘대로 상표 사용 가이드 원문 보기](https://sam.hanatour.co.kr/cst/hana/bbs/usr.read.jsp?id=2241476)

▶ 브랜드 체계·상표 관련 문의: 천성해 선임 (내선 1911)""",

    "하나프리팩": """하나프리팩을 안내해 드립니다.

하나프리팩은 '준비는 편하게, 여행은 자유롭게'를 실현하는 하이브리드 여행 상품입니다. 자유여행의 자율성과 패키지의 편리함을 결합해, 세미패키지(일부만 자유)부터 에어텔(항공+숙박만 묶음)까지 선택하고 원하는 현지투어만 골라 나만의 여행을 완성할 수 있습니다.

(참고: '하나프리'와 '하나프리팩'은 서로 다른 상품입니다. 상세 소개는 아래 PPT를 참고해 주세요.)

▶ 다운로드
• [하나프리팩 브랜드 소개 자료 (PPT)](https://hanatour0.sharepoint.com/:p:/s/msteams_7d230d/IQDfYG1tQ-bBTKHhAhty24uYATMm6ElyX4GrDzUXaXRjcy4?e=sfUoaQ)

▶ 브랜드 체계·소개·정의 문의: 천성해 선임 (내선 1911)
▶ 디자인·로고·검수 문의: 이승현G 선임 (6725) / 백솜이 선임 (7051)""",

    "브랜드이미지": """하나투어 브랜드 이미지 자료를 안내해 드립니다.

■ 파일 수량: 총 446컷
· 인물 이미지: 274컷
· 소품 이미지: 172컷

■ 다운로드 링크
· [이미지 프리뷰 모음](https://hanatour0.sharepoint.com/:p:/s/msteams_7d230d/IQBRerud4Tw7Tad8d3nlXe8IASk2C9Uwxn3nZY4A-S7Dtpw?e=IzazzU)
· [파일 리스트](https://hanatour0.sharepoint.com/:x:/s/msteams_7d230d/IQA_EWt6NNJ6Sp_A18_r4VnKAcOOZFlrx4QzNiYiCo2YyWM?e=skFoAS)
· [인물 이미지 폴더 (25년 촬영분, ~27년 7월 18일까지ㅣ1년 단위 연장)](https://hanatour0.sharepoint.com/:f:/s/msteams_7d230d/IgAd0h6A_M1qT5ph2rge9Ga7AVUn8wphVS3DDvIAH4dXyiI?e=jQwk4F)
· [소품 이미지 폴더 (25년 촬영분, 영구 사용ㅣ고화질 필요 시 문의)](https://hanatour0.sharepoint.com/:f:/s/msteams_7d230d/IgCdy2NrXOL-T6zHuIIVUzkaAf5UhNX75pNPHWsPjJCEZyk?e=nlGGyg)
· [브랜드성 이미지 모음](https://hanatour0.sharepoint.com/:b:/s/msteams_7d230d/IQAZLz9HXqQFSqiY5FwHzB_WAZuSR2t7RgebFS8gfVSjbjE?e=iQwF0L)

■ 유의사항
① 인물 이미지 사용 시, 최종 시안을 공유해 주세요. (검수가 아닌 단순 공유이니 부담 없이 생각해 주세요.)
모델 개별 계약이 체결되어 있어 인물별 활용 채널과 기간을 참고하기 위함입니다.
- 수신: 브랜드마케팅팀 천성해, 이승현, 백솜이
- 공유 항목: 최종 시안, 노출 채널, 노출 기간
② 고해상 파일이 필요하신 경우, 파일명과 함께 문의해 주세요.
③ 대리점의 직접 사용은 불가합니다. (본사에서 제작하는 제작물만 사용 가능)
④ 하나투어가 아닌 제휴처를 홍보하는 콘텐츠에는 사용 불가합니다. (기준이 모호할 경우 문의해 주세요.)
⑤ 인물 이미지는 27년 7월 18일까지 사용 가능하며, 1년 단위로 계약 갱신 예정입니다.
⑥ 소품 이미지는 영구적으로 사용 가능합니다.

▶ 이미지 관련 문의: 이승현G 선임 (6725) / 백솜이 선임 (7051)
▶ 브랜드 체계·소개·정의 문의: 천성해 선임 (내선 1911)"""
}

# ─────────────────────────────────────
# Trigger Check Helper
# ─────────────────────────────────────

def check_fixed_answer(query: str) -> str | None:
    q = query.strip().lower()
    
    # 구체적인 세부 의문사/질문 수식어가 포함된 경우 FIXED-ANSWER 대신 CSV 개별 FAQ 검색 수행
    specific_qualifiers = [
        "dmc", "해외지사", "명함", "봉투", "x배너", "현수막", "신청", "절차", 
        "위치", "크기", "사이즈", "규격", "서식", "양식", "검수", "템플릿", "매장", "센터", "채널", "종류",
        "여백", "보호영역", "바꿔", "변경", "비율", "회전", "돌려", "그림자", "테두리", 
        "배경", "전달", "외부", "전용", "안전", "책임", "얼마나", "최소", "작게", 
        "무슨", "어떤", "무엇", "어디", "어디서", "왜", "어떻게", "기준", "써도", 
        "돼", "되나요", "가능", "가능해", "가능한가요", "설치", "만들어", "작은"
    ]
    
    # 구체적인 질문 수식어가 들어있는 문장은 CSV FAQ 검색으로 우선 전달
    if any(sq in q for sq in specific_qualifiers):
        # 단, 비즈링/내맘대로/하나프리팩/제우스 매니페스토 명시적 고정 키워드는 전용 답변 출력
        if "비즈링" in q and ("신청" in q or q in ["비즈링", "biz ring", "통화연결음"]):
            return FIXED_ANSWERS["비즈링"]
        if "하나프리팩" in q:
            return FIXED_ANSWERS["하나프리팩"]
        if "내맘대로" in q:
            return FIXED_ANSWERS["내맘대로"]
        if "매니페스토" in q:
            return FIXED_ANSWERS["제우스월드 매니페스토"]
        return None

    # 1. 비즈링
    bizring_triggers = ["비즈링", "biz ring", "비즈링 신청", "통화연결음", "회사 벨소리", "대기음", "비즈링 설정", "전화연결음", "하나투어 컬러링", "컬러링"]
    if any(k == q or k in q for k in bizring_triggers):
        return FIXED_ANSWERS["비즈링"]

    # 2. 하나프리팩
    freepack_triggers = ["하나프리팩", "하나프리팩 소개", "하나프리팩 뜻", "하나프리팩이 뭐야"]
    if any(k == q for k in freepack_triggers):
        return FIXED_ANSWERS["하나프리팩"]

    # 3. 브랜드 체계 (단독/대표 질의)
    arch_triggers = ["하나투어 브랜드 체계 아키텍처", "브랜드 체계 (4계층)", "브랜드 아키텍처", "브랜드 체계"]
    if q in arch_triggers:
        return FIXED_ANSWERS["브랜드 체계"]

    # 4. 내맘대로
    if "내맘대로" in q:
        return FIXED_ANSWERS["내맘대로"]

    # 5. 제우스월드 매니페스토
    if any(k in q for k in ["제우스월드 매니페스토", "제우스 매니페스토", "zeusworld 매니페스토", "경험의 기준을 높이다"]):
        return FIXED_ANSWERS["제우스월드 매니페스토"]
        
    # 6. 제우스월드 (단독/대표 질의)
    if q in ["제우스월드", "제우스 월드", "zeusworld", "제우스월드 브랜드 라인업", "제우스월드 소개"]:
        return FIXED_ANSWERS["제우스월드"]

    # 7. 로고 (단독/대표 질의만 매칭)
    logo_triggers = ["로고", "로고 다운로드", "하나투어 로고", "브랜드 로고", "로고 파일", "ci 다운로드", "bi 다운로드", "로고 ci/bi 다운로드"]
    if q in logo_triggers or q in ["ci", "bi", "ci/bi"]:
        return FIXED_ANSWERS["로고"]

    # 8. 간판 / 사인시스템 (단독/대표 질의만 매칭)
    sign_triggers = ["간판", "사인시스템", "대리점 간판", "대리점 간판 설치 ci 사용 규정", "대리점 간판 설치"]
    if q in sign_triggers:
        return FIXED_ANSWERS["간판"]

    # 9. 대리점 템플릿
    template_triggers = ["대리점 템플릿", "공식인증예약센터 대리점 템플릿", "대리점 ppt"]
    if q in template_triggers:
        return FIXED_ANSWERS["대리점 템플릿"]

    # 10. SNS
    sns_triggers = ["sns", "sns 운영 규정 알려줘", "sns 유의사항", "sns 게시물 규정", "sns 체크리스트"]
    if q in sns_triggers:
        return FIXED_ANSWERS["sns"]

    # 11. 폰트 (단독/대표 질의만 매칭)
    font_triggers = ["폰트", "서체", "글꼴", "폰트 다운로드", "서체 다운로드", "하나투어 폰트 지정서체 다운로드"]
    if q in font_triggers:
        return FIXED_ANSWERS["폰트"]

    # 12. 수상이력
    award_triggers = ["수상이력", "수상 내역", "수상 실적", "수상 내역 실적 알려줘", "주요 수상 및 인증 실적"]
    if q in award_triggers:
        return FIXED_ANSWERS["수상이력"]

    # 13. 담당자
    contact_triggers = ["브랜드 담당자 연락처", "브랜드 문의 담당자", "담당자 연락처", "브랜드팀 연락처", "담당자"]
    if q in contact_triggers:
        return FIXED_ANSWERS["담당자"]

    # 14. 컬러 (단독/대표 질의만 매칭)
    color_triggers = ["컬러", "브랜드 컬러", "컬러 가이드", "컬러 가이드 규정 알려줘", "브랜드 컬러 규정"]
    if q in color_triggers:
        return FIXED_ANSWERS["컬러"]

    # 15. 브랜드 이미지 (홍보물 이미지, 사용 가능한 이미지, 사진 소스 등 포함)
    img_keywords = [
        "브랜드 이미지", "브랜드성 이미지", "인물 이미지", "소품 이미지", "모델 이미지", 
        "이미지 소스", "이미지 다운로드", "이미지 파일", "브랜드 사진", "모델 사진", 
        "소품 사진", "이미지 프리뷰", "446컷", "홍보물 이미지", "사용할 수 있는 이미지",
        "사용 가능한 이미지", "이미지 넣고", "이미지 필요", "이미지 446컷"
    ]
    if any(k in q for k in img_keywords) or ("이미지" in q and ("사용" in q or "홍보물" in q or "사진" in q or "다운" in q or "넣고" in q or "있어" in q or "있을까" in q or "있나요" in q)):
        return FIXED_ANSWERS["브랜드이미지"]
        
    return None

# ─────────────────────────────────────
# Gemini API Answer Generation
# ─────────────────────────────────────

def generate_brand_response(query: str, search_results: List[Dict[str, Any]]) -> str:
    """FIXED-ANSWER 감지 시 고정 답변 출력, 일반 질문 시 Gemini API 또는 규칙 응답 생성"""
    fixed = check_fixed_answer(query)
    if fixed:
        return fixed
        
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            if hasattr(st, "secrets"):
                api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")
        except Exception:
            pass
    
    context_str = ""
    if search_results:
        context_items = []
        for idx, item in enumerate(search_results, 1):
            link_info = f"\n  - 링크: {item['link']}" if item.get('link') else ""
            context_items.append(
                f"[항목 {idx} - 가중치점수 {item['score']}점]\n"
                f"  - 질문: {item['question']}\n"
                f"  - 키워드: {item['keyword']}\n"
                f"  - 답변: {item['answer']}{link_info}"
            )
        context_str = "\n\n".join(context_items)
    else:
        context_str = "검색된 관련 CSV 데이터 항목이 없습니다."

    prompt_file = os.path.join(os.path.dirname(__file__), "FINAL_VERSION_지시문.txt")
    if os.path.exists(prompt_file):
        with open(prompt_file, "r", encoding="utf-8") as f:
            system_prompt = f.read()
    else:
        system_prompt = "너는 하나투어 브랜드 가이드라인 전문 AI 어시스턴트 '브랜드 똑순이'야. CSV 데이터에 있는 정보만으로 답변하고, 없는 정보는 절대 지어내지 마. 답변은 친절하고 구조적으로 해줘."

    prompt = f"""[사용자 질문]: {query}

[참고 데이터 - CSV 검색 결과]:
{context_str}

위 CSV 검색 결과의 내용만을 바탕으로 사용자 질문에 대해 친절하고 명확한 마크다운 문장으로 답변하세요.
관련 링크가 있는 경우 [다운로드](링크) 또는 [바로가기](링크) 형식으로 함께 제공하세요.
데이터에 없는 내용은 지어내지 마세요.
"""

    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config={'system_instruction': system_prompt}
            )
            return response.text.replace('\\n', '\n')
        except Exception as e:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)
                res = model.generate_content(prompt)
                return res.text.replace('\\n', '\n')
            except Exception as e2:
                print(f"Gemini API Call failed: {e2}")

    # Fallback when no API Key is set: Synthesize directly from search results
    if search_results:
        if len(search_results) == 1:
            item = search_results[0]
            link_str = f"\n\n▶ [관련 다운로드/바로가기]({item['link']})" if item.get('link') else ""
            return f"{item['answer']}{link_str}\n\n▶ 브랜드 검수·디자인 문의: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)".replace('\\n', '\n')

        res_parts = []
        for idx, item in enumerate(search_results, 1):
            q_clean = item['question']
            a_clean = item['answer']
            link_str = f"\n  ▶ [관련 다운로드/바로가기]({item['link']})" if item.get('link') else ""
            res_parts.append(f"**{idx}. {q_clean}**\n{a_clean}{link_str}")
        res_parts.append("\n▶ 브랜드 검수·디자인 문의: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)")
        return "\n\n".join(res_parts).replace('\\n', '\n')
    else:
        return """요청하신 내용에 관한 세부 규정은 브랜드 담당자에게 확인해 주시기 바랍니다.

▶ 문의 담당자
· 브랜드 검수·디자인: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)
· 수상인증·비즈링·브랜드체계: 천성해 선임 (내선 1911)""".replace('\\n', '\n')
