<script lang="ts">
    import { onMount, onDestroy } from "svelte";
    import { get_current_component } from "svelte/internal";
    import {
        windowStore,
        Window,
        type Options,
        type Position
    } from "./WindowStore";
    import Navbar from "./Navbar.svelte";
    import Footer from "./Footer.svelte";

    $: $windowStore, window_ = window_; // trigger state management

    export let name: string;
    export let options: Partial<Options> = {};

    let window_ = new Window(name, get_current_component(), options);
    let element: HTMLElement;

    const getPosition = (): void => {
        const getSize = (e: HTMLElement): Partial<Position> => {
            const { height, width } = e.getBoundingClientRect();
            return { height, width, top: window.innerHeight / 2, left: window.innerWidth / 2 };
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

    // draggable navbar functions
    let moving = false;

    const dragMouseDown = () => { moving = true; windowClick(); };
    const dragMouseUp = () => moving = false;

    const dragMouseMove = (e: MouseEvent) => {
        if (!moving) return;

        window_.position.top += e.movementY;
        window_.position.left += e.movementX;

        getTopLeftPercent();
    };
    // -----

    onMount(async () => {
        getPosition();

        window.addEventListener("resize", () => getTopLeftPercent());
    });

    onDestroy( () => {
        console.log("destroyed: ", window_);
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    bind:this={element}
    class={window_.options.type}
    class:minimised={window_.options.minimised}
    class:maximised={window_.options.maximised}
    class:draggable={!window_.options.maximised}
    style="z-index: {window_.zIndex}; left: {window_.position.leftPercent}%; top: {window_.position.topPercent}%;"
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
        z-index: 0 !important;
    }

    .maximised {
        position: absolute;
        width: 100%;
        height: calc(100% - 38px);
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
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        max-width: 438px;
        width: 80%;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
    }

    .window-layout {
        display: flex;
        flex: 1 0 auto;
        position: absolute;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        max-height: 80%;
    }

    .draggable {
        position: absolute;
        pointer-events: none;
    }

    .draggable > * {
        pointer-events: auto;
    }
</style>
