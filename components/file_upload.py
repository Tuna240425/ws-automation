import streamlit as st
from config import FILE_CONFIG
from utils.session_manager import next_step
from utils.file_handler import process_uploaded_file

def render_file_upload_page():
    """1단계: 인터뷰 업로드 페이지"""
    
    st.header("1️⃣ 인터뷰 업로드")
    
    st.markdown("### 📁 직원 인터뷰 파일 업로드")
    st.markdown("인터뷰 대화내역이 담긴 파일을 업로드해주세요. (텍스트, 워드, PDF 등)")
    
    # 파일 업로더
    uploaded_file = st.file_uploader(
        "파일 선택",
        type=FILE_CONFIG["allowed_types"],
        help=FILE_CONFIG["upload_help"]
    )
    
    # 또는 직접 텍스트 입력
    st.markdown("### ✏️ 또는 직접 입력")
    direct_input = st.text_area(
        "인터뷰 내용을 직접 입력하세요",
        height=300,
        placeholder="인터뷰 대화내용을 여기에 붙여넣거나 입력하세요...",
        key="direct_input"
    )
    
    # 파일 처리 또는 직접 입력 처리
    if uploaded_file or direct_input.strip():
        if uploaded_file:
            try:
                content = process_uploaded_file(uploaded_file)
                st.session_state.interview_content = content
                st.session_state.interview_file = uploaded_file.name
                st.success(f"✅ 파일 '{uploaded_file.name}'이 성공적으로 업로드되었습니다.")
            except Exception as e:
                st.error(f"❌ 파일 처리 중 오류가 발생했습니다: {str(e)}")
                return
        else:
            st.session_state.interview_content = direct_input
            st.session_state.interview_file = "직접 입력"
            st.success("✅ 텍스트가 성공적으로 입력되었습니다.")
        
        # 업로드된 내용 미리보기
        with st.expander("📋 업로드된 인터뷰 내용 미리보기", expanded=False):
            preview_content = st.session_state.interview_content[:1000]
            if len(st.session_state.interview_content) > 1000:
                preview_content += "\n\n... (더 많은 내용이 있습니다)"
            st.text(preview_content)
        
        # 다음 단계 버튼
        if st.button("🔍 콘텐츠 소재 도출하기", type="primary", use_container_width=True):
            if st.session_state.interview_content.strip():
                next_step()
            else:
                st.error("인터뷰 내용이 비어있습니다.")
    
    else:
        st.info("📝 파일을 업로드하거나 직접 텍스트를 입력해주세요.")
        
        # 샘플 데이터 버튼 (테스트용)
        if st.button("🎯 샘플 데이터로 테스트하기", help="테스트용 샘플 인터뷰 데이터를 로드합니다"):
            sample_content = get_sample_interview()
            st.session_state.interview_content = sample_content
            st.session_state.interview_file = "샘플 데이터"
            st.success("✅ 샘플 데이터가 로드되었습니다.")
            st.rerun()

def get_sample_interview():
    """테스트용 샘플 인터뷰 데이터"""
    return """
[BGN 밝은눈안과 직원 인터뷰 - 2024.08.20]

Q: 최근에 기억에 남는 환자 케이스가 있나요?

A: 네, 지난주에 50대 주부분이 오셨는데요. 백내장이 많이 진행되어서 일상생활이 정말 불편하셨어요. 
요리하실 때 칼질하는 것도 무서워하시고, TV 시청도 제대로 못 하셨다고 하더라구요. 
수술 후에는 정말 새 세상을 본 것 같다며 눈물을 흘리셨어요.

Q: 검사 과정에서 환자들이 가장 궁금해하는 것은 무엇인가요?

A: 안저검사할 때 "왜 이런 검사를 하는지" 많이 물어보세요. 
특히 젊은 분들은 "눈에 별 문제없는데 왜 이렇게 자세히 보냐"고 하시는데, 
망막 질환은 조기 발견이 정말 중요하다고 설명드리면 이해해주세요.

Q: 병원 분위기나 운영에서 특별한 점이 있다면?

A: 저희는 대기시간을 최대한 줄이려고 노력해요. 
예약 시스템을 정말 체계적으로 관리하고, 환자분들이 기다리시는 동안 
불편하지 않도록 편안한 의자와 차분한 음악도 신경써서 준비했어요.

Q: 처음 이곳에서 일할 때 어려웠던 점은?

A: 처음에는 환자분들께 검사 설명할 때 너무 의학적인 용어를 많이 썼어요. 
한 번은 할머니께서 "무슨 말인지 하나도 모르겠다"고 하셔서 정말 반성했어요. 
그 후로는 쉬운 말로 설명하려고 노력하고 있어요.

Q: 환자들이 자주 하는 질문이 있나요?

A: "라식 수술 후 언제부터 운동할 수 있나요?"가 가장 많은 질문이에요. 
특히 헬스장 다니시는 분들이나 골프치시는 분들이 정말 많이 물어보세요. 
또 안구건조증 환자분들은 "인공눈물 언제까지 넣어야 하나요?"도 자주 물어보시고요.

Q: 의료진 교육이나 학습은 어떻게 이루어지나요?

A: 원장님이 정말 공부를 강조하세요. 매월 학회 참석하시고, 
저희에게도 최신 의료 동향을 항상 공유해주세요. 
새로운 장비 들어오면 전체 스태프 교육도 철저히 하고요.
"""