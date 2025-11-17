from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

st.title("인공지능 시인")

# 사이드바에서 API 키 입력
with st.sidebar:
    st.header("설정")
    # API 키를 받아옵니다.
    api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password", help="sk-로 시작하는 OpenAI API 키를 입력하세요.")
    
    if api_key:
        st.success("API 키가 입력되었습니다.")
    else:
        st.warning("API 키를 입력해주세요.")

# 메인 화면
content = st.text_input("시의 주제를 입력하세요.")

if st.button("시 작성 요청하기"):
    if not api_key:
        st.error("먼저 사이드바에서 OpenAI API 키를 입력해주세요.")
    elif not content:
        st.error("시의 주제를 입력해주세요.")
    else:
        try:
            # ⭐ CRITICAL FIX: The os.environ is no longer strictly necessary 
            # for the model to work, but we keep it for general LangChain conventions. 
            # The key is passed directly below.
            # However, we must ensure we are using the correct LangChain method.
            
            with st.spinner("시를 작성하는 중입니다..."):
                # 환경 변수 설정 (LangChain이 아닌 다른 라이브러리가 사용할 경우를 대비)
                os.environ['OPENAI_API_KEY'] = api_key 
                
                # ⭐ CRITICAL FIX: Pass the API key directly to the model
                # init_chat_model or ChatOpenAI will now use this passed key.
                # In modern LangChain, init_chat_model passes extra kwargs 
                # to the underlying provider (ChatOpenAI in this case).
                llm = init_chat_model(
                    "gpt-4o-mini", 
                    model_provider="openai",
                    # The key is passed directly to the underlying model class (ChatOpenAI)
                    api_key=api_key 
                )
                
                # 프롬프트 템플릿 생성
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are a helpful assistant that writes beautiful Korean poetry."),
                    ("user", "{input}")
                ])
                
                # 체인 생성
                output_parser = StrOutputParser()
                chain = prompt | llm | output_parser
                
                # 시 생성 요청
                result = chain.invoke({"input": f"{content}에 대한 아름다운 시를 써 줘"})
                
                # 결과 출력
                st.markdown("### 생성된 시")
                st.markdown(f"**주제: {content}**")
                st.markdown("---")
                st.write(result)
                
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")
            if "api" in str(e).lower() or "key" in str(e).lower() or "authentication" in str(e).lower():
                st.error("API 키가 올바르지 않거나 권한이 없습니다. API 키를 확인해주세요.")