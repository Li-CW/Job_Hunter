//对外暴露配置路由(常量路由):全部用户都可以访问到的路由
export const interviewRoute = [
  {
    path: '/interview',
    component: () => import('@/views/interview/list/index.vue'),
    name: 'interview',
  },
  {
    path: '/interview/:id',
    component: () => import('@/views/interview/retrieve/index.vue'),
    name: 'interview_show',
  },
  {
    path: '/interview/add',
    component: () => import('@/views/interview/post/index.vue'),
    name: 'interview_add',
  },
];
