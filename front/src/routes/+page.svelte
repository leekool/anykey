<script lang="ts">
    import KeyboardMenu from "../lib/KeyboardMenu.svelte";
    import UploadMenu from "../lib/UploadMenu.svelte";
    import Window from "../lib/Window.svelte";
    import { onMount } from "svelte";

    // from UploadMenu
    let file: File;
    let fileName: string = "";
    let mergeLayers: boolean = false;

    // from KeyboardMenu
    let menuItems: { name: string; path: string }[] = [];
    let selectedItem: { name: string; path: string } = { name: "", path: "" };

    let formData = new FormData();
    let layoutResponse: string = "";
    let submitDisabled: boolean = true;
    let btnState: string = "btn-invalid";

    // This is a watcher
    $: if (fileName && selectedItem.name !== "") {
        btnState = "btn-valid";
        submitDisabled = false;
    }

    onMount(async () => {
        // fetch some data from the server when the component is mounted
        const response = await fetch("http://localhost:5000/api/keyboards");
        menuItems = await response.json();
    });

    const submitForm = (event: Event) => {
        event.preventDefault(); // prevent default form submission behavior
        console.log("Form submitted!");
        postLayout();
    };

    async function postLayout() {
        formData = new FormData();

        formData.append("file", file);
        formData.append("mapPath", selectedItem.path);
        formData.append("mergeLayers", mergeLayers == true ? "true" : "false");
        const response = await fetch("http://localhost:5000/api/layout", {
            method: "POST",
            body: formData,
        });
        const json = await response.json();
        layoutResponse = json.message;
        console.log(json.message);
    }
</script>

