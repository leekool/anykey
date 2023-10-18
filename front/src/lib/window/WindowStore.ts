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
    navbarClose?: boolean,
    navbarInfo?: boolean,
    layoutInfo?: LayoutInfo
}

interface LayoutInfo {
    svg: string,
    name: string,
    fileName: string,
    filePath: string,
    fileSize: string
}

export class Window {
    name: string;
    icon: string;
    id: number;
    element: Node = (null as any) as Node;
    position?: Partial<{ -readonly [K in keyof DOMRect]: DOMRect[K] }>;

    options: Options = {
        focused: true,
        minimised: false,
        maximised: false,
        type: 'window-main',
        navbarMaximise: false,
        navbarMinimise: true,
        navbarClose: false,
        navbarInfo: false,
        layoutInfo: {
            svg: '',
            name: '',
            fileName: '',
            filePath: '',
            fileSize: ''
        }
    };

    constructor(name: string, options?: Options) {
        this.options = { ...this.options, ...options };

        this.name = name;
        this.icon = (this.options.type?.includes('layout')) ? 'keymap-icon.png' : name + '-icon.png';

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

    screenshotCanvas = async (): Promise<File | null> => {
        const layout = this.options.layoutInfo?.svg;
        if (!layout) return null;

        // Get the id from the <svg> element
        const svgId = layout.substring(layout.indexOf("id=") + 4, layout.indexOf("<style>") - 2)
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

    downloadData(blob: Blob, name: string) {
        let a = document.createElement("a");
        document.body.append(a);
        a.download = name;
        a.href = URL.createObjectURL(blob);
        a.click();
        a.remove();
    }
}

export function createWindow(name: string, options?: Options) {
    const window = new Window(name, options);

    windowStore.update((store) => [...store, window]);

    return window;
}

export function killWindow(window: Window) {
    windowStore.update((store) => {
        store.forEach(w => {
            if (w.id !== window.id - 1) return;
            w.options.focused = true; // focus next window
        });

        return store.filter(w => w.id !== window.id); // remove window from store
    });

    window.element.parentNode?.removeChild(window.element); // remove window from DOM
}

export const windowStore = writable<Window[]>([]);
