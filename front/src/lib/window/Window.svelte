<script lang="ts">
    import { onMount } from "svelte";
    import {
        windowStore,
        createWindow,
        type Window,
        type Options,
    } from "./WindowStore";
    import Navbar from "./Navbar.svelte";
    import Footer from "./Footer.svelte";

    export let name: string;
    export let options: Options = {};

    let windowElement: Node;
    let window_: Window = createWindow(name, options);

    const getOffsetStyle = (): string | void => {
        const windowRect: any = (windowElement as HTMLElement).getBoundingClientRect();
        const index = $windowStore.findIndex(w => w.id === window_.id);

        // deep copy windowRect, maybe lodash time
        window_.position = {
            x: windowRect.x,
            y: windowRect.y,
            width: windowRect.width,
            height: windowRect.height,
            // top: windowRect.top,
            // left: windowRect.left
            top: window.innerHeight / 2,
            left: window.innerWidth / 2
        };

        if (index < 2) return; 

        const prevPos = $windowStore[index - 1].position as DOMRect;

        window_.position.top = prevPos.top + (window_.position.height! - prevPos.height) / 2 + 20;
        window_.position.left = prevPos.left + (window_.position.width! - prevPos.width) / 2 + 20;

        dragTop = (window_.position.top / window.innerHeight) * 100;
        dragLeft = (window_.position.left / window.innerWidth) * 100;
    };

    const windowClick = () => {
        if (window_.options.focused || window_.options.minimised) return;

        window_.getFocus($windowStore);

        $windowStore = $windowStore;
    };

    // draggable navbar functions
    let dragTop = 50, dragLeft = 50 // start centred;
    let moving = false;

    const dragMouseDown = () => {
        moving = true;
        windowClick();
    };

    const dragMouseUp = () => moving = false;

    const dragMouseMove = (e: MouseEvent) => {
        if (moving) {
            dragTop = ((window_.position!.top! += e.movementY) / window.innerHeight) * 100;
            dragLeft = ((window_.position!.left! += e.movementX) / window.innerWidth) * 100;
        }
    };
    // -----

    onMount(async () => {
        window_.element = windowElement;

        getOffsetStyle();

        for (let window of $windowStore) {
            if (window_.name === name) window.getFocus($windowStore);
        }

        $windowStore = $windowStore; // trigger svelte state management
    });

    /* trigger svelte state management
       there has to be a way to not have to do this */
    $: $windowStore, window_ = window_;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    bind:this={windowElement}
    class={window_.options.type}
    class:minimised={window_.options.minimised}
    class:maximised={window_.options.maximised}
    class:draggable={!window_.options.maximised}
    class:focused={window_.options.focused}
    style="left: {dragLeft}%; top: {dragTop}%;"
    on:click={() => windowClick()}
>
    <div class="main pixel-corners">
        <div on:mousedown={dragMouseDown}>
            <Navbar {window_} />
        </div>

        <div class="content">
            <slot />
        </div>

        <Footer {window_} />
    </div>
</div>

<svelte:window on:mouseup={dragMouseUp} on:mousemove={dragMouseMove} />

<style>
    @import url("../../../static/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .main {
        display: flex;
        flex: 1 0 auto;
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
        z-index: 9 !important;
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
        flex: 1 0 auto;
        position: absolute;
        /* top: 50%; */
        /* left: 50%; */
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        max-width: 438px;
        width: 80%;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        z-index: 5;
    }

    .window-layout {
        display: flex;
        flex: 1 0 auto;
        position: absolute;
        /* top: 50%; */
        /* left: 50%; */
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        max-height: 80%;
        z-index: 5;
    }

    .draggable {
        position: absolute;
        /* height: 100%; */
        /* width: 100%; */
        /* top: 50%; */
        /* left: 50%; */
        /* -ms-transform: translate(-50%, -50%); */
        /* transform: translate(-50%, -50%); */
        pointer-events: none;
    }

    .draggable > * {
        pointer-events: auto;
    }
</style>
