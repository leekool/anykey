<script lang="ts">
    export let file: File;
    export let fileName: string = "";
    export let mergeLayers: boolean = false;

    let fileSize: string = "";

    const fileSizeKb = (file: File) => {
        var i = Math.floor(Math.log(file.size) / Math.log(1024));
        return `${parseFloat((file.size / Math.pow(1024, i)).toFixed(1))}kB`;
    };

    const onFileSelected = (e: { currentTarget: HTMLInputElement }) => {
        if (!e.currentTarget.files) return;

        file = e.currentTarget.files[0];
        fileName = file.name;
        fileSize = fileSizeKb(file);
        console.log(file);
    };
</script>

<div class="main">
    <div class="upload-btn">
        <label>
            <img src="images/upload-icon.png" />
            <input
                type="file"
                accept=".c"
                on:change={(e) => onFileSelected(e)}
            />
        </label>
    </div>
    <div class="info">
        <div>{fileName}</div>
        <div>{fileSize ? `size: ${fileSize}` : ''}</div>
    </div>
    <div class="check-btn">
        <label>
            <input type="checkbox" bind:checked={mergeLayers} />
            <span class="checkbox" />
            merge layers
        </label>
    </div>
</div>

<style>
    .main {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        flex: 1 1 auto;
        height: 100%;
    }

    input {
        display: none;
    }

    label {
        display: inline-block;
        margin-top: 2px;
        cursor: pointer;
    }

    .checkbox {
        display: inline-block;
        height: 10px;
        width: 10px;
        background-color: #fff;
    }

    .upload-btn {
        display: flex;
        align-content: center;
        justify-content: center;
        /* padding-left: 5px; */
        /* height: 20px; */
        /* background-color: #553e3a; */
        /* color: #e9e5d8; */
        /* box-shadow: 1px 1px 0 0 #b4b6b1 inset, -1px -1px 0 0 #3f413b inset; */
        /* border-color: #b4b6b1 #363430 #363430 #b4b6b1; */
        /* border-style: solid; */
        /* border-width: 1px; */
        border-color: #7a776e #fff #fff #7a776e;
        border-style: inset;
        border-width: 1px;
        image-rendering: pixelated;
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    .check-btn {
        padding-left: 5px;
        height: 20px;
        color: #000;
        /* box-shadow: 1px 1px 0 0 #b4b6b1 inset, -1px -1px 0 0 #3f413b inset; */
        user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }

    /* on checkbox hover, change bg colour */
    .check-btn:hover input ~ .checkbox {
        background-color: #e5dac3;
    }

    /* black bg when checkbox checked (test) */
    .check-btn input:checked ~ .checkbox {
        background-color: #000;
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

    /* style tick/checkmark (just a shitty test atm) */
    .check-btn .checkbox:after {
        width: 3px;
        height: 7px;
        margin-left: 2px;
        border: solid white;
        border-width: 0 2px 2px 0;
        -webkit-transform: rotate(45deg);
        -ms-transform: rotate(45deg);
        transform: rotate(45deg);
    }
</style>
