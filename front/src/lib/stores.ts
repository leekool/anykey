import { writable } from "svelte/store";

// todo: focus functions need to loop through existing
// windows and get/drop focus of other windows
let count: number = 1;

export class Window {
    name: string;
    icon: string;
    id: number;
    focused: boolean = false;
    minimised: boolean = false;

    constructor(name: string, focused?: boolean, minimised?: boolean) {
        this.name = name;
        this.icon = (this.name.includes(' layout')) ? 'keymap-icon.png' : name + '-icon.png';

        if (focused) this.focused = focused;
        if (minimised) this.minimised = minimised;
        
        this.id = count;
        count++
    }

    toggleMinimise(store: Window[]): void {
        this.minimised = !this.minimised;

        this.minimised ? this.dropFocus(store) : this.getFocus(store);
    }

    taskbarClk(store: Window[]): void {
        !this.focused && !this.minimised
            ? this.getFocus(store)
            : this.toggleMinimise(store);
    }

    // focuses target window and unfocuses all other windows
    getFocus(store: Window[]): void {
        this.focused = true;

        for (let window of store) {
            if (this.id !== window.id) window.focused = false;
        }
    }

    // unfocuses target window and focuses next unminimised window (if any)
    dropFocus(store: Window[]): void {
        this.focused = false;

        for (let window of store) {
            if (this.id === window.id || window.minimised) continue;

            window.focused = true;
            break;
        }
    }

}

export function createWindow(name: string, focused?: boolean, minimised?: boolean) {
    const window = new Window(name, focused, minimised);

    windowStore.update((store) => [...store, window]);

    return window;
}

export const windowStore = writable<Window[]>([]);
