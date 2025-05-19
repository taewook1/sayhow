export default function MyPage() {
  return (
    <div className="py-10 px-4 max-w-3xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">👤 마이페이지</h2>

      <div className="mb-8">
        <h3 className="text-lg font-semibold mb-2">내가 쓴 질문</h3>
        <div className="bg-gray-100 p-4 rounded">질문 목록 예정</div>
      </div>

      <div className="mb-8">
        <h3 className="text-lg font-semibold mb-2">내가 쓴 답변</h3>
        <div className="bg-gray-100 p-4 rounded">답변 목록 예정</div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-2">AI 피드백 리포트</h3>
        <div className="bg-gray-100 p-4 rounded">피드백 로그 예정</div>
      </div>
    </div>
  );
}
