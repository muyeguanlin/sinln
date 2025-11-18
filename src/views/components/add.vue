<template>
    <div>
      <button @click="testConnection">测试连接</button>
      <div>
        <h3>调试信息:</h3>
        <pre>{{ debugInfo }}</pre>
      </div>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const debugInfo = ref('');

async function testConnection(){
    const url = 'http://127.0.0.1:3000/add';
   
    debugInfo.value += `尝试连接: ${url}\n`;
    const response = await axios.post(url, { timeout: 5000 });
    debugInfo.value += `✅ 成功: ${response.data}\n\n`;
   
};
</script>
