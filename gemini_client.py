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
한 줄 요약: 제작물에서 가장 많이 써야 하는 색상입니다.

- 대표·확장 색상은 브랜드를 대표하는 주(主) 색상이므로, 모든 시각물에 기본적으로 적용합니다.
- 강조 색상과 함께 쓸 때 → 대표·확장 색상이 면적의 **40% 이상**을 차지해야 합니다.
- 로고에는 대표 색상과 흑백만 적용 가능합니다. (확장 색상은 로고에 사용 불가)
- 확장 색상은 단독으로도 활용 가능하며, 콘텐츠 성격에 따라 주 색상으로 쓸 수 있습니다.

**3. 파생·보조 색상 (= 보완 컬러)**
한 줄 요약: 메인 컬러를 도와주는 역할이며, 단독으로는 쓸 수 없습니다.

- 파생·보조 색상은 반드시 대표·확장 색상과 함께 활용해야 합니다. (단독 사용 불가, 흑백 규정은 예외)
- 디자인 구성에 따라 활용 비율을 유연하게 조정할 수 있습니다.

**4. 강조 색상 (= 포인트 컬러)**
한 줄 요약: 눈에 띄어야 하는 곳에만 소량 사용하고, 절대 많이 쓰면 안 됩니다.

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

    "간판": """하나투어 대리점 및 매장 유형별 간판 제작 및 CI 사용 규정을 안내해 드립니다.

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

─── 사인시스템 에셋 ───

공식인증예약센터 등 CI 사용 승인 매장에 한해 적용되는 간판 및 사인시스템 제작용 가이드라인 및 디자인 에셋 다운로드 링크를 안내해 드립니다.
용도에 맞춰 필요한 에셋을 확인해 보시기 바랍니다.

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

※ 사인시스템 에셋은 공식인증예약센터 등 CI 사용 승인 매장에 한해 적용됩니다.

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
  → 천성해 선임 (내선 1911)"""
}

# ─────────────────────────────────────
# Trigger Check Helper
# ─────────────────────────────────────

def check_fixed_answer(query: str) -> str | None:
    q = query.strip().lower()
    
    # 1. 간판 / 사인시스템 (최우선: '간판 설치 CI 규정' 등에서 'ci' 키워드로 인해 로고로 잘못 빠지는 문제 방지)
    sign_triggers = ["간판", "사인시스템", "현판", "윈도우그래픽", "가로입체bar", "대리점 간판", "간판 규정", "간판 설치", "ci 간판", "공식인증예약센터 간판"]
    if any(k in q for k in sign_triggers):
        return FIXED_ANSWERS["간판"]

    # 2. 대리점 템플릿
    template_triggers = ["대리점 템플릿", "대리점 디자인", "대리점 양식", "대리점 홍보물", "대리점 ppt", "홍보물 템플릿"]
    if any(k in q for k in template_triggers):
        return FIXED_ANSWERS["대리점 템플릿"]

    # 3. 제우스월드 매니페스토 (우선순위)
    if any(k in q for k in ["제우스월드 매니페스토", "제우스 매니페스토", "zeusworld 매니페스토", "제우스월드 슬로건", "경험의 기준을 높이다"]):
        return FIXED_ANSWERS["제우스월드 매니페스토"]
        
    # 4. 제우스월드
    if any(k in q for k in ["제우스월드", "제우스 월드", "zeusworld", "하이엔드 브랜드", "하이엔드 여행", "제우스 프라이빗"]):
        return FIXED_ANSWERS["제우스월드"]

    # 5. 로고 (FIXED-ANSWER: 로고)
    logo_triggers = ["로고", "로고 다운로드", "하나투어 로고", "브랜드 로고", "심볼", "심벌", "워드마크", "시그니처", "로고 파일", "로고 규정", "로고 사용", "ci 다운로드", "bi 다운로드", "제우스 로고", "밍글링 로고", "티라운지 로고", "티데스크 로고", "하나팩 로고", "예약센터 로고"]
    if any(k in q for k in logo_triggers) or (("ci" in q or "bi" in q) and not any(ex in q for ex in ["간판", "템플릿", "매장", "센터"])):
        return FIXED_ANSWERS["로고"]

    # 6. SNS (FIXED-ANSWER: SNS)
    sns_triggers = ["sns", "sns 규정", "sns 운영", "콘텐츠 운영", "콘텐츠 규정", "sns 유의사항", "게시물 규정", "sns 브랜드 규정", "밈", "밈 사용", "인스타그램 규정", "유튜브 규정", "콘텐츠 제작 규정", "sns 체크리스트", "게시 전 체크리스트", "브랜드 안전", "콘텐츠 검수"]
    if any(k in q for k in sns_triggers):
        return FIXED_ANSWERS["sns"]

    # 7. 폰트 (FIXED-ANSWER: 폰트)
    font_triggers = ["폰트", "서체", "글꼴", "폰트 다운로드", "서체 다운로드", "본고딕", "inter", "여행그자체", "공식 서체", "지정 서체", "글씨체", "타이포그래피", "영문 폰트", "국문 폰트", "브랜드 폰트"]
    if any(k in q for k in font_triggers):
        return FIXED_ANSWERS["폰트"]

    # 8. 수상이력 (FIXED-ANSWER: 수상이력)
    award_triggers = ["수상이력", "수상", "인증", "수상 내역", "수상 실적", "브랜드파워", "브랜드스타", "고객만족도", "서비스품질", "k-bpi", "kcsi", "ks-sqi", "좋은 광고상", "중앙광고대상", "sns 대상", "존경받는 기업", "국가서비스대상", "뉴욕페스티벌"]
    if any(k in q for k in award_triggers):
        return FIXED_ANSWERS["수상이력"]

    # 9. 담당자 (FIXED-ANSWER: 담당자)
    contact_triggers = ["담당자", "문의", "누구한테", "연락처", "내선", "전화번호", "누구에게 물어봐", "담당", "연락", "문의처", "브랜드팀 연락처"]
    if any(k in q for k in contact_triggers):
        return FIXED_ANSWERS["담당자"]

    # 10. 컬러
    if any(k in q for k in ["컬러", "브랜드 컬러", "컬러 가이드", "메인 컬러", "퍼플", "민트", "hex", "cmyk", "rgb", "강조색상", "강조 색상", "강조", "포인트 컬러", "포인트컬러", "보완컬러", "보완 컬러", "대표 색상", "확장 색상"]):
        return FIXED_ANSWERS["컬러"]
        
    return None

