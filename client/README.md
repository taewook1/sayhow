# 🗣️ Sayhow – 말하기 센스 훈련 커뮤니티

고민 상황에서 어떤 말을 해야 할지 모를 때,  
센스 있는 답변을 참고하고 직접 훈련하며,  
AI 피드백까지 받아보는 실전 말하기 훈련 플랫폼.

---

## ✨ 주요 기능

- 고민 상황을 질문 형태로 등록
- 다양한 사용자들의 자유로운 답변
- 공감/센스/직설 투표 기능
- 내가 쓴 답변에 대한 **AI 피드백 제공**
- 마이페이지에서 누적 피드백 리포트 확인
- 베스트 답변 랭킹/인기 질문 구경
- 관리자 페이지로 신고/차단 관리

---

## 🛠️ 기술 스택

| 영역 | 기술 |
|------|------|
| **Frontend** | React, TypeScript, Vite, Zustand, TailwindCSS, React Router |
| **Backend** | FastAPI, PostgreSQL, SQLAlchemy |
| **Auth** | JWT 기반 로그인 (닉네임만 설정) |
| **AI 분석** | OpenAI GPT 연동 또는 감정 룰 기반 톤 분석 |
| **배포** | Vercel (프론트), EC2 + Docker + Nginx (백엔드) |

---

## 🧭 페이지 구성

| 경로 | 설명 |
|------|------|
| `/` | 메인 페이지 – 최근 질문 / 인기 답변 미리보기 |
| `/write` | 질문 작성 페이지 |
| `/question/:id` | 질문 상세 + 답변 목록 |
| `/answer/:questionId` | 답변 작성 페이지 |
| `/mypage` | 내가 쓴 질문/답변 + 피드백 로그 |
| `/feedback/:answerId` | 답변별 AI 피드백 확인 |
| `/rankings` | 베스트 답변 랭킹 |
| `/admin` | (선택) 관리자 페이지 |

---

## 📁 프로젝트 구조

```
sayhow/
├── client/       # React + Vite 프론트엔드
├── server/       # FastAPI 백엔드
├── docs/         # 기획/설계 문서
├── .gitignore
├── README.md
└── ...
```

---

## 🚀 실행 방법

### 프론트엔드 (client)

```bash
cd client
npm install
npm run dev
```

### 백엔드 (server)

```bash
# 가상환경 세팅 권장
cd server
uvicorn main:app --reload
```

---

## 🙌 협업 및 컨트리뷰션

- 기획/설계 문서는 `docs/` 폴더 참조
- 피드백, 기능 제안, PR 대환영 🙌

---

## 📝 라이선스

본 프로젝트는 MIT 라이선스를 따릅니다.