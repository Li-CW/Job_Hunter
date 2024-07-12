//小仓库:layout组件相关配置仓库
import { defineStore } from "pinia";
import { company } from "@/api/company";
import { subject } from "@/api/question";
import { job } from "@/api/job";
// import { watch } from 'vue';
const useCategoryStore = defineStore("CategoryStore", {
  state: () => {
    return {
      flag: false,
      job: [] as any,
      company: [] as any,
      subject: [] as any,
    };
  },
  actions: {
    async get_category() {
      this.company = await company();
      this.subject = await subject();
      this.job = await job();
      this.flag = true;
    },
  },
});

export default useCategoryStore;
