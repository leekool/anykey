<script lang="ts">
    import Layout from "../../routes/+layout.svelte";
    import Page from "../../routes/+page.svelte";
    import { Window, windowStore } from "./WindowStore";

    export let window_: Window;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="navbar" class:inactive={!window_.options.focused}>
    <div class="navbar-title">{window_.name}</div>

    <div class="navbar-bg" style="width: 14px;" />

    <!-- info button -->
    {#if window_.options.navbarInfo}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner navbar-btn-left"
                on:click={() => {
                    window_.screenshotCanvas(window_.content);
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <div class="navbar-bg" />

    <!-- maximise button (left) -->
    {#if window_.options.navbarMaximise}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner"
                on:click={() => {
                    window_.toggleMaximise();
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <!-- minimise button (right) -->
    {#if window_.options.navbarMinimise}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner navbar-btn-right"
                on:click={() => {
                    window_.toggleMinimise($windowStore);
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <div class="navbar-bg" style="width: 14px;" />
</div>

<style>
    .navbar {
        display: flex;
        height: 34px;
        font-size: 16px;
        align-items: center;
        justify-content: space-between;
        user-select: none;
        border-color: #ccccff #a3a3d7 #a3a3d7 #ccccff;
        border-style: solid;
        border-width: 2px;
        box-sizing: border-box;
        box-shadow: 0 2px 0 0 #000;
        padding-bottom: 1px;
    }

    .navbar-bg {
        box-shadow: 0 2px 0 0 #a4a4a4 inset, 0 4px 0 0 #d5d5d5 inset,
            0 6px 0 0 #a4a4a4 inset, 0 8px 0 0 #d5d5d5 inset,
            0 10px 0 0 #a4a4a4 inset, 0 12px 0 0 #d5d5d5 inset,
            0 14px 0 0 #a4a4a4 inset, 0 16px 0 0 #d5d5d5 inset,
            0 18px 0 0 #a4a4a4 inset, 0 20px 0 0 #d5d5d5 inset,
            0 22px 0 0 #a4a4a4 inset;
        width: 100%;
        height: 22px;
    }

    .navbar-title {
        position: absolute;
        height: 30px;
        line-height: 30px;
        padding: 0 12px;
        left: 50%;
        transform: translate(-50%);
        font-weight: bold;
        color: #000;
        background-color: #d5d5d5;
        text-shadow: 0 1px rgba(138, 134, 160, 0.7);
    }

    .navbar-btn-base {
        display: flex;
        height: 22px;
        aspect-ratio: 1 / 1;
        margin: 4px;
        align-items: center;
        justify-content: center;
        background-color: #ccccff;
        box-shadow: 2px 2px 0 0 #333366 inset;
        cursor: pointer;
    }

    .navbar-btn-inner {
        display: flex;
        height: 16px;
        aspect-ratio: 1 /1;
        margin-left: 2px;
        margin-top: 2px;
        background-color: #a4a4a4;
        box-shadow: -2px -2px 0 0 #333366 inset;
    }

    .navbar-btn-inner:hover {
        box-shadow: 2px 2px 0 0 #333366 inset;
    }

    .navbar-btn-right {
        box-shadow: -2px -2px 0 0 #333366 inset, -6px -6px 0 0 #a4a4a4 inset,
            -8px -8px 0 0 #333366 inset;
    }

    /* .navbar-btn-left { */
    /*     display: flex; */
    /*     height: 80%; */
    /*     width: 80%; */
    /*     content: url("images/left-arrow.svg"); */
    /*     transform: rotate(270deg); */
    /* } */

    .inactive {
        border-color: #d0d0d0 #a7a7a7 #a7a7a7 #d0d0d0;
    }

    .inactive .navbar-btn-base {
        background-color: #d0d0d0;
        box-shadow: 2px 2px 0 0 #454545 inset;
    }

    .inactive .navbar-btn-inner {
        box-shadow: -2px -2px 0 0 #454545 inset;
    }

    .inactive .navbar-btn-right {
        box-shadow: -2px -2px 0 0 #454545 inset, -6px -6px 0 0 #a4a4a4 inset,
            -8px -8px 0 0 #454545 inset;
    }
</style>
