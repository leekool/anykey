import { writable, get } from "svelte/store";
import exampleJson from "$lib/keymap/example.json?raw";
import html2canvas from "html2canvas";

interface KeymapInfo {
    fileName: string,
    filePath: string,
    fileSize: string,
}

export class Keymap {
    layout: string;
    info: KeymapInfo;

    static store = writable<Keymap[]>([]);

    constructor(layout: string, info: KeymapInfo) {
        this.layout = layout;
        this.info = info;

        Keymap.store.update(s => {
            const removeId = (l: string) => { // removes ID in ```<svg id="">```
                const id = l.match(/"([^"]*)"/)?.[1] as string;
                return l.replace(id, "");
            };

            const keymapExists = s.some(item => removeId(item.layout) === removeId(this.layout));
            return keymapExists ? s : [...s, this];
        });
    }

    static screenshotCanvas = async (keymap: Keymap): Promise<File | null> => {
        const layout = keymap.layout;
        if (!keymap.layout) return null;

        // Get the id from the <svg> element
        const svgId = layout.substring(layout.indexOf("id=") + 4, layout.indexOf("<style>") - 2);
        const el: HTMLElement | null | undefined = document.getElementById(svgId)?.parentElement;
        const svgAssets = document.querySelectorAll("img");

        if (!el) return null; 

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
        downloadData(file, this.name);
        return file;
    };
}

const downloadData = (blob: Blob, name: string) => {
    let a = document.createElement("a");
    document.body.append(a);
    a.download = name;
    a.href = URL.createObjectURL(blob);
    a.click();
    a.remove();
};

export const keymapStore = Keymap.store; 

// example keymap
const exampleKeymap = new Keymap(
    JSON.parse(exampleJson).message,
    {
        fileName: "example.c",
        filePath: "ferris/sweep",
        fileSize: "15kB",
    }
);

