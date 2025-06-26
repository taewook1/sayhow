import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import type { RootState } from "../store";
import { logout } from "../store/userSlice";

function Header() {
  const { username } = useSelector((state: RootState) => state.user);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleAskClick = () => {
    if (!username) {
      navigate("/login");
    } else {
      navigate("/write"); // 질문 작성 폼 페이지
    }
  };

  const handleLogout = () => {
    dispatch(logout());
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <header className="flex flex-col sm:flex-row justify-between items-center px-6 py-4 border-b gap-2">
      <h1 className="text-lg font-bold">
        <Link to="/">sayhow</Link>
      </h1>
      <div className="flex gap-3 flex-wrap justify-center sm:justify-end">
        {username ? (
          <>
            <button onClick={handleAskClick}>질문하기</button>
            <Link to="/mypage">마이페이지</Link>
            <button onClick={handleLogout}>로그아웃</button>
          </>
        ) : (
          <>
            <button onClick={handleAskClick}>질문하기</button>
            <Link to="/login">로그인</Link>
            <Link to="/signup">회원가입</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default Header;
