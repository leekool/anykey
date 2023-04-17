<script lang="ts">
    import Button from "../lib/Button.svelte";
    import Link from "../lib/Link.svelte";
    import Input from "../lib/Input.svelte";

    let inputValue: string = "";
    $: console.log(inputValue);

    let menuOpen: boolean = false;
    let menuItems: { name: string; path: string }[] = [];
    let filteredItems: { name: string; path: string }[] = [];

    const handleInput = () => {
        return (filteredItems = menuItems.filter((item) =>
            item.name.toLowerCase().match(inputValue.toLowerCase())
        ));
    };

    // ---
    import { onMount } from "svelte";

    let file: File;
    let formData = new FormData();
    let fileName: string = "";
    let layoutResponse: string = "";

    let selectedOption: { name: string; path: string } = { name: "", path: "" };

    // let options: [] = [];
    let submitDisabled: boolean = true;
    let btnState: string = "btn-invalid";

    // This is a watcher
    $: if (fileName && selectedOption.name !== "") {
        btnState = "btn-valid";
        submitDisabled = false;
    }

    onMount(async () => {
        // fetch some data from the server when the component is mounted
        const response = await fetch("http://localhost:5000/api/keyboards");
        // options = await response.json();
        // options.forEach((item: any) => {
        //     menuItems.push(item);
        // });
        menuItems = await response.json();
    });

    const onFileSelected = (e: { currentTarget: HTMLInputElement }) => {
        if (e.currentTarget.files) {
            file = e.currentTarget.files[0];
            fileName = file.name;
        }
    };

    // function handleSelect(event: any): any {
    //     selectedOption = event.target?.value;
    // }

    function submitForm(event: any) {
        event.preventDefault(); // prevent default form submission behavior
        console.log("Form submitted!");
        postLayout();
    }

    async function postLayout() {
        formData.append("file", file);
        formData.append("mapPath", selectedOption.path);
        const response = await fetch("http://localhost:5000/api/layout", {
            method: "POST",
            body: formData,
        });
        const json = await response.json();
        layoutResponse = json.message;
        console.log(json.message);
    }
</script>

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
                <div class="form">
                    <!-- <form on:submit={(e) => submitForm(e)}> -->
                    <div class="form-contents">
                        <!-- <div class="select-keyboard"> -->
                        <!--     <select on:change={handleSelect}> -->
                        <!--         <option value="select keyboard" -->
                        <!--             >Select Keyboard</option -->
                        <!--         > -->
                        <!--         {#each options as option} -->
                        <!--             <option value={option["path"]} -->
                        <!--                 >{option["name"]}</option -->
                        <!--             > -->
                        <!--         {/each} -->
                        <!--     </select> -->
                        <!-- </div> -->

                        <div class="select-map">
                            <label>
                                <input
                                    type="file"
                                    accept=".c"
                                    on:change={(e) => onFileSelected(e)}
                                />
                                upload keymap
                            </label>
                            <span>{fileName}</span>
                        </div>

                        <!-- button zone -->
                        <div class="select-keyboard">
                            <Button
                                on:click={() => (menuOpen = !menuOpen)}
                                {menuOpen}
                            />

                            <div class:show={menuOpen} class="dropdown-content">
                                <Input bind:inputValue on:input={handleInput} />
                                <!-- MENU -->
                                {#if filteredItems.length > 0}
                                    {#each filteredItems as item}
                                        <div
                                            on:click={() => {
                                                selectedOption = item;
                                                menuOpen = !menuOpen;
                                            }}
                                            on:keypress={(e) => console.log(e)}
                                        >
                                            <Link link={item.name} />
                                        </div>
                                    {/each}
                                {:else}
                                    {#each menuItems as item}
                                        <div
                                            on:click={() => {
                                                selectedOption = item;
                                                menuOpen = !menuOpen;
                                            }}
                                            on:keypress={(e) => console.log(e)}
                                        >
                                            <Link link={item.name} />
                                        </div>
                                    {/each}
                                {/if}
                            </div>
                        </div>
                        <span>{selectedOption.name}</span>

                        <div
                            class="submit-button"
                            on:click={(e) => submitForm(e)}
                            on:keypress={(e) => console.log(e)}
                        >
                            <label class={btnState}>
                                <input
                                    type="submit"
                                    disabled={submitDisabled}
                                />
                                submit
                            </label>
                        </div>

                        <div class="map-svg">
                            {@html layoutResponse}
                        </div>
                    </div>
                    <!-- </form> -->
                </div>
            </div>
        {/if}
    </div>
</div>

<style>
    @import url("../../static/fonts/real-icons.css");

    .form {
        display: block;
        /* width: 80%; */
        position: absolute;
        top: 3%;
        left: 32%;
        transform: translate(-50%);
        width: 60%;
    }

    .form-contents {
        margin: 0;
    }

    input[type="file"],
    input[type="submit"] {
        display: none;
    }

    label {
        border: 1px solid #ccc;
        /* display: inline-block; */
        padding: 3px 6px;
        cursor: pointer;
    }

    .select-keyboard {
        display: inline-block;
        position: relative;
        /* display: inline-block; */
    }

    .submit-button,
    .select-keyboard,
    .select-map,
    .map-svg {
        margin-top: 10px;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f6f6f6;
        min-width: 230px;
        border: 1px solid #ddd;
        z-index: 1;
    }

    /* Show the dropdown menu */
    .show {
        display: block;
    }

    .map-svg {
        width: 200px;
        height: 200px;
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
        max-height: calc(100% - 29.5px);
        background-color: #c6bb9b;
    }

    .position-centre {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        max-height: 80%;
        width: 80%;
        max-width: 1200px;
    }

    .btn-valid {
        background-color: rgb(153, 255, 153, 50);
    }

    .btn-invalid {
        background-color: rgb(255, 153, 153, 50);
    }
</style>
