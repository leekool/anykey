<script lang="ts">
    export let file: File;
    export let fileName: string, fileSize: string = "";
    export let mergeLayers: boolean = false;

    let mergeLayersSelected: boolean = false;

    const fileSizeKb = (file: File): string => {
        return (file.size / 1024).toFixed(0);
    };

    const onFileSelected = (e: { currentTarget: HTMLInputElement }): void => {
        if (!e.currentTarget.files) return;

        file = e.currentTarget.files[0];
        if (Number(fileSizeKb(file)) > 1024) {
            fileName = 'Max allowed file size is 1MB'
            return;
        }

        if (file.type !== 'text/plain' || !file.name.endsWith(".c")) {
            fileName = 'File type must be of type ".c"'
            return;
        }
        fileName = file.name;
        fileSize = fileSizeKb(file) + "kB";
    };
</script>

<div class="main">
    <fieldset>
        <legend>Keymap</legend>
        <div class="upload-btn pixel-corners">
            <label>
                <!-- <img src="images/upload-icon.png" /> -->
                upload...
                <input
                    type="file"
                    accept=".c"
                    on:change={(e) => onFileSelected(e)}
                />
            </label>
        </div>
        <div class="check-btn">
            <label>
                <input
                    type="checkbox"
                    bind:checked={mergeLayers}
                    on:click={() =>
                        (mergeLayersSelected = !mergeLayersSelected)}
                />
                <span
                    class={mergeLayersSelected
                        ? "checkbox pixel-corners ri-close"
                        : "checkbox pixel-corners"}
                />
                merge layers
            </label>
        </div>
    </fieldset>
</div>

<style>
    @import url("/fonts/real-icons.css");
    @import url("/pixel-corners.css");

    .main {
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        min-height: 100px;
        height: 100%;
        width: 100%;
    }

    fieldset {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border: 2px solid #000;
        font-weight: 800;
        margin: 0 10px 0px 10px;
        height: 100%;
    }

    legend {
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    input {
        display: none;
    }

    label {
        /* margin-top: 2px; */
        cursor: pointer;
    }

    .upload-btn label {
        width: 100%;
        padding-left: 8px;
    }

    .upload-btn {
        display: flex;
        height: 27px;
        line-height: 23px;
        width: 30%;
        min-width: 92px;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
        box-sizing: border-box;
        background-color: #e0e0e0;
        box-shadow: -2px -2px 0 0 #c2c2c2 inset, 2px 2px 0 0 #f5f5f5 inset;
    }

    .upload-btn:hover {
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    .check-btn {
        display: flex;
        margin-top: 6px;
        flex: 1 1 auto;
        height: 25px;
        width: 0;
        min-width: 131px;
        color: #000;
        box-sizing: border-box;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .check-btn label {
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .checkbox {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 13px;
        height: 25px;
        aspect-ratio: 1 / 1;
        border: 2px solid #000;
        box-sizing: border-box;
        background-color: #ebebeb;
        box-shadow: -2px -2px 0 0 #f5f5f5 inset, 2px 2px 0 0 #c2c2c2 inset;
    }

    /* on checkbox hover, change bg colour */
    .check-btn:hover input ~ .checkbox {
        box-shadow: none;
    }

    /* black bg when checkbox checked (test) */
    .check-btn input:checked ~ .checkbox {
        /* background-color: #000; */
    }

    /* tick/checkmark indicator (hidden when unchecked) */
    .checkbox:after {
        content: "";
        display: none;
    }

    /* show tick/checkmark when checked */
    .check-btn input:checked ~ .checkbox:after {
        display: block;
    }
</style>
