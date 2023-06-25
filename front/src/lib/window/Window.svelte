<script lang="ts">
    import { onMount } from "svelte";
    import { windowStore, createWindow, type Window, type Options } from "./WindowStore";
    import Navbar from "./Navbar.svelte";
    import Footer from "./Footer.svelte";

    export let name: string;
    export let options: Options = {}; 
    let windowDomRect: any;

    let window: Window = createWindow(name, options);

    /* todo: because top/left move the window based on the centre of the page,
             windows of different sizes knock the stagger out of alignment.
             it needs to find the top & left borders of the previous window and
             base the next one's position off of that instead. */
    const offset: number = 50 + (window.options.type === 'window-main' ? 0 : (window.id - 1) * 3);
    const offsetStyle: string = `top: ${offset}%; left: ${offset}%;`;

    /* trigger svelte state management
       i hate how we have to do this */
    $: $windowStore, window = window//, console.log(window);

    const windowClick = () => {
        if (window.options.focused || window.options.minimised) return;

        window.getFocus($windowStore);

        $windowStore = $windowStore;
    };

    onMount(async () => {
        for (let window of $windowStore) {
            if (window.name == name) window.getFocus($windowStore);
        }
        
        // windowDomRect = windowDomRect.getBoundingClientRect();
        // console.log(windowDomRect)

        $windowStore = $windowStore; // trigger svelte state management
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    bind:this={windowDomRect}
    
    class={window.options.type}
    class:minimised={window.options.minimised}
    class:maximised={window.options.maximised}
    class:focused={window.options.focused}
    class:inactive={!window.options.focused}
    
    style={offsetStyle}

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
        min-height: 100%;
    }

    .minimised {
        display: none;
        visibility: hidden;
        z-index: 0;
    }

    .maximised {
        position: absolute;
        width: 100%;
        height: calc(100% - 38px);
        max-height: calc(100% - 38px) !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
        z-index: 1 !important;
    }

    .focused {
        z-index: 10 !important;
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

    .window-main {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        /* top: 50%; */
        /* left: 50%; */
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        width: 80%;
        max-width: 500px;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        z-index: 5;
    }

    .window-layout {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        /* top: 50%; */
        /* left: 50%; */
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        max-height: 80%;
        z-index: 5;
    }
</style>
