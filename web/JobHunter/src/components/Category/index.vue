<template>
  <div style="margin-top: 30px; ">
    <el-card style="padding: 0px !important;">
      <el-form :inline="true">
        <el-form-item>
          <el-select v-model="companyId" placeholder="公司不限" style="width: 330px" :multiple="true" clearable
            @change="handlerCompany">
            <el-option v-for="item in categoryStore.company" :index="item.id" :key="item.id" :label="item.name"
              :value="item.id" />
          </el-select>
        </el-form-item>
        <el-form-item v-if="props.show_2">
          <el-select v-model="subjectId" placeholder="科目不限" style="width: 330px" :multiple="true" clearable
            @change="handlerSubject">
            <el-option v-for="item in categoryStore.subject" :index="item.id" :key="item.id" :label="item.name"
              :value="item.id" />
          </el-select>
        </el-form-item>

        <el-form-item>
          <el-select v-model="jobId" placeholder="岗位不限" style="width: 330px" :multiple="true" clearable
            @change="handlerJob">
            <el-option v-for="item in categoryStore.job" :index="item.id" :key="item.id" :label="item.name"
              :value="item.id" />
          </el-select>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import useCategoryStore from "@/store/models/category"
const categoryStore = useCategoryStore()
const emit = defineEmits(["filter"])
const props = defineProps({
  show_2: {
    type: Boolean,
    required: false,
    default: true
  },
});

let companyId = ref();
let subjectId = ref();
let jobId = ref();


let select = ref({
  company: [],
  subject: [],
  job: [],
});
let handlerCompany = (value: any) => {
  select.value.company = value;
  emit("filter", select.value)
};
let handlerSubject = (value: any) => {
  select.value.subject = value;
  emit("filter", select.value)
};
let handlerJob = (value: any) => {
  select.value.job = value;
  emit("filter", select.value)
}
onMounted(async () => {
  // if (!categoryStore.flag) {
  //   await categoryStore.get_category()
  // }
});
</script>
<script lang="ts">
export default {
  name: 'Category',
};
</script>
<style>
.el-card__body {
  padding-bottom: 0px !important;
}
</style>
