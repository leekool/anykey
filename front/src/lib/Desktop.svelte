<script lang="ts">
    import { assets } from "$app/paths";

    import { windowStore, Window } from "$lib/window/WindowStore";
    import WindowComponent from "$lib/window/Window.svelte";
    import { Keymap, keymapStore } from "$lib/keymap/KeymapStore";
    import KeymapComponent from "$lib/keymap/Keymap.svelte";

    // TODO: 
    //    - refactor desktopIcons to not necessarily have to be keymaps
    //    - types for icons

    let desktopIcons: any[] = [
        {
            name: "github",
            options: {
                type: "github",
                highlight: false
            }
        }
    ];

    $: $keymapStore, checkKeymaps();

    const checkKeymaps = () => {
        const newKeymaps = $keymapStore.filter(keymap => !desktopIcons.slice(1).some(d => d.slot.props.info.fileName === keymap.info.fileName));
        newKeymaps.forEach(keymap => initProgram(keymap));

        desktopIcons = desktopIcons;
    };

    const toggleHighlight = (icon: any) => {
        icon.options.highlight = !icon.options.highlight;
        desktopIcons = desktopIcons; // trigger change detection

        $windowStore = $windowStore;
    }

    const clearHighlight = () => {
        desktopIcons.forEach((icon: any) => {
            icon.options.highlight = false;
        });

        desktopIcons = desktopIcons; // trigger change detection
    }

    let clickCount = 0;

    const handleClick = (icon: any) => {
        let clickTimer: ReturnType<typeof setTimeout>;

        toggleHighlight(icon);

        clickCount++;

        if (clickCount === 1) {
            clickTimer = setTimeout(() => {
                clickCount = 0;
                clearTimeout(clickTimer);
            }, 200);
        } else if (clickCount === 2) {
            if (icon.options.type === "github") {
                return window.open("https://github.com/leekool/layout_generator");
            }

            const windowMatch = $windowStore.find(window => window.name === icon.name);

            if (!windowMatch) return openWindow(icon);

            if (windowMatch.options.minimised) windowMatch.toggleMinimise();
            else if (!windowMatch.options.focused) windowMatch.getFocus();
        }
    }

    const openWindow = (icon: any) => {
        // find the highest level div ("contents") and create a child div as the target
        const contentDiv = document.querySelector("div[style='display: contents']")!;
        const target = document.createElement("div"); 
        contentDiv.appendChild(target);

        new WindowComponent({
            target,
            props: icon
        });
    }

    const initProgram = (keymap: Keymap) => {
         desktopIcons.push({
            name: keymap.info.fileName,
            options: {
                type: "keymap",
                layout: keymap.layout,
                maximised: false,
                highlight: false,
                navbar: {
                    minimise: true,
                    maximise: true,
                    close: true,
                    info: true
                }
            },
            slot: {
                component: KeymapComponent,
                props: {
                    layout: keymap.layout,
                    info: {
                        fileName: keymap.info.fileName,
                        filePath: keymap.info.filePath,
                        fileSize: keymap.info.fileSize,
                    }
                }
            }
        });
    }
</script>

<!-- preload icons -->
<svelte:head>
   <!-- <link rel="preload" as="image" href={`${assets}/images/icons/keymap-icon-56-highlight.png`} /> -->
   <!-- <link rel="preload" as="image" href={`${assets}/images/icons/github-icon-56-highlight.png`} /> -->
</svelte:head>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="desktop" on:click={() => clearHighlight()}>
    <div class="icon-container" on:click|stopPropagation>
        {#each desktopIcons as icon}
            <div
                class="desktop-icon"
                on:click|stopPropagation={() => handleClick(icon)}
            >
                {#if !icon.options.highlight}
                    <img src={`${assets}/images/icons/${icon.options.type}-icon-56.png`} alt={icon.name} />
                {/if}
                {#if icon.options.highlight}
                    <img class="highlight" src={`${assets}/images/icons/${icon.options.type}-icon-56.png`} alt={icon.name} />
                    <!-- <img src={`${assets}/images/icons/${icon.options.type}-icon-56-highlight.png`} alt={icon.name} /> -->
                {/if}
                <span class:desktop-icon-highlight={icon.options.highlight}>
                    {icon.name}
                </span>
            </div>
        {/each}
    </div>

</div>

<style>
    .desktop {
        display: flex;
        width: 100%;
        height: 100vh;
        font-size: 15px;
    }

    .highlight {
        filter: saturate(3) hue-rotate(8deg) contrast(110%);
        mix-blend-mode: overlay;
        /* mix-blend-mode: hard-light; */
    }

    .git-icon {
        position: absolute;
        right: 0;
        bottom: 0;
        margin: 0 20px 30px 0;
    }

    .icon-container {
        display: flex;
        gap: 20px;
        margin: 30px 0 0 20px;
        max-width: 100px;
        height: 0;
        flex-direction: column;
        align-items: center;
        image-rendering: pixelated;
    }
    
    .desktop-icon {
        display: flex;
        height: 102px;
        flex-direction: column;
        align-items: center;
        gap: 4px;
        font-size: 16px;
        text-shadow: 1px 1px #fffefe;
        text-align: center;
        user-select: none;
    }

    .desktop-icon img {
        /* max-width: 80%; */
        /* height: 72px; */
        /* image-rendering: pixelated; */
    }

    .desktop-icon span {
        padding: 2px 4px 0 4px;
        line-height: 16px;
    }

    .desktop-icon-highlight {
        background: rgba(4, 4, 252, 0.3);
        color: #fffefe;
        outline: 1px dotted rgba(255, 254, 254, 0.5);
        text-shadow: none;
    }
</style>
