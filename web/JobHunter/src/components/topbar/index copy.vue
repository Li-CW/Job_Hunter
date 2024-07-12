<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" background-color="#545c64"
    text-color="#fff" active-text-color="#ffd04b" :ellipsis="false" @select="handleSelect">
    <div style="margin-left: 30px">
      <el-menu-item style="height: '50px'; font-family: 'Satisfy', cursive">JH</el-menu-item>
    </div>
    <el-menu-item index="0"> 真题 </el-menu-item>
    <el-menu-item index="1"> 面经 </el-menu-item>
    <el-sub-menu class="el-submenu__wrap" index="2">
      <template #title>分享</template>
      <el-menu-item index="2-1">真题</el-menu-item>
      <el-menu-item index="2-2">面经</el-menu-item>
    </el-sub-menu>
    <div class="el-menu-right" style="margin-right: 30px; overflow: hidden">
      <el-menu-item @click="showLoginDialog = true" v-if="!userStore.is_login"> 登录 </el-menu-item>
      <el-sub-menu index="99" v-if="userStore.is_login">
        <template #title><el-avatar :src="userStore.photo" /> </template>
        <el-menu-item @click="handleLogout"> 退出</el-menu-item>
      </el-sub-menu>
    </div>
  </el-menu>
  <el-dialog @keyup.enter.native="handleEnter" v-model="showLoginDialog" title="JobHunter" style="
      color: #eb9316;
      font-size: larger;
      height: 300px;
      width: 400px;
      border-radius: 15px;
      box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5);
      text-align: center;
      font-family: 'Satisfy', cursive;
    ">
    <el-tabs v-model="activeTab" style="font-family: 'Microsoft YaHei', sans-serif">
      <el-tab-pane label="登录" name="login">
        <el-form>
          <el-form-item>
            <el-input v-model="loginForm.username" placeholder="用户名" autocomplete="username"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input autocomplete="current-password" type="password" v-model="loginForm.password"
              placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" style="width: 400px" @click="handleLogin">登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="注册" name="register">
        <el-form>
          <el-form-item>
            <el-input v-model="registerForm.username" placeholder="用户名" prop="username"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input type="password" v-model="registerForm.password" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item prop="confirmPassword">
            <el-input type="password" v-model="registerForm.confirmPassword" placeholder="确认密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" style="width: 400px" @click="handleRegister">注册</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </el-dialog>
</template>

<script lang="ts" setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { ElMessage } from 'element-plus';
import useUserStore from '@/store/models/user';
const userStore = useUserStore();
const route = useRoute();
const activeIndex = ref();
const router = useRouter();
const showLoginDialog = ref(false);
const activeTab = ref('login');
const loginForm = reactive({
  username: '',
  password: '',
});
const registerForm = reactive({
  username: '',
  password: '',
  confirmPassword: '',
});
const handleSelect = (value: string) => {
  if (value == '0') router.push('/question');
  if (value == '1') router.push('/interview');
  if (value == '2-1') {
    if (!userStore.is_login) {
      showLoginDialog.value = true;
      return;
    }
    router.push('/question/add');
  }
  if (value == '2-2') {
    if (!userStore.is_login) {
      ElMessage({
        message: '请先登录',
        type: 'info',
        offset: 100,
      });
      return;
    }
    router.push('/interview/add');
  }
};
onMounted(() => {
  if (route.path.includes('question')) {
    activeIndex.value = '0';
  }
  if (route.path.includes('interview')) {
    activeIndex.value = '1';
  }
  if (route.path.includes('add')) {
    activeIndex.value = '2-1';
  }
});
const handleEnter = async () => {
  if (activeTab.value === 'login') {
    await handleLogin();
  } else {
    await handleRegister();
  }
};
const handleLogin = async () => {
  if (loginForm.username == '') {
    ElMessage({
      message: '请输入用户名',
      type: 'error',
      offset: 100,
    });
    return;
  }
  if (loginForm.password == '') {
    ElMessage({
      message: '请输入密码',
      type: 'error',
      offset: 100,
    });
    return;
  }
  const result = await userStore.login(loginForm);
  ElMessage({
    message: result,
    type: !userStore.is_login ? 'error' : 'success',
    offset: 100,
  });
  if (userStore.is_login) showLoginDialog.value = false;
};
const handleRegister = async () => {
  if (registerForm.username == '' || registerForm.password == '') {
    ElMessage({
      message: '用户名或密码不能为空',
      type: 'error',
      offset: 100,
    });
    return;
  }
  if (registerForm.password !== registerForm.confirmPassword) {
    ElMessage({
      message: '两次密码不同',
      type: 'error',
      offset: 100,
    });
    return;
  }

  const result = await userStore.register(registerForm);
  ElMessage({
    message: result,
    type: userStore.is_login ? 'success' : 'info',
    offset: 100,
  });
  if (userStore.is_login) showLoginDialog.value = false;
};
const handleLogout = () => {
  userStore.logout();
  ElMessage({
    message: '退出成功',
    type: 'success',
    offset: 100,
  });
};
</script>

<style scoped>
.el-menu-demo {
  height: 50px;
  display: flex;
  justify-content: space-between;
  position: fixed;
  top: 0px;
  width: 100vw;
  z-index: 99999;
  /* overflow: hidden; */
  border: none !important;
}

.el-menu-right {
  margin-left: auto;
  display: flex;
  overflow: hidden;
  padding-right: 30px;
}

@media (max-width: 425px) {
  .el-submenu__wrap {
    display: none;
  }
}

.el-sub-menu__title {
  height: 50px !important;
}
</style>
