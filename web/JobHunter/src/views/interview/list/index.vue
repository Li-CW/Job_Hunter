<template>
  <Toptbar></Toptbar>
  <div class="layout_container">
    <Category @filter="filter" :show_2="false"></Category>
    <el-card style="margin-top: 15px; margin-bottom: 15px;">
      <el-table :data="show_interview" stripe :header-cell-style="{ fontSize: '16px' }">
        <el-table-column label="序号" width="60" align="center" type="index"></el-table-column>
        <el-table-column label="标题" prop="title">
          <template #="{ row }">
            <div class="interview_title" @click="interview_show(row.id)">
              {{ row.title }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="分类" width="90" sortable v-if="hiddenCol">
          <template #="{ row }">
            <div class="flex gap-2">
              {{ row.classification_display }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="公司" width="90" sortable v-if="hiddenCol">
          <template #="{ row }">
            <div class="flex gap-2">
              {{ row.company_name }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="岗位" width="90" sortable v-if="hiddenCol">
          <template #="{ row }">
            <div class="flex gap-2">
              {{ row.job_name }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="面试时间" prop="interview_at" width="120" sortable v-if="hiddenCol"></el-table-column>
        <el-table-column label="热度" prop="read_count" width="80" sortable v-if="hiddenCol"></el-table-column>
        <el-table-column label="收藏" width="80" align="center">
          <template #default>
            <div class="flex gap-2">
              <el-button type="primary" style="margin-left: 2px" v-if="true" @click="handleFavorite">收藏</el-button>
              <el-button type="danger" style="margin-left: 2px" v-if="false">取消</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination-container">
        <el-pagination background :total="count" v-model:current-page="pageNo" v-model:page-size="pageLimit"
          @current-change="page_change" layout="total, prev, pager, next" :small="!hiddenCol">
        </el-pagination>
      </div>
    </el-card>
    <div style="height: 1px;" />
  </div>
</template>

<script setup lang="ts">
import { interview } from '@/api/interview';
import { ref, onMounted } from 'vue';
import useCategoryStore from '@/store/models/category';
import Toptbar from '@/components/topbar/index.vue';
import { ElMessage } from 'element-plus';
const categoryStore = useCategoryStore();
const windowWidth = ref(0);
const windowHeight = ref(0);
const hiddenCol = ref(false);
let all_interview = ref();

let filter_interview = ref();
let show_interview = ref();
let count = ref(-1);
let pageNo = ref<number>(1);
let pageLimit = ref<number>(20);
const getInterview = async () => {
  all_interview.value = await interview();
  const company_dict: any = {};

  for (const company of categoryStore.company) {
    company_dict[company['id']] = company['name'];
  }
  const job_dict: any = {};
  for (const job of categoryStore.job) {
    job_dict[job['id']] = job['name'];
  }
  for (const interview of all_interview.value) {
    interview['company_name'] = company_dict[interview['company']];
    interview['job_name'] = job_dict[interview['job']];
  }
  filter_interview.value = all_interview.value;
  get_show_interview(0, pageLimit.value);
};
const get_show_interview = (start: any, end: any) => {
  show_interview.value = filter_interview.value.slice(start, end);
  count.value = filter_interview.value.length;
};
const interview_show = (id: any) => {
  window.open('/interview/' + id, '_blank');
};
const filter = (params: any) => {
  const filterArray = [];
  for (const item of all_interview.value) {
    if (
      (params.job.length == 0 || params.job.includes(item.job)) &&
      (params.company.length == 0 || params.company.includes(item.company))
    ) {
      filterArray.push(item);
    }
  }
  filter_interview.value = filterArray;
  get_show_interview(0, pageLimit.value);
};

const page_change = (value: any) => {
  let start = (value - 1) * pageLimit.value;
  let end = value * pageLimit.value;
  get_show_interview(start, end);
};

onMounted(async () => {
  document.title = '面经列表';
  getWindowResize();
  window.addEventListener('resize', getWindowResize);
  await getInterview();
});
const getWindowResize = () => {
  windowWidth.value = window.innerWidth;
  windowHeight.value = window.innerHeight;
  if (windowWidth.value < 780) hiddenCol.value = false;
  else hiddenCol.value = true;
};
const handleFavorite = () => {
  ElMessage({
    message: '暂未开放此功能',
    type: 'info',
    offset: 100,
  });
}
</script>
<style lang="scss" scoped>
.layout_container {
  width: $base-contain-width;
  height: 100vh;
  margin: 0 auto;
  margin-top: 70px;
}

.el-tag {
  border: none;
}

.pagination-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

.interview_title {
  color: rgb(0, 157, 248);
  text-decoration-line: underline;
  cursor: pointer;
}
</style>
