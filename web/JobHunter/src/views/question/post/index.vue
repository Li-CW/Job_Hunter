<template>
  <Toptbar></Toptbar>
  <div class="layout_container">
    <el-form :model="questionForm" :rules="rules" label-width="120px" ref="questionFormRef">
      <el-form-item label="题目" prop="title">
        <el-input v-model="questionForm.title" autocomplete="off" placeholder="填写题目"></el-input>
      </el-form-item>
      <el-form-item label="科目" prop="subject">
        <el-select v-model="questionForm.subject" placeholder="请选择科目">
          <el-option v-for="item in categoryStore.subject" :key="item.id" :label="item.name" :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="公司" prop="company">
        <el-select v-model="questionForm.company" placeholder="请选择公司">
          <el-option v-for="item in categoryStore.company" :key="item.id" :label="item.name" :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="工作类型" prop="job">
        <el-select v-model="questionForm.job" placeholder="工作类型">
          <el-option v-for="item in categoryStore.job" :key="item.id" :label="item.name" :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="答案" prop="answer">
        <MdEditor v-model="questionForm.answer" previewTheme="cyanosis" :theme="theme" codeTheme="atom"
          :codeFoldable="false" style="height: 50vh" placeholder="Markdown 格式填写" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { createQuestion } from '@/api/question';
import { MdEditor } from 'md-editor-v3';
import { ref, reactive, onMounted, onUnmounted } from 'vue';
import Toptbar from '@/components/topbar/index.vue';
import 'md-editor-v3/lib/style.css';
import { ElMessage } from 'element-plus';
import useCategoryStore from '@/store/models/category';
import { useRouter } from 'vue-router';
import useUserStore from '@/store/models/user';
const userStore = useUserStore();
const categoryStore = useCategoryStore();
const router = useRouter();
let theme: any = ref('default');
const bc = new BroadcastChannel('my-channel');

onMounted(async () => {
  document.title = '分享真题';
  bc.onmessage = (event) => {
    if (event.data.theme) theme.value = 'dark';
    else theme.value = 'light';
  };
});

onUnmounted(() => {
  bc.close();
});

let questionForm = reactive({
  title: '',
  answer: '',
  subject: '',
  company: '',
  job: '',
  badge: '',
});

const rules = {
  title: [{ required: true, message: '请填写题目', trigger: 'blur' }],
  subject: [{ required: true, message: '请选择科目', trigger: 'blur' }],
  company: [{ required: true, message: '请选择公司', trigger: 'blur' }],
  job: [{ required: true, message: '请选择工作类型', trigger: 'blur' }],
  answer: [{ required: true, message: '请填写答案', trigger: 'blur' }],
};

let submitForm = async () => {
  if (!userStore.is_login) {
    ElMessage({
      message: '请先登录',
      type: 'info',
      offset: 100,
    });
    return;
  }
  try {
    await questionFormRef.value.validate();
    questionForm.badge = ""
    let foundCompany: any = categoryStore.company.find((obj: any) => obj.id === questionForm.company);
    questionForm.badge = questionForm.badge + " " + foundCompany.name
    let foundJob: any = categoryStore.job.find((obj: any) => obj.id === questionForm.job);
    questionForm.badge = questionForm.badge + " " + foundJob.name
    let foundSubject: any = categoryStore.subject.find((obj: any) => obj.id === questionForm.subject);
    questionForm.badge = questionForm.badge + " " + foundSubject.name
    let res = await createQuestion(questionForm);
    window.open('/question/' + res.id, '_blank');
  } catch (error: any) {
    ElMessage({
      message: '请检查是否漏填必填项目',
      type: 'error',
      offset: 100,
    });
  }
};

let resetForm = () => {
  questionFormRef.value.resetFields();
};

const questionFormRef = ref();
</script>

<style lang="scss" scoped>
.layout_container {
  width: 90vw;
  height: 100vh;
  margin: 0 auto;
  margin-top: 60px;
}
</style>
