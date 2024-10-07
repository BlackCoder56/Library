<!-- <script setup>
// No need to define props explicitly in <script setup>
</script> -->

<template>
  <table >
    <thead>
      <tr>
        <td>
          <span class="title">Book Name</span></td>
        <td>
          <span class="title">Author</span>
        </td>
        <td>
          <span class="title">Category</span>
          </td>
        <td>
          <span class="title">Total No.</span>
        </td>
        <td>
          <span class="title">Borrowed</span>
        </td>
      </tr>
    </thead>
    <tbody class="book" v-for="book in books" :key="book.id">
      <tr>
        <td>
          {{ book.title }}
        </td>
        <td>
          <span clas="author">{{ book.author }}</span>
        </td>
        <td>Science</td>
        <td>54</td>
        <td>2</td>
      </tr>
    </tbody>
  </table>
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
table{
  border: solid;  
  margin-left: 20%;
}
*{
  font-size:20px;
}
.title{
  font-weight:bold;
  font-family: 'Times New Roman', Times, serif;
}
</style>
