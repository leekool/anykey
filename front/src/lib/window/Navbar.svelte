<script lang="ts">
    import { Window, windowStore } from "$lib/window/WindowStore";
    import { Keymap, keymapStore } from "$lib/keymap/KeymapStore";
    import { onMount } from "svelte";

    export let window_: Window;
    let keymap: any;

    const matchKeymap = () => {
        $keymapStore.forEach(k => {
            if (k.layout === window_.options.layout) keymap = k;
        });
    };

    onMount(() => {
        if (window_.options.type === "keymap") matchKeymap();
    });
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="navbar" class:inactive={!window_.options.focused}>
    <div class="navbar-title">{window_.name}</div>

    <div class="navbar-bg" style="width: 14px;" />

    <!-- info button -->
    {#if window_.options.navbar.info}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner info-btn"
                on:click|self={() => console.log("window info: ", window_)}
            >
                {#if window_.options.focused}
                    <div class="info-container">

                        {#if window_.options.type?.includes("keymap")}
                            <div class="info-layout-container">
                                <div class="info-layout-column" style="width: 35%;">
                                    <div class="info-layout-item">board:</div>
                                    <div class="info-layout-item">file:</div>
                                    <div class="info-layout-item">size:</div>
                                </div>
                                <div class="info-layout-column">
                                    <div class="info-layout-item" style="font-style: italic;">{keymap?.info.filePath}</div>
                                    <div class="info-layout-item" style="font-style: italic;">{keymap?.info.fileName}</div>
                                    <div class="info-layout-item" style="font-style: italic;">{keymap?.info.fileSize}</div>
                                </div>
                            </div>
                            <div style="min-height: 30px;"></div>
                            <div
                                class="download-btn pixel-corners"
                                title="Download"
                                on:click={() => {
                                    Keymap.screenshotCanvas(keymap);
                                }}
                            >
                                <div class="download-btn-icon" />
                            </div>
                        {/if}

                    </div>
                {/if}
            </div>
        </div>
    {/if}

    <div class="navbar-bg" />

    <!-- minimise button (left) -->
    {#if window_.options.navbar.minimise}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner minimise-btn"
                on:click={() => {
                    window_.toggleMinimise();
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <!-- maximise button (centre) -->
    {#if window_.options.navbar.maximise}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner maximise-btn"
                on:click={() => {
                    window_.toggleMaximise();
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <!-- close button (right) -->
    {#if window_.options.navbar.close}
        <div class="navbar-btn-base">
            <div
                class="navbar-btn-inner close-btn"
                on:click={() => {
                    window_.kill();
                    $windowStore = $windowStore; // tells svelte object changed
                }}
            />
        </div>
    {/if}

    <div class="navbar-bg" style="width: 14px;" />
</div>

<style>
    @import url("/pixel-corners.css");

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
        color: #000;
        background-color: #d5d5d5;
        text-shadow: 0 1px rgba(138, 134, 160, 0.7);
        pointer-events: none;
    }

    .navbar-btn-base {
        /* position: relative; */
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
        position: relative;
        /* box-shadow:  */
        /*     -2px -2px 0 0 #333366 inset,  */
        /*     -4px 0 0 0 #a4a4a4 inset, */
        /*     2px 10px 0 0 #a4a4a4 inset, */
        /*     0 12px 0 0 #333366 inset; */
        box-shadow: 
            -2px -2px 0 0 #55557b inset, 
            -4px 0 0 0 #a4a4a4 inset,
            2px 10px 0 0 #a4a4a4 inset,
            0 12px 0 0 #55557b inset;
    }

    .maximise-btn {
        position: relative;
    }

    .close-btn {
        position: relative;
        box-shadow: 
            -2px -2px 0 0 #333366 inset, 
            -6px -6px 0 0 #a4a4a4 inset,
            -8px -8px 0 0 #333366 inset;
    }

    .info-btn {
        /* position: relative; */
        cursor: default;
    }

    .info-btn:after {
        content: "i";
        display: flex;
        position: relative;
        height: 100%;
        width: 100%;
        left: -1px;
        justify-content: center;
        align-content: center;
        color: #333366;
        font-size: 14px;
        font-weight: 600;
        text-shadow: 0 1px #f5f5f5, 0 2px rgba(138, 134, 160, 0.7);
    }

    .info-btn:hover .info-container {
        display: block;
    }

    .info-container {
        /* display: block; */
        display: none;
        position: absolute;
        padding: 5px;
        top: 30px;
        left: 17px;
        /* max-width: 180px; */
        max-width: 280px;
        background-color: #e4e4e4;
        border: 2px solid #000;
        box-shadow: -2px -2px 0 0 #c2c2c2 inset, 2px 2px 0 0 #f5f5f5 inset;
        cursor: default;
    }

    .info-layout-container {
        display: flex;
        margin: 1px 0 0 4px;
    }

    .info-layout-column {
        display: flex;
        flex-wrap: wrap;
        /* width: 50%; */
    }

    .info-layout-item {
        display: flex;
        width: 100%;
    }

    /* to add padding without affecting .info-container's border/box shadow */
    .info-container:after {
        content: "";
        position: absolute;
        height: calc(100% + 15px);
        width: calc(100% + 15px);
        transform: translate(-50%, -50%);
        left: 50%;
        top: 50%;
        z-index: 0 !important;
    }

    .download-btn {
        display: flex;
        position: absolute;
        height: 27px;
        aspect-ratio: 1 / 1;
        right: 6px;
        bottom: 6px;
        align-items: center;
        justify-content: center;
        font-size: 15px;
        background-color: #e0e0e0;
        box-sizing: border-box;
        box-shadow: -2px -2px 0 0 #c2c2c2 inset, 2px 2px 0 0 #f5f5f5 inset;
        cursor: pointer;
        z-index: 10 !important;
    }

    .download-btn:hover {
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    .download-btn > * {
        user-select: none;
        cursor: pointer;
    }

    /* maybe make it a floppy disc or something */
    .download-btn-icon {
        height: 70%;
        width: 70%;
        content: url("/images/left-arrow.svg");
        transform: rotate(270deg);
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