# ─────────────────────────────────────
# Gemini API Answer Generation
# ─────────────────────────────────────

def generate_brand_response(query: str, search_results: List[Dict[str, Any]]) -> str:
    """FIXED-ANSWER 감지 시 고정 답변 출력, 일반 질문 시 Gemini API 또는 규칙 응답 생성"""
    fixed = check_fixed_answer(query)
    if fixed:
        return fixed
        
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    
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
        system_prompt = "너는 하나투어 브랜드 가이드라인 전문 AI 어시스턴트 '브랜드 지킴이'야. CSV 데이터에 있는 정보만으로 답변하고, 없는 정보는 절대 지어내지 마. 답변은 친절하고 구조적으로 해줘."

    # 2. FIXED-ANSWER 트리거 감지
    query_lower = query.lower()
    
    fixed_triggers = ['로고', 'ci', 'bi', '심볼', '심벌', '워드마크', '시그니처',
                      'sns', '밈', '인스타그램', '유튜브', '콘텐츠 운영', '게시물 규정',
                      '폰트', '서체', '글꼴', '본고딕', 'inter', '여행그자체',
                      '수상이력', '수상', '인증', '브랜드파워', '브랜드스타', 'k-bpi', 'kcsi', 'ks-sqi',
                      '담당자', '문의', '연락처', '내선', '전화번호', '문의처',
                      '컬러 규정', '브랜드 컬러', '색상 규정', '컬러 가이드', '퍼플 컬러', '민트 컬러',
                      '브랜드 검수', '제작물 검수', '검수 방법', '검수 게시판', '검수 요청']
    
    is_fixed = any(trigger in query_lower for trigger in fixed_triggers)
    
    if is_fixed:
        # FIXED-ANSWER 질문: 시스템 프롬프트의 고정 답변 블록 참조
        prompt = f"""[사용자 질문]: {query}

이 질문은 시스템 프롬프트의 FIXED-ANSWER에 정답이 있는 질문입니다.
시스템 프롬프트에서 해당 FIXED-ANSWER 블록을 찾아 내용 수정 없이 그대로 출력하세요.
요약하거나 다른 정보를 섞지 마세요.
"""
    else:
        # 일반 질문 (로고, 폰트, 간판, 에셋 등): CSV 검색 결과 활용
        prompt = f"""[사용자 질문]: {query}

[참고 데이터 - CSV 검색 결과]:
{context_str}

시스템 프롬프트의 톤·형식·담당자 규칙 및 지침(로고/폰트/간판 등)에 따라 위 CSV 검색 결과 항목들을 모두 충실히 종합하여 친절하고 정확하게 답변하세요.
"""

    if api_key:
        try:
            # Try new google-genai package standard
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
                # Fallback to google-generativeai legacy package if installed
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)
                res = model.generate_content(prompt)
                return res.text.replace('\\n', '\n')
            except Exception as e2:
                print(f"Gemini API Call failed: {e2}")

    # Fallback when no API Key is set: Synthesize directly from search results
    if search_results:
        res_parts = ["요청하신 내용에 관련된 하나투어 가이드라인 검색 결과입니다:\n"]
        for idx, item in enumerate(search_results, 1):
            link_str = f"\n  ▶ [관련 자료 바로가기]({item['link']})" if item.get('link') else ""
            res_parts.append(f"**{idx}. {item['question']}**\n{item['answer']}{link_str}")
        res_parts.append("\n▶ 브랜드 검수·디자인 문의: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)")
        return "\n\n".join(res_parts).replace('\\n', '\n')
    else:
        return """요청하신 내용에 관한 세부 규정은 브랜드 담당자에게 확인해 주시기 바랍니다.

▶ 문의 담당자
· 브랜드 검수·디자인: 이승현G 선임 (내선 6725) / 백솜이 선임 (내선 7051)
· 수상인증·비즈링·브랜드체계: 천성해 선임 (내선 1911)""".replace('\\n', '\n')
