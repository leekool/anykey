<script lang="ts">
    import { onMount } from "svelte";
    import { windowStore, createWindow, type Window, type Options } from "./WindowStore";
    import Navbar from "./Navbar.svelte";
    import Footer from "./Footer.svelte";

    export let name: string;
    export let focused: boolean = true;
    export let minimised: boolean = false;
    export let position: string = "position-main";
    export let options: Options; 

    let window: Window = createWindow(name, focused, minimised, options);

    /* trigger svelte state management
       i hate how we have to do this */
    $: $windowStore, window = window;

    const windowClick = () => {
        if (window.focused || window.minimised) return;

        window.getFocus($windowStore);

        $windowStore = $windowStore;
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
    on:click={() => windowClick()}
>
    <div class="main pixel-corners">
        <Navbar {window} />

        <div class="content">
            <slot />
        </div>

        <Footer {window} />
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
</style>
