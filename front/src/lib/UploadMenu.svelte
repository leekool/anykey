<script lang="ts">
    export let file: File;
    export let fileName: string = "";
    export let mergeLayers: boolean = false;

    const onFileSelected = (e: { currentTarget: HTMLInputElement }) => {
        if (!e.currentTarget.files) return;

        file = e.currentTarget.files[0];
        fileName = file.name;
    };
</script>

<div class="main">
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
    <div class="btn">
        <label>
            <input type="checkbox" bind:checked={mergeLayers} />
            <span class="checkbox" />
            merge layers
        </label>
    </div>
</div>

<style>
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

    /* on checkbox hover, change bg colour */
    .btn:hover input ~ .checkbox {
        background-color: #e5dac3;
    }

    /* black bg when checkbox checked (test) */
    .btn input:checked ~ .checkbox {
        background-color: #000;
    }

    /* tick/checkmark indicator (hidden when unchecked) */
    .checkbox:after {
        content: "";
        display: none;
    }

    /* show tick/checkmark when checked */
    .btn input:checked ~ .checkbox:after {
        display: block;
    }

    /* style tick/checkmark (just a shitty test atm) */
    .btn .checkbox:after {
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
