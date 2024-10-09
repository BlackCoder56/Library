<script setup>
import { RouterView } from 'vue-router';
// import BookFormView from '@/views/BookFormView.vue'

</script>

<template>
  <div class="container">
    <h1>LIBRARY</h1>
    <nav class="navbar">
      <div class="nav-links">
        <router-link to="/">Home</router-link> 
        <router-link to="/addbook">Add Book</router-link> 
        <router-link to="/borrow">Lend Book</router-link> 
      </div>
    </nav>
    <hr />
    <!-- <BookFormView /> -->
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #000;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  text-decoration: none;
}

.nav-links {
  /* flex-grow: 1; */
  text-align: center;
  /* text-decoration: none; */
}

/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: rgb(9, 112, 160);
  margin-right:30px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color:blue;
}

h1{
  text-align: center;
  font-size: 50px;
  color:blue;
}

.container{
  /* background-color:darkolivegreen; */
  padding:10px;
  width: 50%;
  margin: auto;
  border-radius: 4px;
}

</style>
