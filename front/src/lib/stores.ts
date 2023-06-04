import { writable } from "svelte/store";

// todo: focus functions need to loop through existing
// windows and get/drop focus of other windows

export class Window {
    focused: boolean = false;
    minimised: boolean = false;

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

const windows = writable<any>([]);

export function createWindow() {
    const window = new Window();

    windows.update((store) => [...store, window]);

    return window;
}

export let windowStore: any = windows;
