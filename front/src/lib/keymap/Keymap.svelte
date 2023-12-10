<script lang="ts">
    import { onMount } from "svelte";

    export let layout = ""; // at the moment this is a string containg svg markup
    export let info = {
        fileName: "",
        filePath: "",
        fileSize: ""
    };

    onMount(() => {
        // const svg = document.querySelector("svg")!;

        // const viewBox = svg.getAttribute("viewBox")!.split(" ");

        // svg.setAttribute("viewBox", "0 0 " + viewBox[2] + " " + window.innerHeight); 
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
        /* width: 100%; */
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
