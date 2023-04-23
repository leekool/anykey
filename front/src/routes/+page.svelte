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
<div class="border position-centre">
    <div class="main">
        <div class="navbar main-item">
            <div class="navbar-buttons">
                <span class="ri-close" />
            </div>
            <div class="navbar-text">
                <span>layout_gen</span>
            </div>
            <div class="navbar-buttons">
                <span class="ri-minimise" />
                <span class="ri-maximise" />
                <span class="ri-close" />
            </div>
        </div>

        <!-- {#if menuItems && menuItems.length > 1} -->
        <div class="content main-item">
            <div class="half-container">
                <div class="half">
                    <KeyboardMenu bind:selectedItem bind:menuItems />
                </div>
                <div class="separator" />
                <div class="half">
                    <UploadMenu bind:file bind:fileName bind:mergeLayers />
                </div>
            </div>
            <div class="footer">
                <div class="version">
                    <span style="padding-left: 5px;">{selectedItem.name}</span>
                    <span>{fileName}</span>
                </div>
                <div
                    class="btn"
                    on:click={(e) => submitForm(e)}
                    on:keypress={(e) => console.log(e)}
                >
                    <label class={btnState}>
                        <input type="submit" disabled={submitDisabled} />
                        submit
                    </label>
                </div>
            </div>
        </div>
        <!-- {/if} -->
    </div>
</div>

<!-- SVG Window -->
{#if layoutResponse}
    <div class="border position-centre">
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
        height: auto;
        width: auto;
        /* margin: 3px; */
        justify-content: space-between;
        background-color: #e5dac3;
        border-top: 1px inset #7a776e;
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
        background-color: #7a776e;
        width: 1px;
    }

    .map-svg {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* svg {
   max-width: 20%;
   max-height: 20%;
   } */

    .main {
        display: flex;
        flex: 1 1 auto;
        padding: 5px 0px 0px 5px;
        flex-direction: column;
        font-family: "Tamzen", sans-serif;
        max-height: calc(100% - 10px);
    }

    .main-item {
        position: sticky;
        width: calc(100% - 5px);
    }

    .border {
        display: flex;
        position: absolute;
        width: 100%;
        flex-direction: column;
        height: calc(100% - 30px); /* 30px to account for taskbar */
        box-shadow: 0 0 0 1px #1f1f1e inset, 0 0 0 3px #30302f inset,
            0 0 0 6px #1f1f1e inset, 0 3px 15px rgba(0, 0, 0, 0.3);
    }

    /* .focus {
   box-shadow: 0 0 0 1px #222020 inset,
   0 0 0 3px #32302c inset,
   0 0 0 6px #222020 inset,
   0 3px 15px rgba(0, 0, 0, 0.3);
   z-index: 10;
   } */

    .navbar {
        display: flex;
        height: 38px;
        color: #e9e5d8;
        font-size: 15px;
        align-items: center;
        justify-content: space-between;
        background-repeat: repeat;
        /* background-image: url("images/navbar-tile.svg"); */
        background-color: #d5d5d5;
        box-shadow: 0 -1px 0 0 #30302f inset;
        user-select: none;
    }

    .navbar-text {
        position: absolute;
        left: 50%;
        transform: translate(-50%);
        background-image: url("images/navbar-title-tile.svg");
        width: 60%;
        height: 17px;
        margin-bottom: 1px;
    }

    .navbar-text span {
        position: absolute;
        left: 50%;
        transform: translate(-50%);
        font-weight: bold;
        margin-top: 1px;
        text-shadow: 0 1px rgba(138, 134, 160, 0.7);
    }

    .navbar-buttons {
        display: flex;
        max-width: 90px;
        align-items: center;
        justify-content: center;
        margin-right: 2px;
        color: #000;
    }

    .navbar-buttons span {
        font-size: 8px;
        padding: 6px;
        cursor: pointer;
    }

    .navbar-buttons span:hover {
        opacity: 0.4;
    }

    .content {
        overflow-y: scroll;
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        background-color: #ccc6b7;
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
        height: 200px;
        width: 350px;
        max-width: 1500px;
    }

    /* .btn-valid { */
    /*     background-color: rgb(153, 255, 153, 50); */
    /* } */
    /**/
    /* .btn-invalid { */
    /*     background-color: rgb(255, 153, 153, 50); */
    /* } */
</style>
