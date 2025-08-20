import streamlit as st
from pathlib import Path

def process_uploaded_file(uploaded_file):
    """업로드된 파일을 처리하여 텍스트 내용 반환"""
    
    file_type = uploaded_file.type
    file_name = uploaded_file.name
    file_extension = Path(file_name).suffix.lower()
    
    try:
        if file_type == "text/plain" or file_extension == ".txt":
            # 텍스트 파일 처리
            content = str(uploaded_file.read(), "utf-8")
            return content
            
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or file_extension == ".docx":
            # DOCX 파일 처리
            return process_docx_file(uploaded_file)
            
        elif file_type == "application/pdf" or file_extension == ".pdf":
            # PDF 파일 처리
            return process_pdf_file(uploaded_file)
            
        elif file_extension == ".hwp":
            # HWP 파일 처리 (추후 구현)
            st.warning("HWP 파일은 현재 개발 중입니다. 텍스트나 DOCX 파일을 사용해주세요.")
            return "HWP 파일 처리는 추후 지원 예정입니다."
            
        else:
            raise ValueError(f"지원하지 않는 파일 형식입니다: {file_type}")
            
    except Exception as e:
        raise Exception(f"파일 처리 중 오류 발생: {str(e)}")

def process_docx_file(uploaded_file):
    """DOCX 파일에서 텍스트 추출"""
    try:
        import docx
        
        # 파일을 메모리에서 직접 처리
        doc = docx.Document(uploaded_file)
        
        # 모든 단락의 텍스트 추출
        full_text = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():  # 빈 줄이 아닌 경우만
                full_text.append(paragraph.text)
        
        return "\n".join(full_text)
        
    except ImportError:
        st.error("DOCX 파일 처리를 위해 python-docx 라이브러리가 필요합니다.")
        st.code("pip install python-docx")
        raise Exception("python-docx 라이브러리가 설치되지 않았습니다.")
    except Exception as e:
        raise Exception(f"DOCX 파일 처리 실패: {str(e)}")

def process_pdf_file(uploaded_file):
    """PDF 파일에서 텍스트 추출"""
    try:
        import PyPDF2
        
        # PDF 리더 생성
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        
        # 모든 페이지의 텍스트 추출
        full_text = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text.strip():  # 빈 페이지가 아닌 경우만
                full_text.append(text)
        
        return "\n".join(full_text)
        
    except ImportError:
        st.error("PDF 파일 처리를 위해 PyPDF2 라이브러리가 필요합니다.")
        st.code("pip install PyPDF2")
        raise Exception("PyPDF2 라이브러리가 설치되지 않았습니다.")
    except Exception as e:
        raise Exception(f"PDF 파일 처리 실패: {str(e)}")

def validate_file_size(uploaded_file, max_size_mb=10):
    """파일 크기 검증"""
    file_size_mb = uploaded_file.size / (1024 * 1024)
    
    if file_size_mb > max_size_mb:
        raise Exception(f"파일 크기가 너무 큽니다. (현재: {file_size_mb:.1f}MB, 최대: {max_size_mb}MB)")
    
    return True

def get_file_info(uploaded_file):
    """업로드된 파일의 정보 반환"""
    file_size_mb = uploaded_file.size / (1024 * 1024)
    
    return {
        "name": uploaded_file.name,
        "type": uploaded_file.type,
        "size_mb": round(file_size_mb, 2),
        "extension": Path(uploaded_file.name).suffix.lower()
    }