<template>
  <a-layout class="layout-demo">
    <a-layout-sider
    
      collapsible
     
    >
    
    <Menu />
    </a-layout-sider>
    <a-layout class="contener">
      <router-view />
      <Taupage />
    </a-layout>
  </a-layout>
</template>
<script  setup>
import Menu from '@/views/menu/menu.vue';
import Taupage from '@/views/login/tauri-page.vue';


</script>
<style scoped>
.layout-demo {
  height: 100vh;
  background: var(--color-fill-2);
  border: 1px solid var(--color-border);
}
.layout-demo :deep(.arco-layout-sider) .logo {
  height: 32px;
  margin: 12px 8px;
  background: rgba(34, 25, 25, 0.2);
}
.layout-demo :deep(.arco-layout-sider-light) .logo{
  background: var(--color-fill-2);
}

</style>
