import streamlit as st
import time

# --- 1. 앱 설정 및 제목 ---
st.set_page_config(page_title="GNU 교육혁신처 규정 질문 챗봇")
st.title("🏛️ GNU 교육혁신처 입니다. 무엇이든 물어보세요")
st.markdown("규정에 관한 것을 질문해 주세요.")
# -------------------------

# --- 2. 채팅 기록 초기화 ---
# 'messages' 세션 상태에 채팅 기록을 저장합니다.
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "안녕하세요! GNU 교육혁신처 교육과정 규정에 대해 궁금한 점을 질문해 주세요."}
    ]
# -------------------------

# --- 3. 사용자 Gem(지식 기반) 응답 함수 (가상의 로직) ---
def get_gem_response(user_input: str) -> str:
    """
    사용자의 입력에 따라 GNU 교육혁신처 Gem이 응답하는 로직을 구현합니다.
    실제로는 이 부분에서 RAG, LangChain, LlamaIndex 등을 사용하여
    'GNU 교육혁신처 교육과정' 문서를 기반으로 답변을 생성해야 합니다.
    """
    # 임시 응답 로직 (질문에 따라 응답이 달라지는 뼈대)
    
    # 핵심 키워드 체크
    if any(keyword in user_input for keyword in ["교육과정", "이수", "졸업"]):
        return "교육과정 이수 및 졸업 규정에 관한 문의사항이시군요. 상세 규정은 교육혁신처 홈페이지에서 확인하실 수 있으며, 주요 내용은 다음과 같습니다. (Gem 상세 내용 추가 예정)"
    elif any(keyword in user_input for keyword in ["수강", "학점", "신청"]):
        return "수강 신청 및 학점 인정에 대한 질문으로 이해했습니다. 관련 규정은 'GNU 학사 규정'을 참고해 주시고, 더 자세한 내용은 문의해 주시면 안내해 드리겠습니다."
    else:
        return "질문 감사합니다. 현재 저는 '교육과정' 및 '규정' 관련 질문에 최적화되어 있습니다. 다른 질문이 있으시면 다시 입력해 주세요."
# ----------------------------------------------------


# --- 4. 이전 채팅 기록 표시 ---
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# -------------------------------

# --- 5. 사용자 입력 처리 ---
if prompt := st.chat_input("질문을 입력하세요..."):
    # 1. 사용자 메시지를 기록에 추가하고 화면에 표시
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. 어시스턴트(Gem) 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("규정집을 검색하고 있습니다..."):
            time.sleep(1) # 답변 생성 대기 시간 시뮬레이션
            response = get_gem_response(prompt)
        
        # 응답을 스트리밍하여 표시 (사용자 경험 개선)
        full_response = ""
        placeholder = st.empty()
        for chunk in response.split():
            full_response += chunk + " "
            placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        placeholder.markdown(full_response)
        
    # 3. 어시스턴트 메시지를 기록에 추가
    st.session_state["messages"].append({"role": "assistant", "content": response})
# ----------------------------
