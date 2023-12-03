<script lang="ts">
    import WindowComp from "$lib/window/Window.svelte";
    import { Window } from "$lib/window/WindowStore";

    import LayoutGen from "$lib/layout_gen/LayoutGen.svelte";
    import Taskbar from "$lib/Taskbar.svelte";

    import { onMount } from "svelte";

    onMount(async () => {
        Window.isMobile = (window.innerWidth <= 600 && window.innerHeight <= 800); 
    });
</script>

<WindowComp 
    name="layout_gen"
    slot={{
        component: LayoutGen,
        props: null
    }}
/>

<Taskbar />

<style>
</style>
