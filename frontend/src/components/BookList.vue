<template>
  <table >
    <thead>
      <tr>
        <th>Book Name</th>
        <th>Author</th>
        <th>Category</th>
        <th>Total No.</th>
        <th>Borrowed</th>
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
        <td>{{ book.category.categoryName }}</td>
        <td class="book-total">{{ book.total }}</td>
        <td class="books-borrowed">0</td>
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
  *{
    font-size:20px;
  }
  table {
    border-collapse: collapse; 
    width: 100%; 
  }

  th, td {
      border: 1px solid black; 
      padding: 8px; 
  }

  .book-total, .books-borrowed{
    text-align: center;
  }

  .title{
    font-weight: bolder;
    font-family: 'Times New Roman', Times, serif;
  }
</style>
