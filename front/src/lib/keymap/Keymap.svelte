<script lang="ts">
    import { onMount } from "svelte";
    // import { svg_element } from "svelte/internal";

    export let layout = ""; // at the moment this is a string containg svg markup
    export let info = {
        fileName: "",
        filePath: "",
        fileSize: ""
    };

    onMount(() => {
        // calculate vertical distance between highest and lowest key to set svg height
        const id = "#" + layout.match(/"([^"]*)"/)?.[1];
        const svg = document.querySelector(id)!;

        const height = +svg.getAttribute("height")!;
        const rects = svg.getElementsByTagName("rect");

        const highestKey = Math.min(...Array.from(rects).map(rect => rect.getBoundingClientRect().top));
        const lowestKey = Math.max(...Array.from(rects).map(rect => rect.getBoundingClientRect().bottom));

        // const firstKey = rects[0].getBoundingClientRect();
        // const lastKey = rects[rects.length - 1].getBoundingClientRect();

        // const verticalDistance = Math.abs(firstKey.top - lastKey.bottom) + 40;
        const verticalDistance = Math.abs(highestKey - lowestKey);

        const finalHeight = height <= 400 ? height : verticalDistance;

        svg.setAttribute("height", String(finalHeight));
    });
</script>

<div class="map-svg" id="canvas">
    <div class="layout">
        {@html layout}
    </div>
</div>

<style>
    .layout {
        display: flex;
        height: 100%;
        max-width: 100%;
        justify-content: center;
    }

    #canvas {
        display: flex;
        flex: 1 1 auto;
        /* width: 100%; */
        padding: 20px 20px 0 20px; 
        justify-content: center;
        align-items: center;
        overflow: scroll;
    }

    .map-svg {
        display: flex;
        flex: 1 1 auto;
        justify-content: center;
        align-items: center;
        font-size: 15px;
        letter-spacing: -0.5px;
        height: 100%;
        /* width: 100%; */
        /* padding-top: 500px; */
        /* padding-bottom: 500px; */
    }


    @media screen and (max-width: 700px) {
        #canvas {
            /* height: 100%; */
        }

        .map-svg {
            padding: 10px;
        }
    }
</style>
