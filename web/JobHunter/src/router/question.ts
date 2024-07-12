//对外暴露配置路由(常量路由):全部用户都可以访问到的路由
export const questionRoute = [
  {
    path: '/',
    redirect: 'question',
    name: 'home',
  },
  {
    path: '/question',
    component: () => import('@/views/question/list/index.vue'),
    name: 'question',
  },
  {
    path: '/question/:id',
    component: () => import('@/views/question/retrieve/index.vue'),
    name: 'question_show',
  },
  {
    path: '/question/add',
    component: () => import('@/views/question/post/index.vue'),
    name: 'question_add',
  },
];
