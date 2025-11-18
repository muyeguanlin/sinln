<template>
    <component :is="currentComponent" v-if="currentComponent" />
    <div v-else>组件加载中...</div>
    <input type="text" :value="route.params.msg" >
      <p>当前路由参数: {{ route.params.msg }}</p>
   
  </template>
  
  <script setup>
  import { useRoute } from 'vue-router'
  import { ref, watch, onMounted } from 'vue'
  
  const route = useRoute()
  const currentComponent = ref('')
 
  // 组件映射
  const componentMap = {
    'add': () => import('./add.vue'),
    'see': () => import('./see.vue'),
    'chakan': () => import('./chakan.vue'),
    // 可以继续添加更多映射
  }
  
  // 加载组件的函数
  const loadComponent = async (msg) => {
    if (componentMap[msg]) {
      const componentLoader = componentMap[msg]
      const module = await componentLoader()
      currentComponent.value = module.default
      
    } else {
      currentComponent.value = null
    }
  }
  
  // 初始加载
  onMounted(() => {
    loadComponent(route.params.msg)
  })
  
  // 监听路由参数变化
  watch(
    () => route.params.msg,
    (newMsg) => {
      loadComponent(newMsg)
    }
  )
  </script>
