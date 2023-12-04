<script lang="ts">
    export let layout = ""; // at the moment this is a string containg svg markup
    export let info = {
        fileName: "",
        filePath: "",
        fileSize: ""
    };
</script>

<div class="map-svg" id="canvas">
    {@html layout} 
</div>

<style>
    .map-svg {
        display: flex;
        padding: 20px;
        justify-content: center;
        align-items: center;
        font-size: 15px;
        letter-spacing: -0.5px;
    }

    @media screen and (max-width: 700px) {
        #canvas {
            height: 100%;
        }

        .map-svg {
            padding: 10px;
        }
    }
</style>
