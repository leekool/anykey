<script lang="ts">
    import WindowComp from "$lib/window/Window.svelte";
    import { Window } from "$lib/window/WindowStore";

    import LayoutGen from "$lib/layout_gen/LayoutGen.svelte";
    import Taskbar from "$lib/Taskbar.svelte";

    import Desktop from "$lib/Desktop.svelte";
</script>

<Desktop />

<WindowComp 
    name="anykey"
    slot={{
        component: LayoutGen,
        props: null
    }}
/>

<Taskbar />

<style>
</style>
