<template>
    <a-form :model="form" :style="{ width: '600px' }" @submit="handleSubmit">
      <a-form-item field="name" tooltip="Please enter username" label="Username">
        <a-input
          v-model="form.name"
          placeholder="请输入用户名"
        />
      </a-form-item>
      <a-form-item field="password" label="password">
        <a-input v-model="form.password" placeholder="请输入密码" />
      </a-form-item>
      <a-form-item field="isRead">
        <a-checkbox v-model="form.isRead"> 我已阅读用户手册 </a-checkbox>
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit">登录</a-button>
      </a-form-item>
    </a-form>
    {{ form }}
    <div class="default-account">
        <h3>默认测试账号信息</h3>
        <p>用户名: <strong>admin</strong></p>
        <p>密码: <strong>admin123</strong></p>
        <p style="margin-top: 8px; font-size: 12px; color: #888;">
            请勾选"我已阅读用户手册"后使用默认账号登录
        </p>
    </div>
    
    <div class="footer-links">
        <a href="#">忘记密码?</a>
        <a href="#">注册新账号</a>
    </div>

 
  </template>
  
  <script lang="ts" setup>
  import { ref,reactive} from 'vue';
import { useRouter } from 'vue-router';


const router = useRouter();

const form = reactive({
  name: 'admin',
  password: 'admin123',// 设置默认密码
  isRead: true,
});


const showMessage = ref(false);
const messageType = ref('');
const messageText = ref('');
                
const handleSubmit = () => {
  
  if (form.name === 'admin' && form.password === 'admin123'&&form.isRead === true) {
                        showMessage.value = true;
                        messageType.value = 'success-message';
                        messageText.value = '验证成功！正在跳转页面...';
                        
                        // 模拟页面跳转
                        router.replace('/layout')
                        // setTimeout(() => {
                        // router.replace('/layout')
                            
                        // }, 1500);
                    } else {
                        // showMessage.value = true;
                        // messageType.value = 'error-message';
                        // messageText.value = '用户名或密码错误，请重试';
                    }
  // router.replace('/layout');
};

// const messageIcon = () => {
//                     switch(messageType.value) {
//                         case 'success-message': return 'fas fa-check-circle';
//                         case 'error-message': return 'fas fa-exclamation-circle';
//                         default: return 'fas fa-info-circle';
//                     }
//                 };
  </script>
  