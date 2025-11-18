<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
      <a-form-item field="name" tooltip="Please enter username" label="Username">
        <a-input
          v-model="form.name"
          placeholder="please enter your username..."
        />
      </a-form-item>
      <a-form-item field="password" label="password">
        <a-input v-model="form.password" placeholder="please enter your post..." />
      </a-form-item>
      <a-form-item field="isRead">
        <a-checkbox v-model="form.isRead"> I have read the manual </a-checkbox>
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit">Submit</a-button>
      </a-form-item>
    </a-form>
    {{ form }}
   
  </template>
  
  <script lang="ts" setup>
  import { ref,reactive} from 'vue';
import { useRouter } from 'vue-router';


const router = useRouter();

const form = reactive({
  name: '',
  password: '',
  isRead: false,
});


const showMessage = ref(false);
                const messageType = ref('');
                const messageText = ref('');
                
const handleSubmit = () => {
  
  if (form.name === 'zst900' && form.password === 'zst654321'&&form.isRead === true) {
                        showMessage.value = true;
                        messageType.value = 'success-message';
                        messageText.value = '验证成功！正在跳转页面...';
                        
                        // 模拟页面跳转
                        setTimeout(() => {
                        router.replace('/layout')
                            
                        }, 1500);
                    } else {
                        showMessage.value = true;
                        messageType.value = 'error-message';
                        messageText.value = '用户名或密码错误，请重试';
                    }
  router.replace('/layout');
};
  </script>
  