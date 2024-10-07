<script setup>
import { RouterView } from 'vue-router';
import BookFormView from '@/views/BookFormView.vue'
</script>

<template>
  <div class="container">
    <h1>LIBRARY</h1>
    <hr />
    <BookFormView />
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
  font-size: 50px;
}

.container{
  background-color:darkolivegreen;
  padding:10px;
  width: 50%;
  margin: auto;
  border-radius: 4px;
}

</style>
