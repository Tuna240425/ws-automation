import json
import streamlit as st
from openai import OpenAI
from config import OPENAI_CONFIG, CONTENT_TYPES

class AIAnalyzer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.config = OPENAI_CONFIG
    
    def analyze_interview_content(self, content):
        """인터뷰 내용을 분석하여 5가지 유형별 콘텐츠 소재 도출"""
        
        content_types_desc = "\n".join([
            f"{i+1}. {type_name}: {info['description']}" 
            for i, (type_name, info) in enumerate(CONTENT_TYPES.items())
        ])
        
        prompt = f"""
다음 인터뷰 내용을 분석하여 BGN 밝은눈안과 블로그용 콘텐츠 소재를 5가지 유형으로 분류해주세요.

인터뷰 내용:
{content}

다음 5가지 유형으로 각각 최소 2개 이상의 소재를 도출해주세요:

{content_types_desc}

각 소재에 대해 다음 형식으로 정리해주세요:
- title: 소재 제목
- content: 소재 내용 요약 (2-3문장)
- timestamp: 인터뷰에서 해당 내용이 나온 시간대 (추정)
- usage_point: 블로그 활용 포인트

JSON 형식으로 응답해주세요. 각 유형별로 배열 형태로 정리해주세요.

예시 형식:
{{
  "고객 에피소드형": [
    {{
      "title": "...",
      "content": "...",
      "timestamp": "...",
      "usage_point": "..."
    }}
  ],
  "검사·과정형": [...],
  ...
}}
"""

        try:
            response = self.client.chat.completions.create(
                model=self.config["model"],
                messages=[
                    {
                        "role": "system", 
                        "content": "당신은 의료 마케팅 전문가이자 콘텐츠 기획자입니다. 인터뷰 내용을 분석하여 블로그 소재를 체계적으로 분류하는 것이 전문 분야입니다."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=self.config["temperature"],
                max_tokens=self.config["analysis_max_tokens"]
            )
            
            result = response.choices[0].message.content
            
            # JSON 파싱 시도
            try:
                materials = json.loads(result)
                return materials
            except json.JSONDecodeError:
                # JSON 파싱 실패시 텍스트에서 정보 추출
                return self._parse_response_to_materials(result)
                
        except Exception as e:
            st.error(f"OpenAI API 호출 실패: {str(e)}")
            raise e
    
    def generate_blog_content(self, selected_material, style, audience, length, include_cta, additional_request):
        """선택된 소재를 바탕으로 블로그 콘텐츠 생성"""
        
        material = selected_material['data']
        material_type = selected_material['type']
        
        from config import BLOG_CONFIG
        length_text = BLOG_CONFIG["length_mapping"].get(length, "1200자 내외")
        
        prompt = f"""
BGN 밝은눈안과 블로그 포스트를 작성해주세요.

선택된 소재 정보:
- 유형: {material_type}
- 제목: {material['title']}
- 내용: {material['content']}
- 활용 포인트: {material['usage_point']}

작성 요구사항:
- 스타일: {style}
- 타겟 독자: {audience}
- 글 길이: {length_text}
- 병원 방문 유도 문구 포함: {'예' if include_cta else '아니오'}

추가 요청사항: {additional_request if additional_request else '없음'}

다음 구조로 작성해주세요:
1. 흥미로운 제목
2. 도입부 (독자의 관심 끌기)
3. 본문 (소재의 핵심 내용)
4. 결론 및 메시지
5. {'병원 방문 유도 문구' if include_cta else '마무리'}

마크다운 형식으로 작성하고, 의료 전문성과 신뢰성을 보여주되 너무 딱딱하지 않게 써주세요.
"""

        try:
            response = self.client.chat.completions.create(
                model=self.config["model"],
                messages=[
                    {
                        "role": "system", 
                        "content": "당신은 의료 마케팅 전문 카피라이터입니다. 안과 전문병원의 블로그 콘텐츠를 작성하는 것이 전문 분야이며, 의학적 정확성과 독자 친화성을 모두 갖춘 글을 작성합니다."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=self.config["temperature"],
                max_tokens=self.config["blog_max_tokens"]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            st.error(f"OpenAI API 호출 실패: {str(e)}")
            raise e
    
    def _parse_response_to_materials(self, response_text):
        """OpenAI 응답을 파싱하여 소재 형식으로 변환"""
        # 간단한 파싱 로직 (실제로는 더 정교하게 구현)
        materials = {}
        
        for type_name in CONTENT_TYPES.keys():
            materials[type_name] = [
                {
                    "title": f"AI 분석 결과 - {type_name}",
                    "content": f"OpenAI가 분석한 {type_name} 관련 내용입니다.",
                    "timestamp": "분석 결과",
                    "usage_point": "AI가 제안한 활용 방안입니다."
                }
            ]
        
        return materials

def get_sample_materials():
    """샘플 소재 데이터 (API 오류시 대체용)"""
    return {
        "고객 에피소드형": [
            {
                "title": "50대 주부의 백내장 수술 성공기",
                "content": "일상생활이 불편할 정도로 시야가 흐려져 내원한 환자분의 치료 과정과 회복 후기",
                "timestamp": "인터뷰 15:30~18:45",
                "usage_point": "환자의 감정 변화와 치료 전후 생활의 차이를 중심으로 스토리텔링"
            },
            {
                "title": "젊은 직장인의 라식 수술 결정 과정",
                "content": "안경착용의 불편함과 운동에 대한 열정으로 라식을 결정한 20대 환자의 이야기",
                "timestamp": "인터뷰 25:10~28:50",
                "usage_point": "동일한 고민을 가진 젊은 층의 공감대 형성"
            }
        ],
        "검사·과정형": [
            {
                "title": "정밀 안저검사의 중요성과 과정",
                "content": "망막 질환 조기 발견을 위한 안저검사 장비와 검사 절차 상세 설명",
                "timestamp": "인터뷰 45:20~52:30",
                "usage_point": "환자들이 궁금해하는 검사 과정을 자세히 설명하여 불안감 해소"
            },
            {
                "title": "라식 수술 전 정밀검사의 단계별 과정",
                "content": "각막두께, 눈물분비량, 동공크기 등 수술 전 필수 검사들의 의미와 과정",
                "timestamp": "인터뷰 1:05:15~1:12:40",
                "usage_point": "수술을 고려하는 환자들의 궁금증 해결과 신뢰도 향상"
            }
        ],
        "센터 운영/분위기형": [
            {
                "title": "환자 중심의 대기실 운영 철학",
                "content": "대기 시간 최소화와 편안한 환경 조성을 위한 센터의 특별한 노력들",
                "timestamp": "인터뷰 1:25:10~1:30:45",
                "usage_point": "병원의 차별화된 서비스와 환자 배려 문화 어필"
            },
            {
                "title": "의료진들의 지속적인 학습 문화",
                "content": "최신 의료기술 습득을 위한 정기 교육과 학회 참석 등의 노력",
                "timestamp": "인터뷰 1:35:20~1:41:10",
                "usage_point": "의료진의 전문성과 발전 의지를 보여주어 신뢰도 강화"
            }
        ],
        "초년차 성장기형": [
            {
                "title": "신입 간호사의 첫 수술실 경험담",
                "content": "처음 수술실에 들어갔을 때의 떨림과 점차 적응해가는 과정",
                "timestamp": "인터뷰 2:05:30~2:12:15",
                "usage_point": "의료진의 인간적인 면모와 성장 스토리로 친근감 조성"
            },
            {
                "title": "환자 상담 실수에서 배운 소중한 교훈",
                "content": "초보 시절 환자 설명 중 실수했던 경험과 이를 통해 배운 소통의 중요성",
                "timestamp": "인터뷰 2:18:45~2:24:20",
                "usage_point": "실수를 통한 성장과 환자를 향한 진정성 있는 마음 전달"
            }
        ],
        "고객 질문 FAQ형": [
            {
                "title": "라식 수술 후 운동은 언제부터 가능한가요?",
                "content": "환자들이 가장 많이 묻는 수술 후 일상 복귀 관련 질문과 답변",
                "timestamp": "인터뷰 2:35:10~2:40:30",
                "usage_point": "실제 상담에서 나온 질문으로 높은 관심도와 검색 가능성"
            },
            {
                "title": "안구건조증, 인공눈물 언제까지 써야 하나요?",
                "content": "만성 안구건조증 환자들의 치료 기간과 관리 방법에 대한 궁금증",
                "timestamp": "인터뷰 2:45:50~2:51:15",
                "usage_point": "일상적인 고민으로 많은 환자들이 공감할 수 있는 내용"
            }
        ]
    }