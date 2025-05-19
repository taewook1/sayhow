export default function HomePage() {
  return (
    <div className="flex flex-col gap-8 py-10 px-4 max-w-3xl mx-auto">
      <section>
        <h2 className="text-2xl font-bold mb-4">🆕 최근 등록된 질문</h2>
        <div className="bg-white p-4 rounded shadow text-gray-700">
          (여기에 최신 질문 카드들이 들어올 예정)
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-bold mb-4">🔥 인기 답변 모음</h2>
        <div className="bg-white p-4 rounded shadow text-gray-700">
          (여기에 베스트 답변 요약 리스트 들어올 예정)
        </div>
      </section>
    </div>
  );
}
