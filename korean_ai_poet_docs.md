# 인공지능 시인 🎭✨

LangChain과 OpenAI API를 활용하여 사용자가 입력한 주제로 아름다운 한국어 시를 자동 생성하는 Streamlit 웹 애플리케이션입니다.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.0.5-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-2.7.2-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-red.svg)

## 📌 주요 기능

- 🔑 **안전한 API 키 관리**: 사이드바에서 OpenAI API 키를 안전하게 입력
- ✍️ **AI 시 생성**: 사용자가 입력한 주제를 기반으로 한국어 시 자동 생성
- 🎨 **직관적인 UI**: Streamlit을 활용한 간단하고 사용하기 쉬운 인터페이스
- ⚡ **빠른 응답**: GPT-4o-mini 모델로 신속한 시 생성
- 🛡️ **강력한 오류 처리**: API 키 검증 및 상세한 오류 메시지 제공

## 🚀 빠른 시작

### 사전 요구사항

- Python 3.8 이상
- OpenAI API 키 ([여기서 발급](https://platform.openai.com/api-keys))
- 인터넷 연결

### 설치

1. **저장소 클론**
```bash
git clone https://github.com/your-username/ai-poet.git
cd ai-poet
```

2. **가상환경 생성 (권장)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **필수 패키지 설치**
```bash
pip install -r requirements.txt
```

### 실행

```bash
streamlit run app.py
```

브라우저에서 자동으로 `http://localhost:8501`로 애플리케이션이 열립니다.

## 💡 사용 방법

### 1단계: API 키 입력 🔑
- 애플리케이션 실행 후 **왼쪽 사이드바**를 확인하세요
- "OpenAI API Key를 입력하세요" 필드에 API 키를 입력합니다
- API 키는 `sk-`로 시작하며, 비밀번호 형식으로 보호됩니다
- 입력 완료 시 "API 키가 입력되었습니다" 메시지가 표시됩니다

### 2단계: 시 주제 입력 ✨
메인 화면의 텍스트 입력 필드에 원하는 시의 주제를 입력합니다.

**주제 예시:**
- 봄날
- 그리움
- 별이 빛나는 밤
- 어머니
- 첫사랑
- 가을 단풍

### 3단계: 시 생성 📝
- **"시 작성 요청하기"** 버튼을 클릭합니다
- AI가 시를 작성하는 동안 로딩 스피너가 표시됩니다
- 몇 초 후 생성된 아름다운 한국어 시를 확인하세요!

## 🛠 기술 스택

### 핵심 프레임워크
| 라이브러리 | 버전 | 용도 |
|-----------|------|------|
| **Streamlit** | latest | 웹 애플리케이션 UI 프레임워크 |
| **LangChain** | 1.0.5 | LLM 체인 구성 및 관리 |
| **langchain-core** | 1.0.4 | LangChain 핵심 컴포넌트 |
| **langchain-openai** | 1.0.2 | OpenAI 통합 |
| **OpenAI** | 2.7.2 | GPT-4o-mini 모델 API |

### 주요 의존성
- **pydantic** (2.12.4): 데이터 검증 및 타입 힌팅
- **httpx** (0.28.1): 비동기 HTTP 클라이언트
- **tiktoken** (0.12.0): OpenAI 토큰 계산
- **python-dotenv** (1.2.1): 환경 변수 관리
- **tenacity** (9.1.2): 재시도 로직

전체 의존성 목록은 `requirements.txt`를 참고하세요.

## 📂 프로젝트 구조

```
ai-poet/
├── app.py              # 메인 애플리케이션 파일
├── requirements.txt    # 의존성 패키지 목록 (40+ 패키지)
└── README.md          # 프로젝트 문서 (이 파일)
```

## 🔧 핵심 코드 구조

### 1. API 키 입력 및 검증
```python
with st.sidebar:
    st.header("설정")
    api_key = st.text_input(
        "OpenAI API Key를 입력하세요:", 
        type="password",
        help="sk-로 시작하는 OpenAI API 키를 입력하세요."
    )
```

### 2. LLM 모델 초기화
```python
# API 키를 직접 전달하여 모델 초기화
llm = init_chat_model(
    "gpt-4o-mini", 
    model_provider="openai",
    api_key=api_key  # ⭐ API 키 직접 전달
)
```

### 3. 프롬프트 템플릿 설정
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that writes beautiful Korean poetry."),
    ("user", "{input}")
])
```

### 4. LangChain 체인 구성 및 실행
```python
# 체인 구성: 프롬프트 → LLM → 출력 파서
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# 시 생성 요청
result = chain.invoke({
    "input": f"{content}에 대한 아름다운 시를 써 줘"
})
```

## 🔒 보안 및 안전성

### 구현된 보안 기능
- ✅ **API 키 보호**: 비밀번호 타입 입력으로 화면에 표시되지 않음
- ✅ **세션 관리**: 세션별로 API 키를 관리하여 보안 유지
- ✅ **입력 검증**: API 키 및 주제 입력 여부 확인
- ✅ **오류 처리**: 상세한 오류 메시지와 해결 가이드 제공

### 오류 처리 예시
```python
try:
    # 시 생성 로직
    pass
except Exception as e:
    st.error(f"오류가 발생했습니다: {str(e)}")
    if "api" in str(e).lower() or "key" in str(e).lower():
        st.error("API 키가 올바르지 않거나 권한이 없습니다.")
