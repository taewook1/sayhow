import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="border-b bg-white shadow-sm">
      <div className="max-w-3xl mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="text-xl font-bold text-gray-900">
          Sayhow
        </Link>

        <div className="flex items-center space-x-6 text-sm text-gray-700">
          <nav className="space-x-4 hidden sm:block">
            <Link to="/write" className="hover:underline">
              질문하기
            </Link>
            <Link to="/mypage" className="hover:underline">
              마이페이지
            </Link>
          </nav>

          <div className="space-x-2">
            <Link
              to="/login"
              className="text-gray-600 hover:text-gray-900 hover:underline"
            >
              로그인
            </Link>
            <span className="text-gray-400">|</span>
            <Link
              to="/signup"
              className="text-gray-600 hover:text-gray-900 hover:underline"
            >
              회원가입
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;
