import { writable } from "svelte/store";
import html2canvas from "html2canvas";

let count: number = 0;

export interface Options {
    focused?: boolean,
    minimised?: boolean,
    maximised?: boolean,
    type?: string,
    navbarMaximise?: boolean,
    navbarMinimise?: boolean
    navbarInfo?: boolean
}

export class Window {
    name: string;
    content: string;
    icon: string;
    id: number;
    // position?: DOMRect;
    position?: Partial<DOMRect>;

    options: Options = {
        focused: true,
        minimised: false,
        maximised: false,
        type: 'window-main',
        navbarMaximise: false,
        navbarMinimise: true,
        navbarInfo: false
    };

    constructor(name: string, content: string, options?: Options) {
        this.name = name;
        this.content = content;
        this.icon = (this.name.includes(' layout')) ? 'keymap-icon.png' : name + '-icon.png';
        this.options = { ...this.options, ...options };

        this.id = count;
        count++
    }

    toggleMinimise(store: Window[]): void {
        this.options.minimised = !this.options.minimised;

        this.options.minimised ? this.dropFocus(store) : this.getFocus(store);
    }

    toggleMaximise(): void {
        this.options.maximised = !this.options.maximised;
    }

    taskbarClk(store: Window[]): void {
        !this.options.focused && !this.options.minimised
            ? this.getFocus(store)
            : this.toggleMinimise(store);
    }

    // focuses target window and unfocuses all other windows
    getFocus(store: Window[]): void {
        this.options.focused = true;

        for (let window of store) {
            if (this.id !== window.id) window.options.focused = false;
        }
    }

    // unfocuses target window and focuses next unminimised window (if any)
    dropFocus(store: Window[]): void {
        this.options.focused = false;

        for (let window of store) {
            if (this.id === window.id || window.options.minimised) continue;

            window.options.focused = true;
            break;
        }
    }

    screenshotCanvas = async (element: string): Promise<File | null> => {
        // Get the id from the <svg> element
        const svgId = element.substring(element.indexOf("id=") + 4, element.indexOf("<style>") - 2)
        const el: HTMLElement | null | undefined = document.getElementById(svgId)?.parentElement;
        const svgAssets = document.querySelectorAll('img');
        
        if (el) {
            const canvas = await html2canvas(el, {
                allowTaint: true,
                useCORS: true,
                logging: true,
                imageTimeout: 0,
                onclone: (doc) => {
                    svgAssets.forEach((asset) => {
                        console.log('assets', asset, asset.width, asset.height)
                        const img = doc.createElement('img');
                        img.src = asset.src;
                        img.width = asset.width;
                        img.height = asset.height;
                        doc.body.appendChild(img);
                    });
                }
            });

            const blob = await new Promise((resolve) => canvas.toBlob(resolve));
            // TODO handle error if blob is null somehow
            const file = new File([blob as BlobPart], 'thumbnail.png', { type: 'image/png' });
            this.downloadData(file, this.name);
            return file;
        }
        return null;
    }

    downloadData(blob: Blob, name: string){
        var a = document.createElement('a');
        document.body.append(a);
        a.download = name;
        a.href = URL.createObjectURL(blob);
        a.click();
        a.remove();
    }
}

export function createWindow(name: string, content: string, options?: Options) {
    const window = new Window(name, content, options);

    windowStore.update((store) => [...store, window]);

    return window;
}

export const windowStore = writable<Window[]>([]);
