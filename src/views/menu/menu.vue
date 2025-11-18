<template>
  <div class="menu-demo">
    
    <a-menu
      class="menu-framework"

    >
    
      <Menu1 :mockData="mockData"></Menu1>
      </a-menu>
  </div>
</template>




<script setup>

  import Menu1 from './menu1.vue';
  import mockData from './mock.js';




</script>
<!-- <style scoped>
.menu-demo {
  box-sizing: border-box;
  width: 100%;
  padding: 40px;
  background-color: var(--color-neutral-2);
}
</style> -->
