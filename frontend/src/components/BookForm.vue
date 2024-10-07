<template>
    <form>
        <label for="bookName">Enter Book name:</label><br/>
        <input id="bookName" type="text" required class="txt" placeholder="Enter book name" /><br/>
        <label for="authorName">Enter Author name:</label><br/>
        <input id="authorName" type="text" required class="txt" placeholder="Enter Author name"/>
        <br/>
        <div class="btn">
            <input class="btn-a" type="submit" value="Add" />
            <input class="btn-b" type="submit" value="Update" />
            <input class="btn-c" type="submit" value="Delete" />
        </div>
    </form>
</template>

<style>
    label{
        margin-left:  35%;
    }
    .txt{
        margin-left: 35%;
        margin-bottom: 20px;
    }
    .btn{
        margin-left: 35%;
    }
    .btn-a, .btn-b, .btn-c{
        margin-right: 12px;    
        margin-top: 5px;   
        margin-bottom: 10px; 
    }
</style>