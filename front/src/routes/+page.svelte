<script lang="ts">
    import KeyboardMenu from "../lib/KeyboardMenu.svelte";
    import UploadMenu from "../lib/UploadMenu.svelte";
    import Window from "../lib/window/Window.svelte";
    import Taskbar from "../lib/Taskbar.svelte";
    import { onMount } from "svelte";

    // from UploadMenu
    let file: File;
    let fileName: string = "";
    let fileSize: string = "";
    let mergeLayers: boolean = false;

    // from KeyboardMenu
    let menuItems: { name: string; path: string }[] = [];
    let selectedItem: { name: string; path: string } = { name: "", path: "" };

    let formData = new FormData();
    let layoutResponse: string[] = [];
    let layoutName: string = "";
    let submitDisabled: boolean = true;
    let submitState: string = "submit-invalid";

    // This is a watcher
    $: if (fileName && selectedItem.name !== "") {
        submitState = "submit-valid";
        submitDisabled = false;
    }

    onMount(async () => {
        // fetch data from the server when the component is mounted
        const response = await fetch("http://localhost:5000/api/keyboards");
        menuItems = await response.json();
    });

    const submitForm = (event: Event) => {
        if (submitState == "submit-invalid") return;

        event.preventDefault(); // prevent default form submission behavior
        layoutName = `${selectedItem.name.toLowerCase()} layout`;

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
        layoutResponse.push(json.message);
        layoutResponse = layoutResponse; // trigger svelte state management
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<Window name="layout_gen">
    <KeyboardMenu bind:selectedItem bind:menuItems />
    <UploadMenu bind:file bind:fileName bind:mergeLayers bind:fileSize />

    <div class="bottom-container">
        <div class="info">
            <span>
                {fileName ? selectedItem.name + " - " : selectedItem.name}
            </span>
            <span>{fileName} {fileSize}</span>
        </div>
        <div
            class="{submitState} submit-btn pixel-corners"
            on:click={(e) => submitForm(e)}
        >
            <label>
                <input class="" type="submit" disabled={submitDisabled} />
                submit
            </label>
        </div>
    </div>
</Window>

<!-- SVG Window -->
{#each layoutResponse as layout}
    <Window name={layoutName} position="position-layout" options={{ navbarMaximise: true }}>
        <div class="map-svg">
            {@html layout}
        </div>
    </Window>
{/each}

<Taskbar />

<style>
    @import url("../../static/pixel-corners.css");

    .bottom-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-sizing: border-box;
        min-height: 40px;
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
        width: 90%;
        line-height: 28px;
        padding-left: 5px;
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