```

## ❗ 문제 해결

### 1. API 키 관련 오류

**증상:**
```
오류가 발생했습니다: Authentication error
API 키가 올바르지 않거나 권한이 없습니다.
```

**해결 방법:**
- API 키가 `sk-`로 시작하는지 확인
- [OpenAI 플랫폼](https://platform.openai.com/api-keys)에서 API 키 상태 확인
- API 키를 복사할 때 공백이 포함되지 않았는지 확인
- [사용량 및 크레딧 잔액 확인](https://platform.openai.com/usage)

### 2. 모델 접근 오류

**증상:**
```
모델에 접근할 수 없습니다
```

**해결 방법:**
- GPT-4o-mini 모델에 대한 접근 권한 확인
- 필요시 `app.py`에서 다른 모델로 변경:
```python
llm = init_chat_model(
    "gpt-3.5-turbo",  # 또는 "gpt-4"
    model_provider="openai",
    api_key=api_key
)
```

### 3. 패키지 설치 오류

**증상:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**해결 방법:**
```bash
# pip 업그레이드
pip install --upgrade pip

# 캐시 없이 재설치
pip install -r requirements.txt --no-cache-dir

# 특정 패키지만 재설치
pip install langchain langchain-openai streamlit
```

### 4. Streamlit 실행 오류

**증상:**
```
streamlit: command not found
```

**해결 방법:**
```bash
# Streamlit 재설치
pip install streamlit

# 또는 Python 모듈로 직접 실행
python -m streamlit run app.py
```

## 🌟 주요 특징

| 특징 | 설명 |
|------|------|
| 🎯 **간편한 사용** | 복잡한 설정 없이 API 키만 입력하면 바로 시작 |
| 🔐 **보안 강화** | API 키를 안전하게 관리하고 세션별로 격리 |
| ⚡ **빠른 생성** | GPT-4o-mini 모델로 몇 초 만에 시 생성 |
| 🎨 **깔끔한 UI** | Markdown 형식으로 생성된 시를 아름답게 표시 |
| 🛡️ **오류 처리** | 상세한 오류 메시지와 해결 가이드 제공 |
| 💬 **한국어 특화** | 한국어 시 작성에 최적화된 프롬프트 템플릿 |

## 📊 성능 및 제한사항

### 성능
- **응답 시간**: 평균 3-5초 (네트워크 상태에 따라 다름)
- **토큰 사용량**: 주제 및 생성된 시의 길이에 따라 100-500 토큰

### 제한사항
- OpenAI API 사용량 제한에 따라 요청 수 제한 가능
- 인터넷 연결 필요
- 매우 긴 시나 복잡한 형식은 추가 프롬프트 엔지니어링 필요

## 📈 향후 개선 사항

### 기능 추가
- [ ] 시의 스타일 선택 (현대시, 고전시, 자유시, 정형시)
- [ ] 시의 길이 조절 옵션 (단시, 장시)
- [ ] 생성된 시 저장 및 다운로드 기능 (TXT, PDF)
- [ ] 여러 시를 생성하여 비교 선택
- [ ] 시 히스토리 기능

### UI/UX 개선
- [ ] 다크 모드 지원
- [ ] 시 스타일 프리셋 (감성적, 철학적, 서정적 등)
- [ ] 실시간 피드백 및 평가 기능
- [ ] 시 공유 기능 (SNS 연동)

### 기술적 개선
- [ ] 다양한 LLM 모델 선택 옵션 (Claude, Gemini 등)
- [ ] 캐싱을 통한 응답 속도 개선
- [ ] 배치 처리로 여러 시 동시 생성
- [ ] 사용자 피드백 학습 시스템

## 🧪 테스트

### 기본 테스트 시나리오

1. **정상 동작 테스트**
   - API 키 입력 → 주제 입력 → 시 생성 확인

2. **오류 처리 테스트**
   - API 키 없이 시도 → 오류 메시지 확인
   - 주제 없이 시도 → 오류 메시지 확인
   - 잘못된 API 키 → 인증 오류 확인

3. **다양한 주제 테스트**
   ```
   테스트 주제: 봄, 사랑, 이별, 희망, 자연, 우정
   ```

## 📝 라이선스

이 프로젝트는 교육 및 학습 목적으로 제작되었습니다.

## 🤝 기여하기

프로젝트 개선에 기여하고 싶으시다면:

1. 저장소를 Fork 합니다
2. 새로운 기능 브랜치를 생성합니다
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 변경사항을 커밋합니다
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. 브랜치에 Push 합니다
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Pull Request를 생성합니다

### 기여 가이드라인
- 코드 스타일: PEP 8 준수
- 커밋 메시지: Conventional Commits 형식
- 테스트: 새로운 기능에는 테스트 코드 포함

## 📚 참고 자료

### 공식 문서
- [LangChain 공식 문서](https://python.langchain.com/)
- [OpenAI API 문서](https://platform.openai.com/docs)
- [Streamlit 공식 문서](https://docs.streamlit.io/)

### 유용한 링크
- [LangChain 프롬프트 가이드](https://python.langchain.com/docs/modules/model_io/prompts/)
- [OpenAI 모델 가이드](https://platform.openai.com/docs/models)
- [Streamlit 갤러리](https://streamlit.io/gallery)

## 💬 지원 및 문의

### 문제 신고
프로젝트 사용 중 문제가 발생하면 [Issues](https://github.com/your-username/ai-poet/issues)에 등록해주세요.

### 이슈 등록 시 포함 정보
- 운영체제 및 Python 버전
- 오류 메시지 전문
- 재현 가능한 단계
- 스크린샷 (선택사항)

## 👨‍💻 개발자

이 프로젝트는 LangChain과 OpenAI API를 학습하기 위해 제작되었습니다.

---

<div align="center">

### ⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요! ⭐

**Made with ❤️ using LangChain & OpenAI**

</div>