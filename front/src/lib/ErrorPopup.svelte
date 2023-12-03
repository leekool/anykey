<script lang="ts">
    export let errorMessage: string;

    const submitForm = (event: Event) => {
        console.log("clicked ok")
    };
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="main">
    <fieldset>
        <legend>Error</legend>
        <div class="check-btn">
            {{ errorMessage }}
        </div>
        <div
        class="submit-btn pixel-corners"
        on:click|preventDefault={(e) => submitForm(e)}
        >
        <label>
            <input class="" type="submit" />
            OK
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

    .submit-btn {
        letter-spacing: 1px;
        display: flex;
        align-items: center;
        box-sizing: border-box;
        font-family: "Tamzen", sans-serif;
        height: 27px;
        font-size: 15px;
        cursor: pointer;
        padding: 2px 8px;
        background-color: #e0e0e0;
        max-width: 10%;
    }

    .submit-btn > * {
        user-select: none;
        cursor: pointer;
    }    
</style>
