<script lang="ts">
    let menuOpen: boolean;
    let inputValue: string = "";
    let inputEl: HTMLElement;

    export let selectedItem: any;
    export let menuItems: { name: string; path: string }[] = [];
    let filteredItems: { name: string; path: string }[] = [];

    const handleClick = (item: { name: string; path: string }) => {
        menuOpen = !menuOpen;
        selectedItem = item;
        console.log(selectedItem);
    }

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.name.toLowerCase().match(inputValue.toLowerCase())
        ));
    }
</script>

<div>
    <div
        class="select-keyboard"
        on:click={() => inputEl.focus()}
        on:keypress={(e) => console.log(e)}
    >
        <button on:click={() => (menuOpen = !menuOpen)} class="dropbtn">
            {!menuOpen ? "keyboard menu ▼" : "close menu ▲"}
        </button>
    </div>
    <div class:show={menuOpen} class="dropdown-content">
        <input
            id="searchInput"
            type="text"
            placeholder="Search..."
            autocomplete="off"
            bind:this={inputEl}
            bind:value={inputValue}
            on:input={handleInput}
        />
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

    .dropbtn {
        font-family: "Tamzen", sans-serif;
        background-color: brown;
        color: white;
        font-size: 15px;
        cursor: pointer;
        border: 1px solid #ccc;
        padding: 3px 6px;
    }

    .dropbtn:hover,
    .dropbtn:focus {
        background-color: #3e8e41;
    }

    .link {
        color: black;
        padding: 1px 6px;
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

    /* search field */
    #searchInput {
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        cursor: pointer;
        padding: 1px 6px;
        border: none;
        border-bottom: 1px solid #ddd;
    }

    #searchInput:focus {
        /* outline: 3px solid #ddd; */
        outline: none;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f6f6f6;
        /* min-width: 230px; */
        border: 1px solid #ddd;
        z-index: 10;
    }

    /* show dropdown menu */
    .show {
        display: block;
    }
</style>
