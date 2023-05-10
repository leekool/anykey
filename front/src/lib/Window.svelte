<script lang="ts">
    export let position: string = "position-main";
    let minimised: boolean = false;

    export const minimise = () => {
        minimised = true;
    }
</script>

<div class="{minimised ? 'minimised' : position}">
    <div class="main pixel-corners">
        <div class="navbar">
            <div class="navbar-title">layout_gen</div>
            <div class="navbar-bg" style="width: 14px;" />
            <div class="navbar-btn-base">
                <div class="navbar-btn-inner" />
            </div>
            <div class="navbar-bg" />
            <div class="navbar-btn-base">
                <div
                    class="navbar-btn-inner navbar-btn-right"
                    on:click={() => minimise()}
                />
            </div>
            <div class="navbar-bg" style="width: 14px;" />
        </div>

        <div class="content">
            <slot />
        </div>

        <div class="footer">
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
    </div>
</div>

<style>
    @import url("../../static/pixel-corners.css");

    *::-webkit-scrollbar {
        display: none;
    }

    .minimised {
        display: none;
        visibility: hidden;
        z-index: 0;
    }

    .main {
        display: flex;
        flex: 1 1 auto;
        flex-direction: column;
        font-family: "Tamzen", sans-serif;
        background-color: #d5d5d5;
    }

    .navbar {
        display: flex;
        height: 34px;
        font-size: 16px;
        align-items: center;
        justify-content: space-between;
        user-select: none;
        border-color: #ccccff #a3a3d7 #a3a3d7 #ccccff;
        border-style: solid;
        border-width: 2px;
        box-sizing: border-box;
        box-shadow: 0 2px 0 0 #000;
        padding-bottom: 1px;
    }

    .navbar-bg {
        box-shadow: 0 2px 0 0 #a4a4a4 inset, 0 4px 0 0 #d5d5d5 inset,
            0 6px 0 0 #a4a4a4 inset, 0 8px 0 0 #d5d5d5 inset,
            0 10px 0 0 #a4a4a4 inset, 0 12px 0 0 #d5d5d5 inset,
            0 14px 0 0 #a4a4a4 inset, 0 16px 0 0 #d5d5d5 inset,
            0 18px 0 0 #a4a4a4 inset, 0 20px 0 0 #d5d5d5 inset,
            0 22px 0 0 #a4a4a4 inset;
        width: 100%;
        height: 22px;
    }

    .navbar-title {
        position: absolute;
        height: 30px;
        line-height: 30px;
        padding: 0 12px;
        left: 50%;
        transform: translate(-50%);
        font-weight: bold;
        color: #000;
        background-color: #d5d5d5;
        text-shadow: 0 1px rgba(138, 134, 160, 0.7);
    }

    .navbar-btn-base {
        display: flex;
        height: 22px;
        aspect-ratio: 1 / 1;
        margin: 4px;
        align-items: center;
        justify-content: center;
        background-color: #ccccff;
        box-shadow: 2px 2px 0 0 #333366 inset;
        cursor: pointer;
    }

    .navbar-btn-inner {
        display: flex;
        height: 16px;
        aspect-ratio: 1 /1;
        margin-left: 2px;
        margin-top: 2px;
        background-color: #a4a4a4;
        box-shadow: -2px -2px 0 0 #333366 inset;
    }

    .navbar-btn-right {
        box-shadow: -2px -2px 0 0 #333366 inset, -6px -6px 0 0 #a4a4a4 inset,
            -8px -8px 0 0 #333366 inset;
    }

    .content {
        display: flex;
        flex: 1 1 auto;
        align-self: center;
        flex-direction: column;
        background-color: #d5d5d5;
        margin: 2px 4px;
        width: 100%;
        overflow: scroll;
    }

    .footer {
        display: flex;
        justify-items: space-between;
        box-sizing: border-box;
        height: 28px;
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

    .separator {
        background-color: #000;
        min-width: 2px;
        z-index: 10;
    }

    .position-main {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        min-height: 300px;
        width: 80%;
        max-width: 500px;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
    }

    .position-layout {
        display: flex;
        flex: 1 1 auto;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -52.5%);
        transform: translate(-50%, -52.5%);
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
        max-height: 80%;
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
    }

    .right-arrow {
        height: 80%;
        width: 80%;
        content: url("images/left-arrow.svg");
        transform: rotate(180deg);
    }
</style>