<!-- <Window /> -->
<!-- Layout Window -->
<div class="position-centre">
    <div class="main pixel-corners">
        <div class="navbar main-item">
            <div class="navbar-title">layout_gen</div>
            <div class="navbar-bg" style="width: 14px;"/>
            <div class="navbar-btn-base">
                <div class="navbar-btn-inner" />
            </div>
            <div class="navbar-bg" />
            <div class="navbar-btn-base">
                <div class="navbar-btn-inner navbar-btn-right" />
            </div>
            <div class="navbar-bg" style="width: 14px;"/>
        </div>

        <!-- {#if menuItems && menuItems.length > 1} -->
        <div class="content main-item">
            <div class="half-container">
                <div class="half">
                    <KeyboardMenu bind:selectedItem bind:menuItems />
                </div>
                <!-- <div class="separator" /> -->
                <div class="half">
                    <UploadMenu bind:file bind:fileName bind:mergeLayers />
                </div>
            </div>
        </div>
        <div class="footer">
            <div class="footer-btn-container">
                <div class="footer-btn">
                    <div class="left-arrow" />
                </div>
                <div class="separator" />
                <div class="footer-scroll-btn">
                    <div class="scroll-img" />
                </div>
            </div>
            <div class="footer-bg" />
            <div class="separator" />
            <div class="footer-btn">
                <div class="right-arrow" />
            </div>
            <!-- <div class="version"> -->
            <!--     <span style="padding-left: 5px;">{selectedItem.name}</span> -->
            <!--     <span>{fileName}</span> -->
            <!-- </div> -->
            <!-- <div -->
            <!--     class="btn" -->
            <!--     on:click={(e) => submitForm(e)} -->
            <!--     on:keypress={(e) => console.log(e)} -->
            <!-- > -->
            <!--     <label class={btnState}> -->
            <!--         <input type="submit" disabled={submitDisabled} /> -->
            <!--         submit -->
            <!--     </label> -->
            <!-- </div> -->
        </div>
        <!-- {/if} -->
    </div>
</div>

<!-- SVG Window -->
{#if layoutResponse}
    <div class="position-centre">
        <div class="main">
            <div class="navbar main-item">
                <div class="navbar-text">layout_img</div>
                <div class="navbar-buttons">
                    <span class="ri-minimise" />
                    <span class="ri-maximise" />
                    <span class="ri-close" />
                </div>
            </div>
            <div class="content main-item">
                <div class="map-svg">
                    {@html layoutResponse}
                </div>
            </div>
        </div>
    </div>
{/if}

<style>
    @import url("../../static/fonts/real-icons.css");

    .half-container {
        display: flex;
        width: 100%;
        height: 250px;
    }

    .half {
        display: flex;
        margin: 3px;
        /* position: absolute; */
        width: 50%;
        max-width: 175px;
    }

    .footer {
        display: flex;
        justify-items: space-between;
        box-sizing: border-box;
        height: 28px;
        user-select: none;
        /* margin: 3px; */
        box-shadow: 0 -2px 0 0 #000;
    }

    .footer-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        align-items: center;
        justify-content: center;
        background-color: #d5d5d5;
        box-sizing: border-box;
        border-color: #fff #a0a0a0 #a0a0a0 #fff;
        border-style: solid;
        border-width: 2px;
    }

    .footer-btn-container {
        display: flex;
        aspect-ratio: 2 / 1;
        box-sizing: border-box;
        /* justify-content: center; */
    }

    .footer-scroll-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
        background-color: #aaaaaa;
        border-color: #ccccff #333366 #333366 #ccccff;
        border-style: solid;
        border-width: 2px;
        z-index: 10;
    }

    .footer-bg {
        height: calc(100% - 2px);
        width: 100%;
        background-image: url("images/footer-tile.svg");
    }

    /* .footer-btn > .left-arrow { */
    /*     border-right: 1px solid #000; */
    /* } */

    .scroll-img {
        display: flex;
        height: 70%;
        width: 70%;
        content: url("images/footer-scroll.svg");
        border-left: 1px solid #a3a3d7;
        margin-right: 1px;
    }

    .left-arrow {
        display: flex;
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
    }

    .right-arrow {
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        transform: rotate(180deg);
    }

    input {
        display: none;
    }

    label {
        display: inline-block;
        margin-top: 2px;
        cursor: pointer;
    }

    .btn {
        padding-left: 5px;
        height: 22px;
        background-color: #696d63;
        color: #e9e5d8;
        box-shadow: 1px 1px 0 0 #b4b6b1 inset, -1px -1px 0 0 #3f413b inset;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .separator {
        background-color: #000;
        min-width: 2px;
        z-index: 10;
    }

    .map-svg {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 15px;
        letter-spacing: -0.5px;
    }

    /* svg {
   max-width: 20%;
   max-height: 20%;
   } */

    .main {
        display: flex;
        flex: 1 1 auto;
        /* padding: 5px 0px 0px 5px; */
        flex-direction: column;
        font-family: "Tamzen", sans-serif;
        /* max-height: calc(100% - 10px); */
        max-height: 100%;
        background-color: #d5d5d5;
    }

    .main-item {
        /* position: sticky; */
        padding-top: 1px;
        border-color: #fff #a0a0a0 #a0a0a0 #fff;
        border-style: solid;
        border-width: 1px;
        /* width: calc(100% - 5px); */
    }

    /* .border { */
    /*     display: flex; */
    /*     position: absolute; */
    /*     width: 100%; */
    /*     flex-direction: column; */
    /*     height: calc(100% - 30px); */
    /*     box-shadow: 0 0 0 1px #1f1f1e inset, 0 0 0 3px #30302f inset, */
    /*         0 0 0 6px #1f1f1e inset, 0 3px 15px rgba(0, 0, 0, 0.3); */
    /* } */

    /* .border { */
    /*     position: absolute; */
    /*     width: 100%; */
    /*     border: 1px solid black; */
    /*     border-radius: 3px; */
    /* } */

    /* .focus {
   box-shadow: 0 0 0 1px #222020 inset,
   0 0 0 3px #32302c inset,
   0 0 0 6px #222020 inset,
   0 3px 15px rgba(0, 0, 0, 0.3);
   z-index: 10;
   } */

    .navbar {
        display: flex;
        height: 34px;
        color: #e9e5d8;
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
        box-shadow: 0 2px 0 0 #777777 inset,
                    0 4px 0 0 #d5d5d5 inset,
                    0 6px 0 0 #777777 inset,
                    0 8px 0 0 #d5d5d5 inset,
                    0 10px 0 0 #777777 inset,
                    0 12px 0 0 #d5d5d5 inset,
                    0 14px 0 0 #777777 inset,
                    0 16px 0 0 #d5d5d5 inset,
                    0 18px 0 0 #777777 inset,
                    0 20px 0 0 #d5d5d5 inset,
                    0 22px 0 0 #777777 inset;
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

    .navbar-btn-right {
        box-shadow: -2px -2px 0 0 #333366 inset,
                    -6px -6px 0 0 #a4a4a4 inset,
                    -8px -8px 0 0 #333366 inset;
    }

    /* .navbar-text span { */
    /*     position: absolute; */
    /*     left: 50%; */
    /*     transform: translate(-50%); */
    /*     font-weight: bold; */
    /*     margin-top: 1px; */
    /*     text-shadow: 0 1px rgba(138, 134, 160, 0.7); */
    /* } */

    /* .navbar-buttons { */
    /*     display: flex; */
    /*     max-width: 180px; */
    /*     align-items: center; */
    /*     justify-content: center; */
    /*     color: #000; */
    /* } */
    /**/
    /* .navbar-buttons span { */
    /*     font-size: 11px; */
    /*     padding: 4px; */
    /*     cursor: pointer; */
    /* } */
    /**/
    /* .navbar-buttons span:hover { */
    /*     opacity: 0.4; */
    /* } */

    .content {
        overflow-y: scroll;
        display: flex;
        flex: 1 1 auto;
        align-self: center;
        flex-direction: column;
        background-color: #d5d5d5;
        margin-top: 2px;
    }

    .position-left {
        margin: 0;
        position: absolute;
        top: 15%;
        left: 15%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        height: 200px;
        width: 350px;
        max-width: 500px;
    }

    .position-centre {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        height: 300px;
        width: 80%;
        max-width: 500px;
    }

    /* .btn-valid { */
    /*     background-color: rgb(153, 255, 153, 50); */
    /* } */
    /**/
    /* .btn-invalid { */
    /*     background-color: rgb(255, 153, 153, 50); */
    /* } */
    /* border */

    .pixel-corners,
    .pixel-corners--wrapper {
        clip-path: polygon(
            0px calc(100% - 2px),
            2px calc(100% - 2px),
            2px 100%,
            calc(100% - 2px) 100%,
            calc(100% - 2px) calc(100% - 2px),
            100% calc(100% - 2px),
            100% 2px,
            calc(100% - 2px) 2px,
            calc(100% - 2px) 0px,
            2px 0px,
            2px 2px,
            0px 2px
        );
        position: relative;
    }
    .pixel-corners {
        border: 2px solid transparent;
    }
    .pixel-corners--wrapper {
        width: fit-content;
        height: fit-content;
    }
    .pixel-corners--wrapper .pixel-corners {
        display: block;
        clip-path: polygon(
            2px 2px,
            calc(100% - 2px) 2px,
            calc(100% - 2px) calc(100% - 2px),
            2px calc(100% - 2px)
        );
    }
    .pixel-corners::after,
    .pixel-corners--wrapper::after {
        content: "";
        position: absolute;
        clip-path: polygon(
            0px calc(100% - 2px),
            2px calc(100% - 2px),
            2px 100%,
            calc(100% - 2px) 100%,
            calc(100% - 2px) calc(100% - 2px),
            100% calc(100% - 2px),
            100% 2px,
            calc(100% - 2px) 2px,
            calc(100% - 2px) 0px,
            2px 0px,
            2px 2px,
            0px 2px,
            0px 50%,
            2px 50%,
            2px 2px,
            calc(100% - 2px) 2px,
            calc(100% - 2px) calc(100% - 2px),
            2px calc(100% - 2px),
            2px 50%,
            0px 50%
        );
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: #000000;
        display: block;
        pointer-events: none;
    }
    .pixel-corners::after {
        margin: -2px;
    }
</style>
