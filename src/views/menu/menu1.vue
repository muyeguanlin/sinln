<template>
    <template v-for="item in mockData">
            <a-sub-menu 
            :index="item._id"
            v-if="item.children && item.children.length > 0 && item.children[0].menuType.toString() === '1'" 
        
            >
              <template #title>
                <!-- <icon-apps><location /></icon-apps> -->
                <!-- <i :class="item.icon"></i>  -->
                <span>{{item.menuName}}</span>
              </template>
              
              <Menu1 :mockData="item.children"></Menu1>
            </a-sub-menu>



            <a-menu-item v-else-if="item.menuType.toString() === '1'"
              :index="item.path"
              :key="item._id"
              @click="goToPage(item)"  
            >
            <template #icon>
              <icon-menu />
            </template>
              {{item.menuName}}
            </a-menu-item>
            
      
    </template>
</template>


<script setup lang="ts">

defineProps(['mockData'])

import { useRouter } from 'vue-router'

const router = useRouter()


   

const goToPage = (item:any) => {
  router.push(item.path)  // 使用 item.path 而不是字符串 "item.path"
}

</script>