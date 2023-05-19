<!-- <div class="taskbar"> -->
<!--         <div class="start-button"> -->
<!--             <span>></span> -->
<!--             <div class="start-menu-container"> -->
<!--                 <div class="start-menu" #startMenu> -->
<!--                     <div *ngFor="let window of windowList" -->
<!--                          class="start-menu-item" -->
<!--                          (click)="startMenuPress(window)"> -->
<!--                         <img [src]="window.taskbarIcon"> -->
<!--                         <span>{{window._title}}</span> -->
<!--                     </div> -->
<!--                     <hr class="divider"> -->
<!--                     <div class="start-menu-item" -->
<!--                          routerLink="/shutdown"> -->
<!--                         <img src="../assets/icons/shutdown-icon-small.png"> -->
<!--                         <span>shutdown</span> -->
<!--                     </div> -->
<!--                 </div> -->
<!--             </div> -->
<!--         </div> -->
<!--     <div class="iconman"> -->
<!--         <div *ngFor="let window of windowList"> -->
<!--             <div *ngIf="!window.closed" -->
<!--                  class="iconman-button" -->
<!--                  [ngClass]="{'iconman-button-active': !window.minimised && window.focus}" -->
<!--                  (click)="iconmanPress(window)"> -->
<!--                 <img [src]="window.taskbarIcon"> -->
<!--                 <span>{{window._title}}</span> -->
<!--             </div> -->
<!--         </div> -->
<!--     </div> -->
<!-- </div> -->
<script lang="ts">
    export let windowMain: any;

    const iconmanClk = (window: any) => {
        !window.focused && !window.minimised
            ? window.getFocus()
            : window.toggleMinimise();
    };

    function testFocus() {
        return windowMain.focused;
    }
</script>

<div class="taskbar">
    <div class="iconman">
        <div class="{testFocus() ? 'iconman-button iconman-button-active' : 'iconman-button iconman-button-inactive'}" 
            on:click={() => {
                iconmanClk(windowMain);
                testFocus()
            }} 
        />
    </div>
</div>

<style>
    .taskbar {
        display: flex;
        position: fixed;
        height: 34px;
        width: 100%;
        justify-content: space-between;
        left: 50%;
        bottom: 0;
        margin-left: -50%;
        font-family: "Tamzen", sans-serif;
        font-size: 15px;
        color: #222020;
        background-image: url("images/footer-tile.svg");
        background-repeat: repeat;
        border-top: 2px solid #222020;
        box-shadow: 2px 2px #fffefe inset, -2px -2px #948c79 inset;
        z-index: 10;
    }

    .taskbar span {
        margin-top: 3px;
    }

    .start-button {
        display: flex;
        gap: 20px;
        align-items: center;
        justify-content: center;
        width: 60px;
        user-select: none;
        box-shadow: -1px -1px #948c79 inset, -1px 0 0 0 #fffefe inset;
    }

    .start-button:hover,
    .start-button:focus {
    }

    .start-menu-container {
        display: none;
        position: absolute;
        left: 0;
        padding: 10px 10px 10px 0;
    }

    .start-menu {
        position: absolute;
        flex-direction: column;
        gap: 4px;
        bottom: 25px;
        padding: 4px;
        min-width: 10%;
        background-image: url("src/assets/images/pixmaps/menu-tile.png");
        background-repeat: repeat;
        box-shadow: 1px 1px #fffefe inset, -1px -1px #948c79 inset;
        outline: 1px solid #222020;
    }

    .start-button:hover .start-menu-container {
        display: flex;
    }

    .start-menu-item {
        display: flex;
    }

    .start-menu-item span {
        padding-right: 5px;
    }

    .start-menu-item:hover,
    .start-menu-item:focus {
        background: rgba(4, 4, 252, 0.3);
        color: #fffefe;
        box-shadow: -1px -1px #aeabd9 inset, 1px 1px #8680c6 inset;
        outline: 1px dotted rgba(255, 254, 254, 0.5);
    }

    .divider {
        height: 1px;
        margin: 3px 0;
        border: none;
        background-color: #948c79;
    }

    .iconman {
        display: flex;
        width: 100%;
        box-sizing: border-box;
        box-shadow: -1px -1px #948c79 inset, 1px 1px #fffefe inset;
    }

    .iconman-button {
        display: flex;
        align-items: center;
        width: 270px;
        margin: 4px 0 5px 5px;
        cursor: pointer;
        user-select: none;
    }

    .iconman-button img,
    .start-menu-item img {
        max-height: 13px;
        margin: 4px;
        image-rendering: pixelated;
    }

    .iconman-button-inactive {
        color: #000;
        background-image: none;
        box-shadow: none;
    }

    .iconman-button-active {
        color: #fffefe;
        background-image: url("images/menu-tile-hover.png");
        box-shadow: -1px -1px #92998b inset, 1px 1px #5c6057 inset;
    }

    @media screen and (max-width: 700px) {
        .iconman {
            padding-right: 5px;
            overflow-y: hidden;
            overflow-x: scroll;
            -ms-overflow-style: none;
            scrollbar-width: none;
        }

        .iconman::-webkit-scrollbar {
            display: none;
        }

        .iconman-button {
            width: 130px;
        }
    }
</style>
