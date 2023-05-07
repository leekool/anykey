<script lang="ts">
    export let selectedItem: any;
    export let menuItems: { name: string; path: string }[] = [];

    let inputEl: HTMLElement;
    let inputValue: string = "";
    let filteredItems: { name: string; path: string }[] = [];

    const handleClick = (item: { name: string; path: string }) =>
        (selectedItem = item);

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.name.toLowerCase().match(inputValue.toLowerCase())
        ));
    };

    const handleKey = (event: KeyboardEvent) => {
        if (event.code !== "Enter") return;

        const matchedItem = menuItems.find((item) => item.name.toLowerCase() === inputValue.toLowerCase());

        if (matchedItem) selectedItem = matchedItem;
    };
</script>

<div class="main">
    <fieldset>
        <legend>Keyboard</legend>
        <input
            style="line-height: 20px;"
            class="search-input pixel-corners--wrapper"
            type="text"
            placeholder="filter..."
            autocomplete="off"
            bind:this={inputEl}
            bind:value={inputValue}
            on:input={handleInput}
            on:keyup={handleKey}
        />
        <div class="list-container pixel-corners">
            <div class="list-spacer" />
            <div class="list-content">
                {#if filteredItems.length > 0}
                    {#each filteredItems as item}
                        <div
                            class={item.name == selectedItem.name
                                ? "link link-selected"
                                : "link"}
                            on:click={() => handleClick(item)}
                        >
                            {item.name}
                        </div>
                    {/each}
                {:else}
                    {#each menuItems as item}
                        <div
                            class={item.name == selectedItem.name
                                ? "link link-selected"
                                : "link"}
                            on:click={() => handleClick(item)}
                        >
                            {item.name}
                        </div>
                    {/each}
                {/if}
            </div>
            <div class="list-spacer" />
        </div>
    </fieldset>
</div>

<style>
    @import url("../../static/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .main {
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        min-height: 200px;
        height: 100%;
        width: 100%;
    }

    fieldset {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border: 2px solid #000;
        font-weight: 800;
        margin: 6px 10px 10px 10px;
        height: 100%;
    }

    legend {
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .list-container {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
        height: 100%;
        margin-top: 6px;
        background-color: #e0e0e0;
    }

    .list-content {
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        height: 0;
        overflow-x: hidden;
        overflow-y: auto;
        scrollbar-width: none;
    }

    .list-spacer {
        display: flex;
        width: 100%;
        min-height: 2px;
    }

    .link {
        display: flex;
        height: 19px;
        /* width: 100%; */
        padding: 0 8px;
        color: #000;
        text-decoration: none;
        display: block;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    /* search field */
    .search-input {
        display: flex;
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        cursor: pointer;
        padding: 2px 8px;
        background-color: #e0e0e0;
        border: 2px solid #000;
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    /* .box-outset{ */
    /*     border-width: 0.5rem; */
    /*     border-color: green; */
    /*     border-style: outset; */
    /*     outline: 0.5rem outset khaki; */
    /*     background-color: brown; */
    /* } */

    .search-input:hover {
        background-color: #ebebeb;
        box-shadow: none;
    }

    .link:hover {
        background-color: #ebebeb;
        box-shadow: 2px 0 0 0 #c2c2c2 inset, -2px 0 0 0 #f5f5f5 inset,
            0 -2px 0 0 #ebebeb inset, 0 2px 0 0 #ebebeb inset;
    }

    .link-selected {
        background-color: #ebebeb;
        box-shadow: 2px 0 0 0 #c2c2c2 inset, -2px 0 0 0 #f5f5f5 inset,
            0 -2px 0 0 #ebebeb inset, 0 2px 0 0 #ebebeb inset;
        background-image: url("images/keyboard-tile.svg");
    }

    .search-input:focus,
    .link:focus,
    .list-content:focus {
        outline: none;
    }

    /* show dropdown menu */
    .show {
        display: block;
    }
</style>
