<script lang="ts">
    export let selectedItem: any;
    export let menuItems: string[] = [];

    let inputEl: HTMLElement;
    let inputValue: string = "";
    let filteredItems: string[] = [];

    const handleClick = (item: string) =>
        (selectedItem = item);

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.toLowerCase().match(inputValue.toLowerCase())
        ));
    };

    const handleKey = (event: KeyboardEvent) => {
        if (event.code !== "Enter") return;

        const matchedItem = menuItems.find(
            (item) => item.toLowerCase() === inputValue.toLowerCase()
        );

        matchedItem
            ? (selectedItem = matchedItem)
            : (selectedItem =
                  filteredItems.length > 0 ? filteredItems[0] : null);
    };
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
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
                            class={item == selectedItem
                                ? "link link-selected"
                                : "link"}
                            on:click={() => handleClick(item)}
                        >
                            {item}
                        </div>
                    {/each}
                {:else}
                    {#each menuItems as item}
                        <div
                            class={item == selectedItem
                                ? "link link-selected"
                                : "link"}
                            on:click={() => handleClick(item)}
                        >
                            {item}
                        </div>
                    {/each}
                {/if}
            </div>
            <div class="list-spacer" />
        </div>
    </fieldset>
</div>

<style>
    @import url("/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .main {
        display: flex;
        /* flex: 1 1 auto; */
        flex-direction: column;
        min-height: 200px;
        height: 100%;
        width: 100%;
        max-width: 100%;
    }

    fieldset {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border: 2px solid #000;
        font-weight: 800;
        margin: 6px 10px 10px 10px;
        height: 100%;
        min-width: 0 !important; /* overwrite weird browser default */
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
        height: 100%;
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
        margin-top: 6px;
        background-color: #e0e0e0;
    }

    .list-content {
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        height: 0;
        width: 100%;
        max-width: 100%;
        overflow-x: hidden;
        overflow-y: auto;
        white-space: nowrap;
        text-overflow: ellipsis;
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
        max-width: 100%;
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
        background-image: url("/images/keyboard-tile.svg");
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

    @media screen and (max-width: 700px) {
        /* fieldset { */
        /*     max-width: 200px; */
        /* } */
    }
</style>
