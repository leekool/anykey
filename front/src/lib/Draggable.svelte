<script lang="ts">
	export let dragLeft: number = 0;
	export let dragTop: number = 0;
	
	let moving = false;
	
	function onMouseDown() {
		moving = true;
	}
	
	function onMouseMove(e: MouseEvent) {
		if (moving) {
			dragLeft += e.movementX;
			dragTop += e.movementY;
		}
	}
	
	function onMouseUp() {
		moving = false;
	}
	
// 	$: console.log(moving);
</script>

<style>
	.draggable {
        position: absolute;
		user-select: none;
		cursor: move;
	}
</style>

<section on:mousedown={onMouseDown} style="left: {dragLeft}px; top: {dragTop}px;" class="draggable">
	<slot></slot>
</section>

<svelte:window on:mouseup={onMouseUp} on:mousemove={onMouseMove} />
