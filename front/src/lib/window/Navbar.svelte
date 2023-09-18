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
            <!-- <div -->
            <!--     class="navbar-btn-inner navbar-btn-left" -->
            <!--     on:click={() => { -->
            <!--         window_.screenshotCanvas(window_.options.layoutInfo?.svg || ""); -->
            <!--         $windowStore = $windowStore; // tells svelte object changed -->
            <!--     }} -->
            <!-- /> -->
            <div
                class="navbar-btn-inner info-btn"
                on:click|self={() => console.log("window info: ", window_)}
            >
                {#if window_.options.focused}
                    <div class="info">
                        {#if window_.options.type?.includes("layout")}
                            <div>{window_.options.layoutInfo?.name}</div>
                            <div>{window_.options.layoutInfo?.fileName}</div>
                            <div>{window_.options.layoutInfo?.fileSize}</div>
                            <div>{window_.options.layoutInfo?.filePath}</div>
                            <div
                                class="download-btn"
                                on:click={() => {
                                    console.log("TEST");
                                    window_.screenshotCanvas(window_.options.layoutInfo?.svg || "");
                                }}
                            >
                                download
                            </div>
                        {/if}
                    </div>
                {/if}
            </div>
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
                class="navbar-btn-inner minimise-btn"
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

    .minimise-btn {
        box-shadow: -2px -2px 0 0 #333366 inset, -6px -6px 0 0 #a4a4a4 inset,
            -8px -8px 0 0 #333366 inset;
    }

    .info-btn:hover .info {
        display: block;
    }

    .info-btn:after {
        content: "i";
        position: relative;
        transform: translate(-50%, -50%);
        left: 50%;
        top: 8px;
        color: #333366;
        font-weight: bold;
        font-size: 14px;
        text-shadow: 0 1px #f5f5f5, 0 2px rgba(138, 134, 160, 0.7);
    }

    .info {
        display: none;
        position: absolute;
        padding: 5px;
        top: 30px;
        left: 17px;
        background-color: #e4e4e4;
        border: 2px solid #000;
        box-shadow: -2px -2px 0 0 #c2c2c2 inset, 2px 2px 0 0 #f5f5f5 inset;
    }

    /* to add padding without affecting .info's border/box shadow */
    .info:after {
        content: "";
        position: absolute;
        height: calc(100% + 50px);
        width: calc(100% + 50px);
        transform: translate(-50%, -50%);
        left: 50%;
        top: 50%;
        z-index: 0 !important;
    }

    .download-btn {
        display: block;
        position: absolute;
        height: 50px;
        width: 50px;
        right: 0;
        bottom: 0;
        background-color: #ccccff;
        z-index: 10 !important;
    }

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
