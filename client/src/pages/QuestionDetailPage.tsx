import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axiosInstance from "../lib/axiosInstance";

interface Question {
  id: number;
  title: string;
  content: string;
  created_at: string;
  user: {
    username: string;
  };
}

const QuestionDetailPage = () => {
  const { id } = useParams(); // URL의 question ID
  const [question, setQuestion] = useState<Question | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuestion = async () => {
      try {
        const res = await axiosInstance.get(`/questions/${id}`);
        setQuestion(res.data);
      } catch (err) {
        console.error("질문 조회 실패:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchQuestion();
  }, [id]);

  if (loading) return <p>불러오는 중...</p>;
  if (!question) return <p>존재하지 않는 질문입니다.</p>;

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold mb-2">{question.title}</h1>
      <p className="text-gray-600 mb-4">{question.content}</p>
      <p className="text-sm text-right text-gray-400">
        by {question.user.username} ·{" "}
        {new Date(question.created_at).toLocaleString()}
      </p>
    </div>
  );
};

export default QuestionDetailPage;
