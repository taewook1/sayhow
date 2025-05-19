import React, { useState } from "react";
// import axios from "axios"; // axiosInstance 써도 됨

function SignupPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!username.trim()) return alert("아이디를 입력해주세요");
    if (username.length < 4) return alert("아이디는 4자 이상이어야 합니다");
    if (password.length < 6) return alert("비밀번호는 6자 이상이어야 합니다");
    if (password !== confirmPassword)
      return alert("비밀번호가 일치하지 않습니다");

    try {
      const res = await axios.post("/api/signup", { username, password });
      alert("회원가입이 완료되었습니다!");
      window.location.href = "/login"; // 또는 useNavigate
    } catch (err: any) {
      alert(err.response?.data?.message || "회원가입 실패");
    }
  };

  return (
    <div className="form-container">
      <h1 className="form-title">회원가입</h1>
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
        <input
          type="password"
          placeholder="비밀번호 확인"
          className="input"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
        <button type="submit" className="btn-primary">
          회원가입
        </button>
      </form>
    </div>
  );
}

export default SignupPage;
