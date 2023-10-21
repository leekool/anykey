import { writable, get } from "svelte/store";
import html2canvas from "html2canvas";

let count: number = 0;

class Position {
    height = 0;
    width = 0;
    top = 0;
    left = 0;
    topPercent = 50;
    leftPercent = 50;
}

export class Options {
    _focused = true;
    minimised = false;
    maximised = false;
    type = "window-main";
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

    set focused(value: boolean) {
        // if (value === true && this._focused !== true) {
        //     console.log("this", Window.focusList)
        // }

        this._focused = value;
    }

    get focused() { return this._focused; }
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

    constructor(name: string, component: any, options?: Partial<Options>) {
        Window.windowStore.update((store) => [...store, this]);

        this.options = new Options();
        Object.assign(this.options, options);

        this.component = component;
        this.name = name;
        this.icon = (this.options.type?.includes("layout")) ? "keymap-icon.png" : name + "-icon.png";
        this.position = new Position();

        this.id = count; // simple ID system for now
        count++

        this.getFocus();
    }

    toggleMinimise(): void {
        this.options.minimised = !this.options.minimised;

        if (this.options.minimised) {
            const index = Window.focusList.indexOf(this.id);
            Window.focusList.splice(index, 1);
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

        // update focusList
        const index = Window.focusList.indexOf(this.id);
        if (index !== -1) Window.focusList.splice(index, 1);
        Window.focusList.unshift(this.id);

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

        const index = store.findIndex(w => w.id === Window.focusList[0]);
        if (index !== -1) store[index].getFocus();
    }

    static updateZIndex(): void {
        const store = get(Window.windowStore);

        for (let window of store) {
            const index = Window.focusList.indexOf(window.id);
            if (index === -1) continue;

            window.zIndex = 10 + -index;
        }
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
}

// export const windowStore = writable<Window[]>([]);
export const windowStore = Window.windowStore;
