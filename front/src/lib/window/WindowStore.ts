import { writable } from "svelte/store";

let count: number = 0;

export interface Options {
    focused?: boolean,
    minimised?: boolean,
    maximised?: boolean,
    type?: string,
    navbarMaximise?: boolean,
    navbarMinimise?: boolean
}

export class Window {
    name: string;
    icon: string;
    id: number;

    options: Options = {
        focused: true,
        minimised: false,
        maximised: false,
        type: 'window-main',
        navbarMaximise: false,
        navbarMinimise: true
    };

    constructor(name: string, options?: Options) {
        this.name = name;
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

}

export function createWindow(name: string, options?: Options) {
    const window = new Window(name, options);

    windowStore.update((store) => [...store, window]);

    return window;
}

export const windowStore = writable<Window[]>([]);
