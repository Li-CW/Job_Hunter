<template>
  <div>
    <router-view></router-view>
  </div>
  <div class="theme">
    <el-switch
      v-model="isDark"
      active-color="var(--el-fill-color-dark)"
      inactive-color="var(--el-color-primary)"
      @change="toggleDark"
      active-text="暗黑模式"
      inactive-text="正常模式"
      class="mb-2"
      inline-prompt
    />
  </div>
</template>

<script setup lang="ts">
// import { ElMessageBox } from 'element-plus'
// import Toptbar from '@/components/topbar/index.vue';
import { onMounted, onUnmounted } from 'vue';
import { useDark, useToggle } from '@vueuse/core';
import useCategoryStore from '@/store/models/category';
const categoryStore = useCategoryStore();
const isDark = useDark();
const bc = new BroadcastChannel('my-channel');

const toggleDark = (value: any) => {
  useToggle(isDark);
  bc.postMessage({ theme: value });
};
onMounted(async () => {
  await categoryStore.get_category();
  console.log(10000)
});
onUnmounted(() => {
  bc.close();
});
</script>

<style scoped>
.theme {
  transform: rotate(90deg);
  transform-origin: center center;
  position: fixed;
  right: 10px;
  bottom: 80px;
  z-index: 99999;
}
</style>
