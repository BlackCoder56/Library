<style scoped>
    form {
    width: 60vw;
    max-width: 500px;
    min-width: 300px;
    margin: 0 auto;
    padding-bottom: 2em;
  }
  
  fieldset {
    border: none;
    padding: 2rem 0;
    border-bottom: 3px solid #3b3b4f;
  }
  
  fieldset:last-of-type {
    border-bottom: none;
  }
  
  label {
    display: block;
    margin: 0.5rem 0;
  }
  
  input,
  select {
    margin: 10px 0 0 0;
    width: 100%;
    font-size: 1.1rem;
  }

  select{
    /* background-color: #101062; */
    color:  rgb(9, 112, 160);
    width:85%;
    min-height: 2em;
  }
  input {
    /* background-color: #101062; */
    border: 1px solid #0a0a23;
    color:  rgb(9, 112, 160);
  }
  
  .inline {
    width: unset;
    margin: 0 0.5em 0 0;
    vertical-align: middle;
  }
  
  input[type="submit"] {
    display: block;
    width: 10%;
    margin: 1em auto;
    height: 2em;
    font-size: 1.1rem;
    background-color: #101062;
    border-color: white;
    min-width: 200px;
    color: #ffff;
  }

  
  input[type="file"] {
    padding: 1px 2px;
  }
  
  .inline{
    display: inline; 
  }
  
  a{
    color:#dfdfe2;
  }
  
</style>
<template>
  <form method="post" action="">
    <fieldset>
      <label for="book-name">Enter Book Name:
        <input id="book-name" name="book-name" type="text" required />
      </label>      
      <label for="author-name">Enter Author Name:
        <input id="author-name" name="author-name" type="text" required />
      </label>
      <label for="referrer">How did you hear about us?
        <select id="referrer" name="referrer" v-model="selectedCategory" required>
          <option value="">(select one)</option>          
          <!-- Display categories when loaded -->
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.categoryName }}
          </option>
        </select>
      </label>      
      <label for="age">Input Number of Books:
        <input id="age" type="number" name="age" min="10" max="120" required />
      </label>
    </fieldset>    
    <input type="submit" value="Save Book" />
  </form>
</template>

<script>
import { ref, watch } from "vue";
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

export default {
  setup() {
    const { result, loading, error } = useQuery(gql`
      query {
        categories {
          id
          categoryName
        }
      }
    `);
    
    const categories = ref([]);
    const selectedCategory = ref("");  // v-model for the select element
    
    // Watch the result for changes and update categories
    watch(result, (newVal) => {
      if (newVal?.categories) {
        categories.value = newVal.categories;
        console.log('Categories loaded:', categories.value);  // Debugging
      }
    });

    return { categories, selectedCategory, loading, error };
  }
};
</script>


