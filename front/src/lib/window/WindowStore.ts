import { writable, get } from "svelte/store";
import type WindowComponent from "$lib/window/Window.svelte";
import html2canvas from "html2canvas";

let count: number = 0;

export class Position {
    height = 0;
    width = 0;
    top = 0;
    left = 0;
    topPercent = 50;
    leftPercent = 50;

    constructor(top: number, left: number) {
        this.topPercent = top;
        this.leftPercent = left;
    }
}

export class Options {
    focused = true;
    minimised = false;
    maximised = false;
    type = "main"; // probably redundant
    navbar = {
        maximise: false,
        minimise: true,
        close: false,
        info: false
    }
    layoutInfo = {
        name: "",
        svg: "",
        fileName: "",
        filePath: "",
        fileSize: ""
    }
}

export class Window {
    name: string;
    icon: string;
    id: number;
    component: any;
    position: Position;
    options: Options;
    zIndex: number = 0;

    static windowStore = writable<Window[]>([]);
    static focusList: number[] = [];
    static isMobile = false;

    constructor(name: string, component: WindowComponent, options?: Partial<Options>, position?: Partial<Position>) {
        // Window.windowStore.update((store) => [...store, this]);

        this.options = new Options();
        Object.assign(this.options, options);

        this.component = component;
        this.name = name;

        this.icon = (this.options.type?.includes("layout")) ? "keymap-icon.png" : name + "-icon.png";
        this.position = new Position(position?.topPercent || 50, position?.leftPercent || 50);

        this.id = count; // simple ID system for now
        count++

        if (!this.options.minimised) this.getFocus();

        Window.windowStore.update((store) => {
            // windowExists prevents duplication on navigation, need to have a better check rather than name though 
            // const windowExists = store.some(item => item.name === this.name);
            // return windowExists ? store : [...store, this];

            return [...store, this];
        });

        Window.updateZIndex();
    }

    static updateZIndex(): void {
        const store = get(Window.windowStore);

        for (let window of store) {
            const index = Window.focusList.indexOf(window.id);
            if (index === -1) continue;

            window.zIndex = 10 + -index;
        }
    }

    toggleMinimise(): void {
        this.options.minimised = !this.options.minimised;

        if (this.options.minimised) {
            const index = Window.focusList.indexOf(this.id);
            Window.focusList.splice(index, 1); // remove from focusList
        }

        this.options.minimised ? this.dropFocus() : this.getFocus();
    }

    toggleMaximise(): void {
        this.options.maximised = !this.options.maximised;
    }

    taskbarClk(): void {
        !this.options.focused && !this.options.minimised
            ? this.getFocus()
            : this.toggleMinimise();
    }

    // focuses target window and unfocuses all other windows
    getFocus(): void {
        const store = get(Window.windowStore);

        this.options.focused = true;

        if (!Window.isMobile) {
            // focus element (after 100ms to account for opening windows)
            // setTimeout(() => this.options.focusEle?.focus(), 100);
        }

        // update focusList
        const index = Window.focusList.indexOf(this.id);
        if (index !== -1) Window.focusList.splice(index, 1);
        Window.focusList.unshift(this.id);

        // drop focus of other windows
        for (let window of store) {
            if (this.id !== window.id) window.dropFocus(false);
        }
    }

    // unfocuses target window and focuses next unminimised window (if any)
    dropFocus(focusNext = true): void {
        const store = get(Window.windowStore);

        this.options.focused = false;

        Window.updateZIndex();

        if (!focusNext) return;

        // focus next window
        const index = store.findIndex(w => w.id === Window.focusList[0]);
        if (index !== -1) store[index].getFocus();
    }

    kill() {
        const index = Window.focusList.indexOf(this.id);
        Window.focusList.splice(index, 1);

        Window.windowStore.update((store) => {
            const index = store.findIndex(w => w.id === this.id);

            store[index].dropFocus(); // focus next window
            store = store.filter(w => w.id !== this.id); // remove window from store

            return store;
        });

        this.component.$destroy(); // remove window from DOM
    }

    async screenshotCanvas(): Promise<File | null> {
        const layout = this.options.layoutInfo?.svg;
        if (!layout) return null;

        // Get the id from the <svg> element
        const svgId = layout.substring(layout.indexOf("id=") + 4, layout.indexOf("<style>") - 2);
        const el: HTMLElement | null | undefined = document.getElementById(svgId)?.parentElement;
        const svgAssets = document.querySelectorAll("img");
        
        if (el) {
            const canvas = await html2canvas(el, {
                allowTaint: true,
                useCORS: true,
                logging: true,
                imageTimeout: 0,
                onclone: (doc) => {
                    svgAssets.forEach((asset) => {
                        console.log("assets", asset, asset.width, asset.height);
                        const img = doc.createElement("img");
                        img.src = asset.src;
                        img.width = asset.width;
                        img.height = asset.height;
                        doc.body.appendChild(img);
                    });
                }
            });

            const blob = await new Promise((resolve) => canvas.toBlob(resolve));
            // TODO handle error if blob is null somehow
            const file = new File([blob as BlobPart], "thumbnail.png", { type: "image/png" });
            this.downloadData(file, this.name);
            return file;
        }
        return null;
    }

    downloadData(blob: Blob, name: string) {
        let a = document.createElement("a");
        document.body.append(a);
        a.download = name;
        a.href = URL.createObjectURL(blob);
        a.click();
        a.remove();
    }
}

export const windowStore = Window.windowStore;
