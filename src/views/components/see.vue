<template>
    <div class="user-form">
      <h2>用户注册</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label>姓名:</label>
          <input 
            type="text" 
            v-model="formData.name" 
            required 
          />
        </div>
        
        <div class="form-group">
          <label>邮箱:</label>
          <input 
            type="email" 
            v-model="formData.email" 
            required 
          />
        </div>
        
        <div class="form-group">
          <label>年龄:</label>
          <input 
            type="number" 
            v-model="formData.age" 
            min="0" 
          />
        </div>
        
        <div class="form-group">
          <label>职业:</label>
          <select v-model="formData.job">
            <option value="">请选择</option>
            <option value="developer">开发者</option>
            <option value="designer">设计师</option>
            <option value="manager">经理</option>
          </select>
        </div>
        
        <div class="form-group">
          <label>兴趣爱好:</label>
          <div>
            <label>
              <input type="checkbox" v-model="formData.hobbies" value="reading"> 阅读
            </label>
            <label>
              <input type="checkbox" v-model="formData.hobbies" value="sports"> 运动
            </label>
            <label>
              <input type="checkbox" v-model="formData.hobbies" value="music"> 音乐
            </label>
          </div>
        </div>
        
        <button type="submit" :disabled="loading">
          {{ loading ? '提交中...' : '提交' }}
        </button>
      </form>
      
      <!-- 显示结果 -->
      <div v-if="result" class="result success">
        <h3>提交成功!</h3>
        <pre>{{ JSON.stringify(result, null, 2) }}</pre>
      </div>
      
      <div v-if="error" class="result error">
        <h3>提交失败!</h3>
        <p>{{ error }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive } from 'vue';
  import axios from 'axios';
  
  // 表单数据
  const formData = reactive({
    name: '',
    email: '',
    age: '',
    job: '',
    hobbies: []
  });
  
  // 状态管理
  const loading = ref(false);
  const result = ref(null);
  const error = ref('');
  
  // 提交表单
  const submitForm = async () => {
    loading.value = true;
    error.value = '';
    result.value = null;
    
   
      // 发送 POST 请求到后端
      const response = await axios.post('http://localhost:3000/see', formData, {
        headers: {
          'Content-Type': 'application/json'
        },
        timeout: 10000 // 10秒超时
      });
      
      result.value = response.data;
      
      // 重置表单
      Object.assign(formData, {
        name: '',
        email: '',
        age: '',
        job: '',
        hobbies: []
      });
      
    
  };
  </script>
  
  <style scoped>
  .user-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .form-group div label {
    display: inline-block;
    margin-right: 15px;
    font-weight: normal;
  }
  
  button {
    width: 100%;
    padding: 12px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  button:disabled {
    background-color: #6c757d;
    cursor: not-allowed;
  }
  
  .result {
    margin-top: 20px;
    padding: 15px;
    border-radius: 4px;
  }
  
  .success {
    background-color: #d4edda;
    border: 1px solid #c3e6cb;
    color: #155724;
  }
  
  .error {
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
    color: #721c24;
  }
  
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  </style>