<template>
  <Toptbar></Toptbar>
  <div class="layout_container">
    <Category @filter="filter"></Category>
    <el-card style="margin-top: 15px; margin-bottom: 15px">
      <el-table
        :data="show_question"
        stripe
        :header-cell-style="{ fontSize: '16px' }"
        @sort-change="handleSortChange"
      >
        <el-table-column label="序号" width="60" align="center" type="index"></el-table-column>
        <el-table-column label="标题" prop="title">
          <template #="{ row }">
            <div class="quseston_title" @click="question_show(row.id)">
              {{ row.title }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="标签" width="160" sortable v-if="hiddenCol">
          <template #="{ row }">
            <div class="flex gap-2">
              <el-tag
                v-for="(badge, id) in row.badge.trim().split(' ')"
                :color="badge_style[id]"
                style="margin-left: 3px"
                effect="dark"
                >{{ badge }}</el-tag
              >
            </div>
          </template>
        </el-table-column>
        <el-table-column
          label="面试时间"
          prop="interview_at"
          width="120"
          sortable="custom"
          v-if="hiddenCol"
        ></el-table-column>
        <el-table-column
          label="热度"
          prop="id"
          width="80"
          sortable
          v-if="hiddenCol"
        ></el-table-column>
        <el-table-column label="收藏" width="80" align="center">
          <template #default>
            <div class="flex gap-2">
              <el-button type="primary" style="margin-left: 2px" @click="handleFavorite"
                >收藏</el-button
              >
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div class="pagination-container">
        <el-pagination
          background
          :total="count"
          v-model:current-page="pageNo"
          v-model:page-size="pageLimit"
          @current-change="page_change"
          layout="total, prev, pager, next"
          :small="!hiddenCol"
        >
        </el-pagination>
      </div>
    </el-card>
    <div style="height: 1px" />
  </div>
</template>

<script setup lang="ts">
import Toptbar from '@/components/topbar/index.vue';
import { question } from '@/api/question';
import { ElMessage } from 'element-plus';
import { ref, onMounted } from 'vue';

let badge_style = ['red', 'green', 'purple', 'blue', ''];
const params = {
  subject: -1,
  company: -1,
  job: -1,
};
// 屏幕宽度
const windowWidth = ref(0);
// 屏幕高度
const windowHeight = ref(0);
const hiddenCol = ref(false);
let all_question = ref();
let filter_question = ref();
let show_question = ref();
let count = ref(-1);
let pageNo = ref<number>(1);
let pageLimit = ref<number>(20);
let page_select = ref<number>(1);
const getQuestion = async () => {
  all_question.value = await question(params);
  filter_question.value = all_question.value;
  get_show_question(0, pageLimit.value);
};
const question_show = (id: any) => {
  window.open('/question/' + id, '_blank');
};
const get_show_question = (start: any, end: any) => {
  show_question.value = filter_question.value.slice(start, end);
  count.value = filter_question.value.length;
};
const filter = (params: any) => {
  const filterArray = [];
  for (const item of all_question.value) {
    if (
      (params.job.length == 0 || params.job.includes(item.job)) &&
      (params.subject.length == 0 || params.subject.includes(item.subject)) &&
      (params.company.length == 0 || params.company.includes(item.company))
    ) {
      filterArray.push(item);
    }
  }
  filter_question.value = filterArray;
  get_show_question(0, pageLimit.value);
};

const page_change = (value: any) => {
  page_select.value = value;
  let start = (page_select.value - 1) * pageLimit.value;
  let end = page_select.value * pageLimit.value;
  get_show_question(start, end);
};
const handleSortChange = (data: any) => {
  let sort_key: string = data.prop;
  if (data.order === 'descending') {
    filter_question.value.sort((a: any, b: any) => {
      if (a[sort_key] > b[sort_key]) return -1;
      if (a[sort_key] < b[sort_key]) return 1;
      if (a.id > b.id) return -1;
      if (a.id < b.id) return 1;
      return 0;
    });
  } else {
    filter_question.value.sort((a: any, b: any) => {
      if (a[sort_key] < b[sort_key]) return -1;
      if (a[sort_key] > b[sort_key]) return 1;
      if (a.id < b.id) return -1;
      if (a.id > b.id) return 1;
      return 0;
    });
  }
  let start = (page_select.value - 1) * pageLimit.value;
  let end = page_select.value * pageLimit.value;
  get_show_question(start, end);
};

onMounted(() => {
  document.title = '真题列表';
  getWindowResize();
  window.addEventListener('resize', getWindowResize);
  getQuestion();
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
};
</script>
<script lang="ts">
export default {
  name: 'Contain',
};
</script>
<style lang="scss" scoped>
.layout_container {
  width: $base-contain-width;
  height: 100vh;
  margin: 0 auto;
  margin-top: 70px;

  .quseston_title {
    color: rgb(0, 157, 248);
    text-decoration-line: underline;
    cursor: pointer;
  }
}

.el-tag {
  border: none;
}

.pagination-container {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}
</style>
