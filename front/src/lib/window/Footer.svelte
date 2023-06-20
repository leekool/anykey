<script lang="ts">
    import type { Window } from "./WindowStore";

    export let window: Window;
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="footer"
     class:inactive={!window.focused}>
    <div class="footer-btn-container">
        <div class="footer-btn">
            <div class="left-arrow" />
        </div>
        <div class="separator" />
        <div class="footer-scroll-btn">
            <div class="scroll-img" />
        </div>
    </div>
    <div class="footer-bg" />
    <div class="separator" />
    <div class="footer-btn">
        <div class="right-arrow" />
    </div>
</div>

<style>

    .footer {
        display: flex;
        justify-items: space-between;
        box-sizing: border-box;
        height: 24px;
        min-height: 24px;
        user-select: none;
        box-shadow: 0 -2px 0 0 #000, 0 -4px 0 0 #a3a3d7;
    }

    .footer-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        align-items: center;
        justify-content: center;
        background-color: #d5d5d5;
        box-sizing: border-box;
        border-color: #fff #a0a0a0 #a0a0a0 #fff;
        border-style: solid;
        border-width: 2px;
    }

    .footer-btn-container {
        display: flex;
        aspect-ratio: 2 / 1;
        box-sizing: border-box;
        /* justify-content: center; */
    }

    .footer-scroll-btn {
        display: flex;
        height: 100%;
        aspect-ratio: 1 / 1;
        box-sizing: border-box;
        align-items: center;
        justify-content: center;
        background-color: #aaaaaa;
        border-color: #ccccff #333366 #333366 #ccccff;
        border-style: solid;
        border-width: 2px;
        z-index: 10;
    }

    .footer-bg {
        height: calc(100% - 2px);
        width: 100%;
        background-image: url("images/footer-tile.svg");
    }

    .scroll-img {
        display: flex;
        height: 70%;
        width: 70%;
        content: url("images/footer-scroll.svg");
        border-left: 1px solid #a3a3d7;
        margin-right: 1px;
    }

    .left-arrow {
        display: flex;
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        /* filter: saturate(0%) brightness(100%) contrast(80%); */
    }

    .right-arrow {
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        transform: rotate(180deg);
    }

    .separator {
        background-color: #000;
        min-width: 2px;
        z-index: 10;
    }

    .inactive {
        box-shadow: 0 -2px 0 0 #000, 0 -4px 0 0 #a7a7a7;
    }

    .inactive .left-arrow,
    .inactive .right-arrow,
    .inactive .scroll-img {
        filter: saturate(0%) brightness(100%) contrast(80%);
    }

    .inactive .footer-scroll-btn {
        border-color: #d0d0d0 #454545 #454545 #d0d0d0;
    }
</style>
