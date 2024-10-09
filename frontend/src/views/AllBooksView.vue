<script setup>
import BookList from '@/components/BookList.vue';
import { ref, watch } from 'vue';
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

// Reactive searchQuery
const searchQuery = ref("");

// GraphQL query with title_icontains variable
const GET_BOOKS = gql`
  query Books($title_icontains: String) {
    books(titleIcontains: $title_icontains) {
      id
      title
      author
      category {
        categoryName
      }
      total
    }
  }
`;

// Watch the searchQuery and refetch data when it changes
const { result, loading, error, refetch } = useQuery(GET_BOOKS, {
  title_icontains: searchQuery.value
});

// Debounce function to reduce unnecessary API calls
const debounceSearch = (callback, delay = 300) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      callback(...args);
    }, delay);
  };
};

// Function to trigger search with debounce
const fetchBooks = debounceSearch(() => {
  refetch({
    title_icontains: searchQuery.value || null // Pass null to display all books when input is empty
  });
});

// Watch for changes in searchQuery and trigger fetchBooks
watch(searchQuery, () => {
  fetchBooks();
});
</script>

<template>
  <div class="list-border"> 
    <!-- Search Input Field -->
    <input v-model="searchQuery" placeholder="Search books..." />
    <h2>Book Shelf</h2>  
    <div class="loader" v-if="loading">Loading...</div>
    <div class="err" v-else-if="error">Error: {{ error.message }} books! <br/>Try refreshing page.</div>
    
    <!-- Check if books are found -->
    <template v-else>
      <div v-if="result.books.length === 0" class="no-books">
        No books found matching "{{ searchQuery }}".
      </div>
      <BookList v-else :books="result.books" />
    </template>
  </div>
</template>

<style>
.err {
  color: darkred;
  font-style: italic;
  text-align: center;
  font-weight: bold;
  font-size: 20px;
}

.no-books {
  color: darkred;
  font-style: italic;
  text-align: center;
  font-weight: bold;
  font-size: 18px;
}
.loader{
    text-align: center;
}
h2 {
  text-align: center;
  font-size: 26px;
}

.list-border {
  /* border: dashed; */
  border-radius: 4px;
  padding: 8px;
}

input {
  display: block;
  margin: 10px auto;
  padding: 8px;
  width: 80%;
  max-width: 400px;
  font-size: 16px;
  border-radius: 4px;
  border: 1px solid #ccc;
}
</style>
