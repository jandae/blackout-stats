<template>
    <calendar-heatmap :values="days" :end-date="new Date()" tooltip-unit="power interuptions" :max="7" :range-color="['fffde5', '777777', '555555', '333333', '000']"/>
</template>

<script>
// import axios from 'axios'
// const api_server = process.env.VUE_APP_API
import { CalendarHeatmap } from 'vue-calendar-heatmap'

export default {
    name: 'HeatMap',
    components: {
      CalendarHeatmap
    },
    props: ['days'],
	data () {
		return {
			computed_data : {}
		}
	},
	methods: {
		getComputed: function () {
		}
	},
	mounted() {
        // this.days
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
