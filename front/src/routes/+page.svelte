<script lang="ts">
    import WindowComp from "$lib/window/Window.svelte";
    import { Window, windowStore } from "$lib/window/WindowStore";

    import LayoutGen from "$lib/layout_gen/LayoutGen.svelte";
    import Taskbar from "$lib/Taskbar.svelte";

    import { onMount } from "svelte";

    // from LayoutGen

    onMount(async () => {
        Window.isMobile = (window.innerWidth <= 600 && window.innerHeight <= 800); 
    });
</script>

<WindowComp 
    name="layout_gen"
    slot={{
        component: LayoutGen,
        props: null
    }}
/>

<!-- SVG Window -->
<!-- {#each layoutResponse as layout} -->
<!--     <WindowComp -->
<!--         name={layoutName} -->
<!--         options={{  -->
<!--             type: "keymap",  -->
<!--             maximised: Window.isMobile, -->
<!--             navbar: { -->
<!--                 minimise: true, -->
<!--                 maximise: !Window.isMobile, -->
<!--                 close: true, -->
<!--                 info: true -->
<!--             }, -->
<!--             layoutInfo: { -->
<!--                 svg: layout, -->
<!--                 name: selectedItem, -->
<!--                 fileName: fileName, -->
<!--                 filePath: selectedItem, -->
<!--                 fileSize: fileSize -->
<!--             } -->
<!--         }} -->
<!--     > -->
<!--         <div class="map-svg" id="canvas"> -->
<!--             <viewBox> -->
<!--                 {@html layout} -->
<!--             </viewBox> -->
<!--         </div> -->
<!--     </WindowComp> -->
<!-- {/each} -->

<Taskbar />

<style>
    @import url("/pixel-corners.css");

    .bottom-container {
        display: flex;
        min-height: 40px;
        max-width: 100%;
        justify-content: space-between;
        align-items: center;
        box-sizing: border-box;
        margin: 2px 10px;
        font-weight: bold;
    }

    .submit-btn {
        display: flex;
        align-items: center;
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        height: 27px;
        font-size: 15px;
        cursor: pointer;
        padding: 2px 8px;
        background-color: #e0e0e0;
    }

    .submit-btn > * {
        user-select: none;
        cursor: pointer;
    }

    .submit-valid {
        box-shadow: -2px -2px 0 0 #c2c2c2 inset, 2px 2px 0 0 #f5f5f5 inset;
    }

    .submit-valid:hover {
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    .submit-invalid {
        cursor: not-allowed;
        color: #a4a4a4;
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    .submit-invalid > * {
        cursor: not-allowed;
    }

    .info {
        max-width: 90%;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        line-height: 28px;
        padding-left: 5px;
        margin-right: 2px;
    }

    .map-svg {
        display: flex;
        padding: 20px;
        justify-content: center;
        align-items: center;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        letter-spacing: -0.5px;
    }

    input {
        display: none;
    }
</style>
