<template>
  <Toptbar></Toptbar>
  <div class="layout_container">
    <MdPreview v-model="text" previewTheme="cyanosis" :theme="theme" codeTheme="atom" :codeFoldable="false" />
  </div>
</template>

<script setup lang="ts">
import { getInterviewById } from '@/api/interview';
import { ref, onMounted, onUnmounted } from 'vue';
import { useRoute } from 'vue-router';
import { MdPreview } from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import Toptbar from '@/components/topbar/index.vue';
const text = ref();
let route = useRoute();
let theme: any = ref('default');

const bc = new BroadcastChannel('my-channel');

onMounted(async () => {
  bc.onmessage = (event) => {
    if (event.data.theme) theme.value = 'dark';
    else theme.value = 'light';
  };
  theme.value = localStorage.getItem('vueuse-color-scheme');
  if (theme.value == 'auto') theme.value = 'light';
  let obj = await getInterviewById(route.params.id);
  document.title = obj.title;
  text.value =
    '# ' +
    obj.title +
    '\n' +
    obj.body +
    '\n';
});

onUnmounted(() => {
  bc.close()
});
</script>
<style lang="scss" scoped>
.layout_container {
  width: $base-contain-width;
  height: 100vh;
  margin: 0 auto;
  margin-top: 5dvh;
}
</style>