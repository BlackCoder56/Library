<script setup>
import BookForm from '@/components/BookForm.vue';
</script>

<template>
    <div class="form-div">
        <h2>Book Form</h2>
        <BookForm />
    </div>
</template>

<style>
    h2{
        text-align: center;
        font-size:26px;
    }
    .form-div{
        border: dashed;
        padding: 8px;
        margin-bottom: 5px;
        border-radius: 4px;
    }
</style>