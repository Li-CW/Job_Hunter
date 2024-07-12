//小仓库:layout组件相关配置仓库
import { defineStore } from "pinia";
// import { watch } from 'vue';
const useLayOutSettingStore = defineStore("SettingStore", {
  state: () => {
    return {
      theme: "default", //用户控制菜单折叠还是收起控制
    };
  },
});


export default useLayOutSettingStore;
