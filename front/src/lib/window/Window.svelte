<script lang="ts">
    import { onMount } from "svelte";
    import { windowStore, createWindow, Window } from "./WindowStore";
    import Navbar from "./Navbar.svelte";

    export let name: string;
    export let focused: boolean = true;
    export let minimised: boolean = false;
    export let position: string = "position-main";

    let window: Window = createWindow(name, focused, minimised);

    $: $windowStore, checkWindows();

    /* trigger svelte state management
       i hate how we have to do this */
    const checkWindows = () => {
        window = window;
        console.log($windowStore);
    };

    onMount(async () => {
        for (let window of $windowStore) {
            if (window.name == name) window.getFocus($windowStore);
        }

        $windowStore = $windowStore; // trigger svelte state management
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    class={position}
    class:minimised={window.minimised}
    class:focused={window.focused}
    class:inactive={!window.focused}
    on:click={() => {
        if (window.focused || window.minimised) return;
        window.getFocus($windowStore);
        $windowStore = $windowStore;
    }}
>
    <div class="main pixel-corners">
        <Navbar window={window}></Navbar>

        <div class="content">
            <slot />
        </div>

        <div class="footer">
            <div class="footer-btn-container">
                <div class="footer-btn">
                    <div class="left-arrow" />
                </div>
                <div class="separator" />
                <div class="footer-scroll-btn">
                    <div class="scroll-img" />
                </div>
            </div>
            <div class="footer-bg" />
            <div class="separator" />
            <div class="footer-btn">
                <div class="right-arrow" />
            </div>
        </div>
    </div>
</div>

<style>
    @import url("../../../static/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .main {
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        font-family: "Tamzen", sans-serif;
        background-color: #d5d5d5;
    }

    .minimised {
        display: none;
        visibility: hidden;
        z-index: 0;
    }

    .focused {
        z-index: 10;
    }

    .content {
        display: flex;
        flex: 1 1 auto;
        align-self: center;
        flex-direction: column;
        background-color: #d5d5d5;
        margin: 2px 4px;
        width: 100%;
        overflow: scroll;
    }

    .footer {
        display: flex;
        justify-items: space-between;
        box-sizing: border-box;
        min-height: 24px;
        user-select: none;
        box-shadow: 0 -2px 0 0 #000, 0 -4px 0 0 #a3a3d7;
    }

    .footer-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        align-items: center;
        justify-content: center;
        background-color: #d5d5d5;
        box-sizing: border-box;
        border-color: #fff #a0a0a0 #a0a0a0 #fff;
        border-style: solid;
        border-width: 2px;
    }

    .footer-btn-container {
        display: flex;
        aspect-ratio: 2 / 1;
        box-sizing: border-box;
        /* justify-content: center; */
    }

    .footer-scroll-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
        background-color: #aaaaaa;
        border-color: #ccccff #333366 #333366 #ccccff;
        border-style: solid;
        border-width: 2px;
        z-index: 10;
    }

    .footer-bg {
        height: calc(100% - 2px);
        width: 100%;
        background-image: url("images/footer-tile.svg");
    }

    .separator {
        background-color: #000;
        min-width: 2px;
        z-index: 10;
    }

    .position-main {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        width: 80%;
        max-width: 500px;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
    }

    .position-layout {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        max-height: 80%;
    }

    .scroll-img {
        display: flex;
        height: 70%;
        width: 70%;
        content: url("images/footer-scroll.svg");
        border-left: 1px solid #a3a3d7;
        margin-right: 1px;
    }

    .left-arrow {
        display: flex;
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        /* filter: saturate(0%) brightness(100%) contrast(80%); */
    }

    .right-arrow {
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        transform: rotate(180deg);
    }

    .inactive .footer {
        box-shadow: 0 -2px 0 0 #000, 0 -4px 0 0 #a7a7a7;
    }

    .inactive .left-arrow,
    .inactive .right-arrow,
    .inactive .scroll-img {
        filter: saturate(0%) brightness(100%) contrast(80%);
    }

    .inactive .footer-scroll-btn {
        border-color: #d0d0d0 #454545 #454545 #d0d0d0;
    }
</style>
