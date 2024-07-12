import { createApp } from "vue";
import "element-plus/theme-chalk/dark/css-vars.css";
import App from "@/App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
//@ts-ignore忽略当前文件ts类型的检测否则有红色提示(打包会失败)
import zhCn from "element-plus/dist/locale/zh-cn.mjs";

import "@/styles/index.scss";
import router from "./router";
import gloalComponent from "@/components";
import pinia from "./store";

let app = createApp(App);
app.use(pinia);
app.use(gloalComponent);
app.use(ElementPlus, {
  locale: zhCn,
});
app.use(router), app.mount("#app");
