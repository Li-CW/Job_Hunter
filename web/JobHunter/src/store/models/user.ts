//小仓库:layout组件相关配置仓库
import { defineStore } from 'pinia';
import { login, register, refreshToken } from '@/api/user';

const useUserStore = defineStore('UserStore', {
  state: () => {
    return {
      userId: -1,
      photo: '',
      refresh: '',
      token: '',
      is_login: false,
      refreshTokenInterval: null as number | null, // 用于保存定时器ID
    };
  },
  actions: {
    async login(loginForm: any) {
      try {
        let userInfo = await login(loginForm);
        this.userId = userInfo.userId;
        this.photo = userInfo.photo;
        this.refresh = userInfo.refresh;
        this.token = userInfo.token;
        this.is_login = true;
        this.startTokenRefresh();
      } catch (err) {
        this.is_login = false;
        return '用户名或密码错误！';
      }

      return '登陆成功';
    },
    async logout() {
      this.userId = -1;
      this.photo = '';
      this.refresh = '';
      this.token = '';
      this.is_login = false;
      if (this.refreshTokenInterval !== null) clearInterval(this.refreshTokenInterval);
    },
    async register(registerForm: any) {
      try {
        let res: any = await register(registerForm);
        if (res.result == '注册成功') await this.login(registerForm);
        return res.result;
      } catch (err) {
        this.is_login = false;
        return '注册失败！';
      }
    },
    async startTokenRefresh() {
      if (this.refreshTokenInterval !== null) {
        clearInterval(this.refreshTokenInterval);
      }
      try {
        const newToken: any = await refreshToken({ refresh: this.refresh });
        this.token = newToken.access;
      } catch (error) {
        this.logout();
      }
      this.refreshTokenInterval = setInterval(async () => {
        try {
          const newToken: any = await refreshToken({ refresh: this.refresh });
          this.token = newToken.access;
        } catch (error) {
          this.logout();
        }
      }, 100 * 60 * 1000);
    },
    loadFromStorage() {
      if (this.is_login) {
        this.startTokenRefresh();
      }
    },
  },

  persist: {
    key: 'piniaStore', //存储名称
    storage: localStorage,
    afterRestore: (context) => {
      if (context.store.is_login) context.store.loadFromStorage();
    },
  },
});

export default useUserStore;
