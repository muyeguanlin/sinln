<template>
    <div class="container">
      <h1>Fastify MySQL 连接测试</h1>
      <button @click="testConnection" :disabled="loading">
        {{ loading ? '测试中...' : '测试连接' }}
      </button>
      
      <div v-if="result" class="result-section">
        <h2>测试结果</h2>
        <div class="success-message">✅ 连接成功！</div>
        <div class="data-section">
          <h3>返回数据：</h3>
          <span>{{ formattedData }}</span>
        </div>
      </div>
  
      <div v-if="error" class="error-section">
        <h2>错误信息</h2>
        <div class="error-message">❌ {{ error }}</div>
        <br />
        <div></div>
        <br />
      </div>
  
      <!-- <div class="debug-section">
        <h2>调试信息</h2>
        <pre>{{ debugInfo }}</pre> -->
       
      <!-- </div> -->
    </div>
  </template>
  
  <script setup>
  import { ref, reactive, computed } from 'vue';
  import axios from 'axios';
  
  const debugInfo = ref('');
  const result = ref(null);
  const error = ref('');
  const loading = ref(false);
  
  // 计算属性，格式化返回的数据
  const formattedData = computed(() => {
    if (!result.value) return '';
    return JSON.stringify(result.value, null, 2);
  });
  
  async function testConnection() {
    const url = 'http://127.0.0.1:3000';
    
    // 重置状态
    loading.value = true;
    result.value = null;
    error.value = '';
    debugInfo.value = '';
    
    try {
      debugInfo.value += `🕒 ${new Date().toLocaleTimeString()} - 尝试连接: ${url}\n`;
      
      const response = await axios.post(url, { timeout: 5000 });
      
      debugInfo.value += `✅ ${new Date().toLocaleTimeString()} - 请求成功!\n`;
      debugInfo.value += `📊 状态码: ${response.status}\n`;
      debugInfo.value += `🔗 响应头: ${JSON.stringify(response.headers, null, 2)}\n\n`;
      
      // 保存完整的响应数据，而不是直接字符串化
      result.value = response.data;
      
      // 在调试信息中显示数据结构
      debugInfo.value += `📦 响应数据类型: ${typeof response.data}\n`;
      debugInfo.value += `📋 响应数据结构: ${JSON.stringify({
        success: response.data.success,
        count: response.data.count,
        data_length: response.data.data ? response.data.data.length : 0,
        keys: Object.keys(response.data)
      }, null, 2)}\n`;
      
      if (response.data.data && response.data.data.length > 0) {
        debugInfo.value += `👤 第一条数据示例: ${JSON.stringify(response.data.data[0], null, 2)}\n`;
      }
      
    } catch (err) {
      debugInfo.value += `❌ ${new Date().toLocaleTimeString()} - 请求失败!\n`;
      
      if (err.response) {
        // 服务器返回了错误状态码
        error.value = `服务器错误: ${err.response.status} - ${err.response.statusText}`;
        debugInfo.value += `📊 错误状态码: ${err.response.status}\n`;
        debugInfo.value += `📝 错误数据: ${JSON.stringify(err.response.data, null, 2)}\n`;
      } else if (err.request) {
        // 请求发送但没有收到响应
        error.value = '网络错误: 无法连接到服务器';
        debugInfo.value += `🌐 网络错误: ${err.message}\n`;
      } else {
        // 其他错误
        error.value = `请求错误: ${err.message}`;
        debugInfo.value += `⚠️ 其他错误: ${err.message}\n`;
      }
    } finally {
      loading.value = false;
    }
  }
  </script>
  