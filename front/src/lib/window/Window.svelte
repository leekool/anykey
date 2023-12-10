<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import { get_current_component } from "svelte/internal";
    import {
        windowStore,
        Window,
        type Options,
        type Position
    } from "./WindowStore";
    import Navbar from "$lib/window/Navbar.svelte";
    import Footer from "$lib/window/Footer.svelte";

    $: $windowStore, window_ = window_; // trigger state management

    export let name: string;
    export let options: Partial<Options> = {};
    export let position: Partial<Position> = {}
    export let slot: {
        component: any,
        props: any
    } = {
        component: null,
        props: null
    };

    let window_ = new Window(name, get_current_component(), options, position);
    let element: HTMLElement;

    const getPosition = (): void => {
        const getSize = (e: HTMLElement): Partial<Position> => {
            const { height, width } = e.getBoundingClientRect();
            return { 
                height, 
                width, 
                top: (window_.position.topPercent / 100) * window.innerHeight,
                left: (window_.position.leftPercent / 100) * window.innerWidth
            };
        }

        window_.position = Object.assign({}, window_.position, getSize(element));

        if ($windowStore.length <= 2) return;

        const offset = 20;

        const index = $windowStore.slice(0, -1).findLastIndex(w => w.options.type === window_.options.type);

        const prevPos = $windowStore[index].position;

        window_.position.top = prevPos.top + (window_.position.height - prevPos.height) / 2 + offset;
        window_.position.left = prevPos.left + (window_.position.width - prevPos.width) / 2 + offset;

        getTopLeftPercent();
    };

    const getTopLeftPercent = (): void => {
        window_.position.topPercent = (window_.position.top / window.innerHeight) * 100;
        window_.position.leftPercent = (window_.position.left / window.innerWidth) * 100;
    }

    const windowClick = () => {
        if (window_.options.focused || window_.options.minimised) return;

        window_.getFocus();

        $windowStore = $windowStore;
    };

    const clickNavbar = (): void => {
        // if (!window_.options.focusEle) return;
        // window_.options.focusEle.focus();
    }

    // --- draggable navbar functions for mouse events ---
    let moving = false;

    const dragMouseDown = () => { 
        moving = true; 
        windowClick(); 
    };

    const dragMouseUp = () => {
        moving = false;
    }

    const dragMouseMove = (e: MouseEvent) => {
        if (!moving) return;

        window_.position.top += e.movementY;
        window_.position.left += e.movementX;

        getTopLeftPercent();
    };

    // --- draggable navbar functions for touch events ---
    let movingTouch: Touch | null = null;

    const dragTouchStart = (e: TouchEvent) => {
        moving = true;
        movingTouch = e.touches[0];

        windowClick();
    }

    const dragTouchEnd = () => {
        moving = false;
        movingTouch = null;
    }

    const dragTouchMove = (e: TouchEvent) => {
        if (!moving) return;

        const initialTouch = movingTouch;

        if (initialTouch) {
            window_.position.top += e.touches[0].clientY - initialTouch.clientY;
            window_.position.left += e.touches[0].clientX - initialTouch.clientX;
    
            getTopLeftPercent();
        }

        movingTouch = e.touches[0];
    }

    // -----

    onMount(async () => {
        getPosition();

        window.addEventListener("resize", () => getTopLeftPercent());
    });

    onDestroy(() => {
        console.log("destroyed: ", window_);
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    bind:this={element}
    class={"window-" + window_.options.type}
    class:minimised={window_.options.minimised}
    class:maximised={window_.options.maximised}
    class:draggable={!window_.options.maximised}
    style="z-index: {window_.zIndex}; left: {window_.position.leftPercent}%; top: {window_.position.topPercent}%;"
    on:click={() => windowClick()}
>
    <div class="main pixel-corners">
        <div 
            class="drag-bar" 
            on:mousedown={dragMouseDown}
            on:touchstart|preventDefault={dragTouchStart}
            on:click={() => clickNavbar()}
        />
        <Navbar {window_} />

        <div class="content">
            <svelte:component this={slot.component} {...slot.props} />
        </div>

        <Footer {window_} />
    </div>
</div>

<svelte:window 
    on:mouseup={dragMouseUp} 
    on:touchend={dragTouchEnd}
    on:mousemove={dragMouseMove} 
    on:touchmove|preventDefault={dragTouchMove}
/>

<style>
    @import url("/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .main {
        display: flex;
        flex: 1 0 auto;
        flex-direction: column;
        background-color: #d5d5d5;
        min-height: 100%;
        max-width: calc(100% - 4px); /* 4px to account for pixel-corners */
    }

    .minimised {
        display: none;
        visibility: hidden;
        z-index: 0 !important;
    }

    .maximised {
        position: absolute;
        width: 100% !important;
        max-width: 100% !important;
        height: calc(100% - 38px) !important;
        max-height: calc(100% - 38px) !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
    }

    /* .focused { */
    /*     z-index: 100 !important; */
    /* } */

    .content {
        display: flex;
        flex: 1 1 auto;
        width: 100%;
        /* max-width: 100%; */
        align-self: center;
        flex-direction: column;
        background-color: #d5d5d5;
        margin: 2px 4px;
        overflow: scroll;
    }

    .window-main {
        display: flex;
        flex: 1 0 auto;
        position: absolute;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        min-width: 438px;
        max-width: 438px;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
    }

    .window-keymap {
        display: flex;
        flex: 1 0 auto;
        position: absolute;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        /* min-width: 80%; */
        max-height: 80%;
    }

    .draggable {
        position: absolute;
        pointer-events: none;
    }

    .draggable > * {
        pointer-events: auto;
    }

    .drag-bar {
        position: absolute;
        width: 100%;
        height: 34px;
    }

    @media screen and (max-width: 700px) {
        .window-main {
            min-width: 80%;
            max-width: 80%;
        }

        .window-keymap {
            min-width: 95%;
            max-width: 95%;
        }
    }
</style>
