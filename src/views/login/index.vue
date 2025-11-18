<template>
  <div class="container">
    <div class="logo">
      <img
        alt="logo"
        src="//p3-armor.byteimg.com/tos-cn-i-49unhts6dw/dfdba5317c0c20ce20e64fac803d52bc.svg~tplv-49unhts6dw-image.image"
      />
      <div class="logo-text">Arco Design Pro111
        
      </div>
    </div>
    <!-- <LoginBanner /> -->
    <div class="content">
      <div class="content-inner">
        <Login />
      </div>
   
       
    </div>
    
  </div>
  <div class="footer">
      <Taupage />
  </div>
</template>

<script lang="ts" setup>
  import Taupage from './tauri-page.vue';
  // import LoginBanner from './components/banner.vue';
  import Login from './login.vue';
  // import Menu from './menu.vue';
</script>

<style scoped>
  .container {
    display: flex;
    height: 50vh;

    
    .content {
      position: relative;
      display: flex;
      flex: 1;
      align-items: center;
      justify-content: center;
      padding-bottom: 4px;
    }

 
 

  .logo {
    position: fixed;
    top: 24px;
    left: 22px;
    z-index: 1;
    display: inline-flex;
    align-items: center;

    &-text {
      margin-right: 4px;
      margin-left: 4px;
      color: var(--color-fill-1);
      font-size: 20px;
    }
  }


.footer {
      /* position: absolute; */
      position: relative;
      right: 0;
      bottom: 0;
      width: 20%;
    }

  }

</style>


