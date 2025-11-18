import { createRouter, createWebHashHistory } from 'vue-router'; // 修改了这里的引入history 模式不能在生产模式使用
const routes=[
    {
      path: '/',
      redirect: 'login',
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/login/index.vue'),
      meta: {
        requiresAuth: false,
      },
    },
    {
      path: '/layout',
      name: 'layout',
      component: () => import('@/views/layout.vue'),
      children: [
        {
          path: '/layout',
          redirect: 'system/see',
        },
        {
        path: '/system/add',
        name: 'sys-add',
        component: () => import('@/views/components/add.vue'),

      },
      {
        path: '/system/see',
        name: 'sys-see',
        component: () => import('@/views/components/see.vue'),

      },
      {
        path: '/components/:msg', 
        name: 'sys-id',
        component: () => import('@/views/components/components.vue'),

      },
    ]
    },
  ];



  const router=createRouter({
    history:createWebHashHistory(),
    routes,
  })
  
  export default router;

