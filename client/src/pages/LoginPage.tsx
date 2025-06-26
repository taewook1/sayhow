import React, { useState } from "react";
import axios from "../lib/axiosInstance";
import { isAxiosError } from "axios";
import { useNavigate } from "react-router-dom";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!username.trim()) return alert("아이디를 입력해주세요");
    if (!password.trim()) return alert("비밀번호를 입력해주세요");

    try {
      const res = await axios.post("/login", { username, password });
      localStorage.setItem("token", res.data.token);
      alert("로그인 성공!");
      navigate("/");
    } catch (err: unknown) {
      if (isAxiosError(err)) {
        alert(err.response?.data?.message || "로그인 실패");
      } else {
        alert("알 수 없는 오류가 발생했습니다.");
      }
    }
  };

  return (
    <div className="form-container">
      <h1 className="form-title">로그인</h1>
      <form onSubmit={handleSubmit} className="form-group">
        <input
          type="text"
          placeholder="아이디"
          className="input"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="비밀번호"
          className="input"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit" className="btn-primary">
          로그인
        </button>
      </form>
    </div>
  );
}

export default LoginPage;
