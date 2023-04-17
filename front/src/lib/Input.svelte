<script>
    export let inputValue = "";
</script>

<input
    type="text"
    placeholder="Search..."
    autocomplete="off"
    id="searchInput"
    bind:value={inputValue}
    on:input
/>
<span id="search-icon"></span>

<style>
    /* The search field */
    #searchInput {
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        cursor: pointer;
        padding: 3px 6px;
        border: none;
        border-bottom: 1px solid #ddd;
    }
    #searchInput:focus {
        outline: 3px solid #ddd;
    }

    #search-icon {
        position: absolute;
        left: 10px;
        top: 10px;
        font-size: 1.2rem;
    }
</style>
