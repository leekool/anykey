<script lang="ts">
    export let selectedItem: any;
    export let menuItems: { name: string; path: string }[] = [];

    let inputEl: HTMLElement;
    let inputValue: string = "";
    let filteredItems: { name: string; path: string }[] = [];

    const handleClick = (item: { name: string; path: string }) => selectedItem = item;

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.name.toLowerCase().match(inputValue.toLowerCase())
        ));
    };
</script>

<div class="main">
    <input
        id="searchInput"
        type="text"
        placeholder="filter..."
        autocomplete="off"
        bind:this={inputEl}
        bind:value={inputValue}
        on:input={handleInput}
    />
    <div class="list-content">
        {#if filteredItems.length > 0}
            {#each filteredItems as item}
                <div class="link" on:click={() => handleClick(item)}>
                    {item.name}
                </div>
            {/each}
        {:else}
            {#each menuItems as item}
                <div class="link" on:click={() => handleClick(item)}>
                    {item.name}
                </div>
            {/each}
        {/if}
    </div>
</div>

<style>
    @import url("../../static/fonts/real-icons.css");

    .main {
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        height: 100%;
    }

    /* .dropbtn { */
    /*     font-family: "Tamzen", sans-serif; */
    /*     background-color: brown; */
    /*     color: white; */
    /*     font-size: 15px; */
    /*     cursor: pointer; */
    /*     border: 1px solid #ccc; */
    /*     padding: 3px 6px; */
    /* } */
    /**/
    /* .dropbtn:hover, */
    /* .dropbtn:focus { */
    /*     background-color: #3e8e41; */
    /* } */

    .link {
        height: 19px;
        display: flex;
        color: black;
        padding-left: 4px;
        text-decoration: none;
        display: block;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    /* search field */
    #searchInput {
        height: 22px;
        width: 100%;
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        cursor: pointer;
        padding: 1px 4px;
        border: none;
        background-color: #ccc6b7;
        /* box-shadow: 1px 1px 0 0 #7a776e inset, -1px -1px 0 0 #ffffff inset; */
        border-color: #7a776e #fff #fff #7a776e;
        border-style: inset;
        border-width: 1px;
    }

    #searchInput:hover,
    .link:hover {
        background-color: #e5dac3;
    }

    #searchInput:focus,
    .link:focus,
    .list-content:focus {
        outline: none;
    }

    .list-content {
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        height: 0;
        margin-top: 4px;
        background-color: #ccc6b7;
        overflow-x: hidden;
        overflow-y: auto;
        scrollbar-width: none;
        border-color: #7a776e #fff #fff #7a776e;
        border-style: inset;
        border-width: 1px;
    }

    /* show dropdown menu */
    .show {
        display: block;
    }
</style>
