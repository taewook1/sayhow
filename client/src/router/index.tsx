import { createBrowserRouter } from "react-router-dom";
import AppLayout from "../layouts/AppLayout";
import HomePage from "../pages/HomePage";
import WritePage from "../pages/WritePage";
import QuestionDetailPage from "../pages/QuestionDetailPage";
import AnswerPage from "../pages/AnswerPage";
import MyPage from "../pages/MyPage";
import FeedbackPage from "../pages/FeedbackPage";
import RankingPage from "../pages/RankingPage";
import AdminPage from "../pages/AdminPage";
import LoginPage from "../pages/LoginPage";
import SignupPage from "../pages/SignupPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      { index: true, element: <HomePage /> },
      { path: "write", element: <WritePage /> },
      { path: "question/:id", element: <QuestionDetailPage /> },
      { path: "answer/:questionId", element: <AnswerPage /> },
      { path: "mypage", element: <MyPage /> },
      { path: "feedback/:answerId", element: <FeedbackPage /> },
      { path: "rankings", element: <RankingPage /> },
      { path: "admin", element: <AdminPage /> },
      { path: "login", element: <LoginPage /> },
      { path: "signup", element: <SignupPage /> },
    ],
  },
]);

export default router;
