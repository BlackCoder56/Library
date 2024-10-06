<script setup>
import BookList from '@/components/BookList.vue';
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

const { result, loading, error }  = useQuery(gql`
         query{
        allBooks{
            id
            title
            author
        }
    }
`
);
</script>


<template>
    <div class="list-border">
        <h2>Book Shelf</h2>   
        <div v-if="loading">Loading...</div>
        <div v-else-if="error">{{ error.message }}.</div>
        <BookList v-else :books="result.allBooks" />
    </div>
</template>

<style>
h2{
    text-align: center;
    font-size:26px;
}
.list-border{
    border: dashed;
    padding:8px;
}
</style>