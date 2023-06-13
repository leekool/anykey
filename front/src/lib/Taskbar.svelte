<script lang="ts">
    import { windowStore } from "./stores";
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="taskbar">
    <div class="iconman">
        {#each $windowStore as window}
            <div
                class="iconman-button"
                class:active={!window.minimised}
                on:click={() => {
                    window.taskbarClk();
                    window = window; // tells svelte object changed
                }}
            >
                <img src={"images/" + window.icon} alt={window.name} />
                <span>{window.name}</span>
            </div>
        {/each}
    </div>
</div>

<style>
    .taskbar {
        display: flex;
        position: fixed;
        height: 34px;
        width: 100%;
        justify-content: space-between;
        left: 50%;
        bottom: 0;
        margin-left: -50%;
        font-family: "Tamzen", sans-serif;
        font-size: 16px;
        font-weight: bold;
        color: #222020;
        background-image: url("images/footer-tile.svg");
        background-repeat: repeat;
        border-top: 2px solid #222020;
        box-shadow: 2px 2px #fff inset, -2px -2px #a0a0a0 inset;
        z-index: 10;
    }

    .taskbar span {
        margin-top: 3px;
    }

    .iconman {
        display: flex;
        width: 100%;
        box-sizing: border-box;
        box-shadow: -2px -2px #a0a0a0 inset, 2px 2px #fff inset;
    }

    .iconman-button {
        display: flex;
        align-items: center;
        width: 250px;
        margin: 4px 0 5px 5px;
        cursor: pointer;
        user-select: none;
    }

    .iconman-button img {
        /* max-height: 32px; */
        margin: 8px;
        image-rendering: pixelated;
    }

    /* .inactive { */
    /*     color: #000; */
    /*     background-image: none; */
    /*     box-shadow: none; */
    /* } */

    .active {
        color: #fff;
        background-image: url("images/iconman-tile.svg");
        /* background-size: 8%; */
        background-color: #aaa;
        box-shadow: -2px -2px #ccccff inset, 2px 2px #9c9cd3 inset;
    }

    @media screen and (max-width: 700px) {
        .iconman {
            padding-right: 5px;
            overflow-y: hidden;
            overflow-x: scroll;
            -ms-overflow-style: none;
            scrollbar-width: none;
        }

        .iconman::-webkit-scrollbar {
            display: none;
        }

        .iconman-button {
            width: 130px;
        }
    }
</style>
