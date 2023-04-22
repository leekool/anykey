<script lang="ts">
    // let menuOpen: boolean;
    let inputValue: string = "";
    let inputEl: HTMLElement;

    export let selectedItem: any;
    export let menuItems: { name: string; path: string }[] = [];
    let filteredItems: { name: string; path: string }[] = [];

    const handleClick = (item: { name: string; path: string }) => {
        // menuOpen = !menuOpen;
        selectedItem = item;
        console.log(selectedItem);
    };

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.name.toLowerCase().match(inputValue.toLowerCase())
        ));
    };
</script>

<div class="main">
    <!-- <div -->
    <!--     class="select-keyboard" -->
    <!--     on:click={() => inputEl.focus()} -->
    <!--     on:keypress={(e) => console.log(e)} -->
    <!-- > -->
    <!--     <button on:click={() => (menuOpen = !menuOpen)} class="dropbtn"> -->
    <!--         {!menuOpen ? "keyboard menu ▼" : "close menu ▲"} -->
    <!--     </button> -->
    <!-- </div> -->
    <!-- <div class:show={menuOpen} class="dropdown-content"> -->
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
        width: 163px;
        height: 105px;
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
        color: black;
        padding-left: 4px;
        text-decoration: none;
        display: block;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
        background-color: #ccc6b7;
    }

    /* search field */
    #searchInput {
        width: 100%;
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        cursor: pointer;
        padding: 1px 4px;
        border: none;
        background-color: #ccc6b7;
        /* box-shadow: 1px 1px 0 0 #7a776e inset, -1px -1px 0 0 #ffffff inset; */
        border-left: 1px inset #7a776e;
        border-top: 1px inset #7a776e;
        border-right: 1px inset #fff;
        border-bottom: 1px inset #fff;
    }

    #searchInput:focus,
    #searchInput:hover,
    .link:hover {
        background-color: #e5dac3;
        outline: none;
    }

    .list-content {
        margin-top: 4px;
        background-color: #ccc6b7;
        overflow-x: hidden;
        overflow-y: scroll;
        height: 100%;
        border-left: 1px inset #7a776e;
        border-top: 1px inset #7a776e;
        border-right: 1px inset #fff;
        border-bottom: 1px inset #fff;
    }

    /* show dropdown menu */
    .show {
        display: block;
    }
</style>
