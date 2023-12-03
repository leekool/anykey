<script lang="ts">
    import { PUBLIC_BASE_URL } from "$env/static/public";

    import KeyboardMenu from "$lib/layout_gen/KeyboardMenu.svelte";
    import UploadMenu from "$lib/layout_gen/UploadMenu.svelte";
    import WindowComponent from "$lib/window/Window.svelte";
    import { Window } from "$lib/window/WindowStore";
    import KeymapComponent from "$lib/keymap/Keymap.svelte";
    import { Keymap } from "$lib/keymap/KeymapStore";

    // from UploadMenu
    let file: File;
    let fileName: string = "";
    let fileSize: string = "";
    let mergeLayers: boolean = false;

    // from KeyboardMenu
    let selectedItem: string = "";

    let formData = new FormData();

    let layoutResponse: string[] = [];
    let layoutName: string = "";

    let submitDisabled: boolean = true;
    let submitState: string = "submit-invalid";

    $: if (fileName && selectedItem !== "") {
        submitState = "submit-valid";
        submitDisabled = false;
    }

    const submitForm = () => {
        if (submitState == "submit-invalid") return;

        layoutName = `${selectedItem.toLowerCase()} layout`;

        postLayout();
    };

    const createLayout = (props: any) => {
        // find the highest level div ("contents") and create a child div as the target
        const contentDiv = document.querySelector("div[style='display: contents']")!;
        const target = document.createElement("div");
        contentDiv.appendChild(target);

        new WindowComponent({
            target,
            props,
        });
    };

    // get keyboard SVG Image
    async function postLayout() {
        formData = new FormData();

        formData.append("file", file);
        formData.append("keyboardName", selectedItem);
        formData.append("mergeLayers", mergeLayers == true ? "true" : "false");

        const response = await fetch(`${PUBLIC_BASE_URL}:5000/api/layout`, {
            method: "POST",
            body: formData,
        });

        const json = await response.json();
        const layout = json.message

        layoutResponse.push(json.message);

        // i will refactor this bigly
        const keymapInfo = {
            fileName: fileName,
            filePath: selectedItem,
            fileSize: fileSize
        }; 

        new Keymap(layout, keymapInfo);

        createLayout({
            name: fileName,
            options: {
                type: "keymap",
                layout,
                maximised: Window.isMobile,
                navbar: {
                    minimise: true,
                    maximise: !Window.isMobile,
                    close: true,
                    info: true,
                }
            },
            slot: {
                component: KeymapComponent,
                props: {
                    layout,
                    info: keymapInfo
                }
            }
        });
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div>
    <KeyboardMenu bind:selectedItem />
    <UploadMenu bind:file bind:fileName bind:mergeLayers bind:fileSize />

    <div class="bottom-container">
        <div class="info">
            <span>
                {fileName ? selectedItem + " - " : selectedItem}
            </span>
            <span>{fileName} {fileSize}</span>
        </div>
        <div
            class="{submitState} submit-btn pixel-corners"
            on:click|preventDefault={() => submitForm()}
        >
            <label>
                <input class="" type="submit" disabled={submitDisabled} />
                submit
            </label>
        </div>
    </div>
</div>

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

    input {
        display: none;
    }
</style>