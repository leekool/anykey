<script lang="ts">
    export let link: string;

    function handleClick(item: string) {
        console.log(item)
        return item;
    }
</script>

<!-- <a href="#{link.toLowerCase()}">{link}</a> -->
<!-- <span on:click={return link.toLowerCase()}>{link}</span> -->
<div class="link"
     on:click={() => handleClick(link)}
    >
    {link}
</div>

<style>
    .link {
        color: black;
        padding: 3px 6px;
        text-decoration: none;
        display: block;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .link:hover {
        background-color: #ddd;
    }
</style>
