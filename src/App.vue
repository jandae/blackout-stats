<template>
	<div id="app">
		<Home/>
	</div>
</template>

<script>
import Home from './components/Home.vue'

export default {
	name: 'App',
	components: {
		Home
	}
}
</script>

<style lang="scss">
body {
	background: #171717;
	color: #fffde5;
	font-family: 'Roboto', Arial, sans-serif;
	text-align: center;
	text-transform: uppercase;

	ul {
		list-style-type: none;
		margin: 0;
		padding: 0;
	}

	.number {
		font-family: 'Teko', Arial, sans-serif;;
	}
}
</style>
