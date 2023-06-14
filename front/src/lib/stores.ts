import { writable } from "svelte/store";

// todo: focus functions need to loop through existing
// windows and get/drop focus of other windows

export class Window {
    name: string;
    icon: string;
    focused: boolean = false;
    minimised: boolean = false;

    constructor(name: string, focused?: boolean, minimised?: boolean) {
        this.name = name;
        this.icon = (this.name.includes(' layout')) ? 'keymap-icon.png' : name + '-icon.png';
        if (focused) this.focused = focused;
        if (minimised) this.minimised = minimised;
    }

    toggleMinimise(store: Window[]) {
        this.minimised = !this.minimised;

        if (!this.minimised) this.getFocus(store);
        else this.focused = false;
    }

    taskbarClk(store: Window[]) {
        !this.focused && !this.minimised
            ? this.getFocus(store)
            : this.toggleMinimise(store);
    }
    
    getFocus(store: Window[]) {
        this.focused = true;

        for (let window of store) {
            if (this.name !== window.name) window.focused = false;
        }
    }
}

export function createWindow(name: string, focused?: boolean, minimised?: boolean) {
    const window = new Window(name, focused, minimised);

    windowStore.update((store) => [...store, window]);

    return window;
}

export const windowStore = writable<Window[]>([]);
