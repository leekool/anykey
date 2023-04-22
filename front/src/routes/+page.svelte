<script lang="ts">
    import KeyboardMenu from "../lib/KeyboardMenu.svelte";
    import Window from "../lib/Window.svelte";
    import { onMount } from "svelte";

    let file: File;
    let formData = new FormData();
    let fileName: string = "";
    let layoutResponse: string = "";

    let menuItems: { name: string; path: string }[] = [];
    let selectedItem: { name: string; path: string } = { name: "", path: "" };

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

    const onFileSelected = (e: { currentTarget: HTMLInputElement }) => {
        if (!e.currentTarget.files) return;

        file = e.currentTarget.files[0];
        fileName = file.name;
    };

    const submitForm = (event: Event) => {
        event.preventDefault(); // prevent default form submission behavior
        console.log("Form submitted!");
        postLayout();
    };

    async function postLayout() {
        formData.append("file", file);
        formData.append("mapPath", selectedItem.path);
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
            <div class="navbar-text">layout_gen</div>
            <div class="navbar-buttons">
                <span class="ri-minimise" />
                <span class="ri-maximise" />
                <span class="ri-close" />
            </div>
        </div>

        {#if menuItems && menuItems.length > 1}
            <div class="content main-item">
                <div class="half-container">
                    <div class="half">
                        <KeyboardMenu bind:selectedItem bind:menuItems />

                    </div>
                    <div class="seperator"></div>
                    <div class="half">
                        <div class="btn">
                            <label>
                                <input
                                    type="file"
                                    accept=".c"
                                    on:change={(e) => onFileSelected(e)}
                                />
                                upload keymap
                            </label>
                        </div>
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
        {/if}
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
        <div class="content">
            <div class="main-item map-svg">
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
        height: 90%;
        width: 100%;
    }

    .footer {
        display: flex;
        width: auto;
        margin: 3px;
        justify-content: space-between;
    }

    .half {
        display: flex;
        margin: 3px;
        /* position: absolute; */
        width: 50%;
        max-width: 175px;
    }

    input[type="file"],
    input[type="submit"] {
        display: none;
    }

    label {
        /* border: 1px solid #ccc; */
        /* display: inline-block; */
        /* padding: 3px 6px; */
        cursor: pointer;
    }

    .seperator {
        background-color: #7a776e;        
        width: 1px;
    }

    .btn {
        padding: 2px 5px;
        height: 20px;
        background-color: #696d63;
        color: #e9e5d8;
        box-shadow: 1px 1px 0 0 #b4b6b1 inset,
                    -1px -1px 0 0 #3f413b inset;
    }

    /* .select-btn { */
    /*     display: inline-block; */
    /*     position: relative; */
    /* } */
    /**/
    /* .submit-btn { */
    /*     left: 50%; */
    /*     top: 50%; */
    /*     position: absolute; */
    /*     transform: translate(-50%); */
    /* } */
    /**/
    /* .upload-btn, */
    /* .select-btn { */
    /*     left: 50%; */
    /*     position: absolute; */
    /*     transform: translate(-50%); */
    /* } */
    /**/
    /* .upload-btn { */
    /*     top: 45px; */
    /*     left: 0; */
    /*     background: lightgrey; */
    /* } */
    /**/
    /* .submit-btn, */
    /* .select-btn, */
    /* .upload-btn, */
    /* .map-svg { */
    /*     margin-top: 10px; */
    /*     z-index: 1; */
    /* } */

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f6f6f6;
        /* min-width: 230px; */
        border: 1px solid #ddd;
        z-index: 10;
    }

    /* Show the dropdown menu */
    .show {
        display: block;
    }

    .map-svg {
        overflow-y:scroll;
        justify-content: center;
        align-items: center;
        height:auto;
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
        height: 25px;
        color: #e9e5d8;
        justify-content: flex-end;
        background-repeat: repeat;
        background-image: url("images/navbar-tile.svg");
        box-shadow: 0 -1px 0 0 #30302f inset;
        user-select: none;
    }

    .navbar-text {
        display: flex;
        height: 28px;
        left: 50%;
        font-size: 15px;
        align-items: center;
        position: absolute;
        transform: translate(-50%);
    }

    .navbar-buttons {
        display: flex;
        max-width: 90px;
        align-items: center;
        justify-content: center;
        margin-right: 2px;
    }

    .navbar-buttons span {
        font-size: 8px;
        padding: 8px;
        cursor: pointer;
    }

    .navbar-buttons span:hover {
        opacity: 0.4;
    }

    .content {
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        max-height: calc(100% - 29.5px);
        background-color: #ccc6b7;
    }

    .position-left {
        margin: 0;
        position: absolute;
        top: 15%;
        left: 8%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        height: 200px;
        width: 350px;
        max-width: 1000px;
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
        max-height: 800px;
        max-width: 1400px;
    }

    /* .btn-valid { */
    /*     background-color: rgb(153, 255, 153, 50); */
    /* } */
    /**/
    /* .btn-invalid { */
    /*     background-color: rgb(255, 153, 153, 50); */
    /* } */
</style>
