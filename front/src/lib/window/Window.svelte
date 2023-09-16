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
    let windowElement: HTMLElement;

    let window_: Window = createWindow(name, options);

    // it's not ideal that this depends on window_.id
    const getOffsetStyle = (): string => {
        const windowRect: any = windowElement.getBoundingClientRect();

        // deep copy windowRect
        window_.position = {
            x: windowRect.x,
            y: windowRect.y,
            width: windowRect.width,
            height: windowRect.height,
            top: windowRect.top,
            left: windowRect.left,
        };

        if (window_.id <= 1) {
            window_.position.top = window.innerHeight / 2;
            window_.position.left = window.innerWidth / 2;
            return `top: 50%; left: 50%;`;
        }

        const prevPos = $windowStore[window_.id - 1].position as DOMRect;

        window_.position.top =
            prevPos.top + (window_.position.height! - prevPos.height) / 2 + 20;
        window_.position.left =
            prevPos.left + (window_.position.width! - prevPos.width) / 2 + 20;

        const top = window_.position.top - window.innerHeight / 2;
        const left = window_.position.left - window.innerWidth / 2;

        return `top: calc(50% + ${top}px); left: calc(50% + ${left}px);`;
    };

    let offsetStyle: string = "top: 50%; left: 50%;";

    /* trigger svelte state management
       i hate how we have to do this */
    $: $windowStore, (window_ = window_);

    const windowClick = () => {
        if (window_.options.focused || window_.options.minimised) return;

        window_.getFocus($windowStore);

        $windowStore = $windowStore;
    };

    onMount(async () => {
        for (let window of $windowStore) {
            if (window_.name == name) window.getFocus($windowStore);
        }

        offsetStyle = getOffsetStyle();

        $windowStore = $windowStore; // trigger svelte state management
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
    bind:this={windowElement}
    class={window_.options.type}
    class:minimised={window_.options.minimised}
    class:maximised={window_.options.maximised}
    class:focused={window_.options.focused}
    class:inactive={!window_.options.focused}
    style={offsetStyle}
    on:click={() => windowClick()}
>
    <div class="main pixel-corners">
        <Navbar {window_} />

        <div class="content">
            <slot />
        </div>

        <Footer {window_} />
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
