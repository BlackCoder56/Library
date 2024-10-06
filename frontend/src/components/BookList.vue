<!-- <script setup>
// No need to define props explicitly in <script setup>
</script> -->

<template>
  <ol class="book-list">
    <li class="book" v-for="book in books" :key="book.id">
      <span class="title">{{ book.title }}</span>
      by 
      <span clas="author">{{ book.author }}</span>
    </li>
  </ol>
</template>

<script>
// Props are automatically available in the template
export default {
  props: {
    books: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
*{
  font-size:20px;
}
.title{
  font-weight:bold;
  font-family: 'Times New Roman', Times, serif;
}
</style>
