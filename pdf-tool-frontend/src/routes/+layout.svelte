<!-- 
<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()} -->

<nav style="padding: 1rem; background: #eee; margin-bottom: 1rem;">
    <a href="/" style="margin-right: 1rem;">Home</a>
    <a href="/split" style="margin-right: 1rem;">Split</a>
</nav>

<slot /> 