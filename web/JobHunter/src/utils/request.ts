import axios from 'axios';
import useUserStore from '@/store/models/user';

// 创建 axios 实例
const request = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API, // 基础路径上会携带 /api
  timeout: 5000, // 超时的时间设置
});

// 请求拦截器
request.interceptors.request.use(
  (config) => {
    const userStore = useUserStore();
    if (userStore.token) {
      config.headers.Authorization = `Bearer ${userStore.token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
request.interceptors.response.use(
  (response) => {
    return response.data;
  },
  async (error) => {
    const userStore = useUserStore();
    userStore.logout();
    return Promise.reject(error);
  }
);

export default request;
