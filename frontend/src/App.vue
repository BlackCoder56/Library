<script setup>
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="container">
    <h1>LIBRARY</h1>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #fff;
}

h1{
  text-align: center;
  font-size: 3rem;
}

.container{
  background-color:darkolivegreen;
  padding:10px;
}

</style>
