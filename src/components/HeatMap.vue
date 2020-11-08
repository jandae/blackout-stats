<template>
    <calendar-heatmap :values="days" :end-date="new Date()" tooltip-unit="power interuptions" :max="7" :range-color="['fff', '969842', '494a20', '522d2d', '1f1f1f', '000']"/>
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
