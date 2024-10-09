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
const debounceSearch = (callback, delay = 1000) => {
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
    <div class="loader" v-if="loading"></div>
    <div class="err" v-else-if="error">
      <span class="und-text">Connection error:</span>
      <br/>
       {{ error.message }} books! Try refreshing page.</div>
    
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
.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
  margin-left:45%;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.err {
  color: #fff;
  text-align: center;
  font-weight: bold;
  font-size: 16px;
  background-color: #f44336;
  padding:4px;
  /* font-family: Verdana, Geneva, Tahoma, sans-serif; */
}

.und-text{
  text-decoration: underline;
}
.no-books {
  color:  rgb(9, 112, 160);
  font-style: italic;
  text-align: center;
  font-weight: bold;
  font-size: 18px;
}

.loader{
  text-align: center;
  color:  rgb(9, 112, 160);
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
