# BGN 밝은눈안과 블로그 자동화 시스템 설정

# Streamlit 앱 설정
APP_CONFIG = {
    "page_title": "BGN 밝은눈안과 블로그 자동화",
    "page_icon": "👁️",
    "layout": "wide",
    "sidebar_state": "expanded",
    "main_title": "👁️ BGN 밝은눈안과 블로그 자동화 시스템",
    "footer_text": "💡 **BGN 밝은눈안과 블로그 자동화 시스템** | Made with ❤️"
}

# OpenAI API 설정
OPENAI_CONFIG = {
    "model": "gpt-4-turbo-preview",
    "max_tokens": 3000,
    "temperature": 0.7,
    "analysis_max_tokens": 3000,
    "blog_max_tokens": 2000
}

# 파일 업로드 설정
FILE_CONFIG = {
    "allowed_types": ['txt', 'docx', 'pdf', 'hwp'],
    "max_size_mb": 10,
    "upload_help": "지원 형식: TXT, DOCX, PDF, HWP"
}

# 워드프레스 설정
WORDPRESS_CONFIG = {
    "default_url": "https://brighteye.co.kr",
    "api_endpoint": "/wp-json/wp/v2",
    "default_categories": ["치료후기", "수술후기", "안과상식", "병원소식"],
    "default_tags": "안과, 치료후기, 밝은눈안과"
}

# 블로그 작성 설정
BLOG_CONFIG = {
    "styles": [
        "전문적이고 신뢰성 있는 톤",
        "친근하고 이해하기 쉬운 톤", 
        "환자 중심의 공감적 톤",
        "직원 경험담 중심 톤"
    ],
    "audiences": [
        "일반 환자",
        "안과 질환 관심자",
        "의료진",
        "병원 이용 예정자"
    ],
    "lengths": [
        "짧게 (800자)",
        "보통 (1200자)",
        "길게 (1800자)"
    ],
    "length_mapping": {
        "짧게 (800자)": "800자 내외",
        "보통 (1200자)": "1200자 내외",
        "길게 (1800자)": "1800자 내외"
    }
}

# 이미지 생성 설정
IMAGE_CONFIG = {
    "styles": [
        "의료진과 환자",
        "안과 진료실",
        "치료 과정",
        "수술 장면",
        "회복 과정"
    ],
    "moods": [
        "전문적이고 깔끔한",
        "따뜻하고 친근한",
        "희망적이고 밝은"
    ]
}

# 콘텐츠 소재 유형
CONTENT_TYPES = {
    "고객 에피소드형": {
        "description": "실제 환자의 치료 경험담, 특별한 케이스",
        "icon": "👥"
    },
    "검사·과정형": {
        "description": "검사 방법, 치료 과정, 의료 절차 설명", 
        "icon": "🔍"
    },
    "센터 운영/분위기형": {
        "description": "병원 문화, 직원 이야기, 시설 소개",
        "icon": "🏥"
    },
    "초년차 성장기형": {
        "description": "실수·배움 중심의 성장 스토리",
        "icon": "🌱"
    },
    "고객 질문 FAQ형": {
        "description": "상담 시 자주 나오는 질문과 답변",
        "icon": "❓"
    }
}

# 단계 정보
STEP_INFO = [
    "1️⃣ 인터뷰 업로드",
    "2️⃣ 콘텐츠 소재 도출", 
    "3️⃣ 소재 선택 및 블로그 작성",
    "4️⃣ 이미지 생성",
    "5️⃣ 워드프레스 발행"
]