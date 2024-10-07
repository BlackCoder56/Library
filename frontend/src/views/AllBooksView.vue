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
        <div class="err" v-else-if="error">Error: {{ error.message }} books.</div>
        <BookList v-else :books="result.allBooks" />
    </div>
</template>

<style>
.err{
    color:darkred;
    font-style: italic;
}

h2{
    text-align: center;
    font-size:26px;
}
.list-border{
    border: dashed;
    border-radius: 4px;
    padding:8px;
}
</style>