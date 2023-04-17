<script lang="ts">
    export let menuOpen: boolean;
</script>

<button on:click class="dropbtn">
    { !menuOpen ? "keyboard menu ▼" : "close menu ▲" }
</button>

<style>
    @import url("../../static/fonts/real-icons.css");
    /* Dropdown Button */
    .dropbtn {
        font-family: "Tamzen", sans-serif;
        background-color: brown;
        color: white;
        font-size: 15px;
        cursor: pointer;
        border: 1px solid #ccc;
        padding: 3px 6px;
    }

    /* Dropdown button on hover & focus */
    .dropbtn:hover,
    .dropbtn:focus {
        background-color: #3e8e41;
    }
</style>
