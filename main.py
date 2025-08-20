import streamlit as st
from components.file_upload import render_file_upload_page
from components.material_analysis import render_material_analysis_page
from components.blog_writer import render_blog_writer_page
from components.image_generator import render_image_generator_page
from components.wordpress_publisher import render_wordpress_publisher_page
from utils.session_manager import initialize_session_state, get_step_info
from config import APP_CONFIG

# 페이지 설정
st.set_page_config(
    page_title=APP_CONFIG["page_title"],
    page_icon=APP_CONFIG["page_icon"],
    layout=APP_CONFIG["layout"],
    initial_sidebar_state=APP_CONFIG["sidebar_state"]
)

# 세션 상태 초기화
initialize_session_state()

# 사이드바 - 진행 단계 표시
def render_sidebar():
    st.sidebar.title("📋 진행 단계")
    
    # API 키 설정
    with st.sidebar.expander("⚙️ API 설정", expanded=False):
        openai_api_key = st.text_input(
            "OpenAI API Key", 
            type="password",
            help="OpenAI API 키를 입력하세요",
            key="openai_api_key"
        )
        if openai_api_key:
            st.success("✅ API 키가 설정되었습니다")
            st.session_state.openai_api_key = openai_api_key
        else:
            st.warning("⚠️ API 키를 입력해주세요")
    
    # 진행 단계 표시
    steps = get_step_info()
    for i, step in enumerate(steps, 1):
        if i == st.session_state.step:
            st.sidebar.markdown(f"**🔄 {step}**")
        elif i < st.session_state.step:
            st.sidebar.markdown(f"✅ {step}")
        else:
            st.sidebar.markdown(f"⏳ {step}")

# 메인 앱
def main():
    # 사이드바 렌더링
    render_sidebar()
    
    # 메인 헤더
    st.title(APP_CONFIG["main_title"])
    st.markdown("---")
    
    # 단계별 페이지 렌더링
    if st.session_state.step == 1:
        render_file_upload_page()
    elif st.session_state.step == 2:
        render_material_analysis_page()
    elif st.session_state.step == 3:
        render_blog_writer_page()
    elif st.session_state.step == 4:
        render_image_generator_page()
    elif st.session_state.step == 5:
        render_wordpress_publisher_page()
    
    # 하단 정보
    st.markdown("---")
    st.markdown(APP_CONFIG["footer_text"])

if __name__ == "__main__":
    main()