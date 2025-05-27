import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "/api", // 프록시 설정으로 백엔드에 연결됨
  headers: {
    "Content-Type": "application/json",
  },
});

// 토큰 자동 포함 (옵션)
axiosInstance.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default axiosInstance;
