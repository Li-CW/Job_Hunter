<template>
  <Toptbar></Toptbar>
  <div class="layout_container">
    <el-form :model="interviewForm" :rules="rules" label-width="120px" ref="interviewFormRef">
      <el-form-item label="题目" prop="title">
        <el-input
          v-model="interviewForm.title"
          autocomplete="off"
          placeholder="填写题目"
        ></el-input>
      </el-form-item>
      <el-form-item label="公司" prop="company">
        <el-select v-model="interviewForm.company" placeholder="请选择公司">
          <el-option
            v-for="item in categoryStore.company"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="工作类型" prop="job">
        <el-select v-model="interviewForm.job" placeholder="工作类型">
          <el-option
            v-for="item in categoryStore.job"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="面试类型" prop="classification">
        <el-select v-model="interviewForm.classification" placeholder="面试类型">
          <el-option label="实习" value="1"> </el-option>
          <el-option label="校招" value="2"> </el-option>
          <el-option label="社招" value="3"> </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="面经内容" prop="body">
        <MdEditor
          v-model="interviewForm.body"
          previewTheme="cyanosis"
          :theme="theme"
          codeTheme="atom"
          :codeFoldable="false"
          style="height: 50vh"
          placeholder="Markdown 格式填写"
        />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { createInterview } from '@/api/interview';
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
  document.title = '分享面经';
  bc.onmessage = (event) => {
    if (event.data.theme) theme.value = 'dark';
    else theme.value = 'light';
  };
  // if (!categoryStore.flag) {
  //   await categoryStore.get_category()
  // }
});

onUnmounted(() => {
  bc.close();
});

let interviewForm = reactive({
  title: '',
  company: '',
  job: '',
  classification: '',
  body: '',
});

const rules = {
  title: [{ required: true, message: '请填写题目', trigger: 'blur' }],
  body: [{ required: true, message: '请填写答案', trigger: 'blur' }],
  job: [{ required: true, message: '请选择工作类型', trigger: 'blur' }],
  classification: [{ required: true, message: '请选择面试类型', trigger: 'blur' }],
  company: [{ required: true, message: '请选择单位', trigger: 'blur' }],
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
    await interviewFormRef.value.validate();
    let res = await createInterview(interviewForm);
    router.push('/interview/' + res.id);
  } catch (error: any) {
    ElMessage.error('请检查是否漏填必填项目');
  }
};

let resetForm = () => {
  interviewFormRef.value.resetFields();
};

const interviewFormRef = ref();
</script>

<style lang="scss" scoped>
.layout_container {
  width: 90vw;
  height: 100vh;
  margin: 0 auto;
  margin-top: 60px;
}
</style>
