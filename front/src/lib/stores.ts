import { writable } from "svelte/store";

// todo: focus functions need to loop through existing
// windows and get/drop focus of other windows

export class Window {
    name: string;
    focused: boolean = false;
    minimised: boolean = false;

    constructor(name: string) {
        this.name = name;
    }
    
    toggleMinimise() {
        this.focused = !this.minimised;
        this.minimised = !this.minimised;
    }

    taskbarClk() {
        !this.focused && !this.minimised
            ? this.focused = true
            : this.toggleMinimise();
    }
}

export function createWindow(name: string) {
    const window = new Window(name);

    windowStore.update((store) => [...store, window]);

    return window;
}

export const windowStore = writable<Window[]>([]);
