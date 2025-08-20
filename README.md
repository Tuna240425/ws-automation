# BGN 밝은눈안과 블로그 자동화 시스템

인터뷰 → AI 분석 → 블로그 작성 → 이미지 생성 → 워드프레스 발행의 완전 자동화 시스템

## 🚀 빠른 시작

### 1. 프로젝트 설정

```bash
# 새 폴더 생성 및 이동
mkdir bgn_blog_automation
cd bgn_blog_automation

# 가상환경 생성 (권장)
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 2. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 3. 폴더 구조 생성

```
bgn_blog_automation/
├── main.py
├── config.py
├── requirements.txt
├── utils/
│   ├── __init__.py
│   ├── session_manager.py
│   ├── ai_analyzer.py
│   └── file_handler.py
└── components/
    ├── __init__.py
    ├── file_upload.py
    ├── material_analysis.py
    ├── blog_writer.py
    ├── image_generator.py
    └── wordpress_publisher.py
```

### 4. __init__.py 파일 생성

```bash
# utils와 components 폴더에 빈 __init__.py 파일 생성
touch utils/__init__.py
touch components/__init__.py
```

### 5. 환경 변수 설정 (선택사항)

`.env` 파일 생성:
```env
OPENAI_API_KEY=your_openai_api_key_here
WORDPRESS_URL=https://brighteye.co.kr
WORDPRESS_USERNAME=your_username
WORDPRESS_PASSWORD=your_password
```

### 6. 실행

```bash
streamlit run main.py
```

## 📁 파일별 역할

### 핵심 파일
- **`main.py`**: 메인 앱 진입점, 페이지 라우팅
- **`config.py`**: 모든 설정값 관리
- **`requirements.txt`**: 필요한 라이브러리 목록

### utils/ (유틸리티 함수)
- **`session_manager.py`**: Streamlit 세션 상태 관리
- **`ai_analyzer.py`**: OpenAI API를 사용한 AI 분석
- **`file_handler.py`**: 파일 업로드 및 처리

### components/ (UI 컴포넌트)
- **`file_upload.py`**: 1단계 - 인터뷰 파일 업로드
- **`material_analysis.py`**: 2단계 - 콘텐츠 소재 도출
- **`blog_writer.py`**: 3단계 - 블로그 작성
- **`image_generator.py`**: 4단계 - 이미지 생성
- **`wordpress_publisher.py`**: 5단계 - 워드프레스 발행

## 🔧 주요 기능

### ✅ 현재 구현된 기능
- [x] 모듈화된 프로젝트 구조
- [x] 파일 업로드 (TXT, DOCX, PDF)
- [x] OpenAI API를 사용한 실제 AI 분석
- [x] 5가지 유형별 콘텐츠 소재 분류
- [x] 소재 기반 블로그 자동 작성
- [x] 세션 상태 관리
- [x] 사용자 친화적 UI

### 🚧 개발 예정 기능
- [ ] 이미지 생성 (DALL-E 연동)
- [ ] 워드프레스 자동 발행
- [ ] HWP 파일 처리
- [ ] 음성 파일 텍스트 변환 (STT)
- [ ] 데이터베이스 연동
- [ ] 사용자 인증 시스템

## 🛠️ 개발자 가이드

### 새 컴포넌트 추가하기

1. `components/` 폴더에 새 파일 생성
2. `render_[component_name]_page()` 함수 정의
3. `main.py`에서 import 및 라우팅 추가

### 설정값 수정하기

모든 설정값은 `config.py`에서 관리합니다.

### API 추가하기

`utils/` 폴더에 새 API 모듈을 추가하고 `config.py`에 설정값을 추가하세요.

## 🔍 트러블슈팅

### 일반적인 문제

1. **ModuleNotFoundError**: `pip install -r requirements.txt` 재실행
2. **OpenAI API 오류**: API 키 확인 및 크레딧 잔액 확인
3. **파일 업로드 실패**: 파일 크기 및 형식 확인

### 개발 환경에서만 발생하는 문제

- **상대 import 오류**: Python 경로 설정 확인
- **Streamlit rerun 오류**: 최신 Streamlit 버전 사용

## 📞 문의

개발 관련 문의나 버그 신고는 이슈로 등록해주세요.