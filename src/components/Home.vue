<template>
	<div class="main">
		<div class="total-section">
			<h2>Total Blackouts</h2>
			<h3 class="number">{{computed_data.total_blackouts}}</h3>
			<h2>Total Days</h2>
			<h3 class="number">{{computed_data.total_days}}</h3>
			<p>out of {{computed_data.total_days_since}} days</p>

			<h2>Percentage</h2>
			<h3 class="number">{{computed_data.percent_days}}%</h3>
			of an area to have a blackout

			<h2>Total Downtime:</h2>
			<h3 class="number">{{computed_data.total_days_down}}</h3>
		</div>

		<p>First Post: {{computed_data.first_post}}</p>
		<p>last Post: {{computed_data.last_post}}</p>
		<p>Last Updated: {{computed_data.updated_at}}</p>
		<div class="heatmap-section">
			<heat-map :days="days"/>
		</div>

		<div class="since-section">
			<h2>Days Since Last Blackout</h2>
			<h3 class="number">{{computed_data.days_since}}</h3>
		</div>

		<div class="info-section">
			<!-- <ul class="categories">
				<li><button>All</button></li>
				<li><button>Emergency</button></li>
				<li><button>Unscheduled</button></li>
				<li><button>Scheduled</button></li>
			</ul> -->

			<!-- <div class="info-wrap">
				<div class="info-item">
					<h4>Average Restoration Time</h4>
					<h5 class="number">{{computed_data.categories.all.average_restoration}}</h5>
				</div>
				<div class="info-item">
					<h4>Average Days Per Week</h4>
					<h5 class="number">{{computed_data.categories.all.average_days_week}}</h5>
				</div>
				<div class="info-item">
					<h4>Photo Verification</h4>
					<h5 class="number">{{computed_data.categories.all.photo_verification}}</h5>
				</div>

				<div class="info-item">
					<h4>Top Causes</h4>
					<ul class="number">

						<li v-for="cause in computed_data.categories.all.top_causes" :key="cause">
							{{cause.name}}: {{cause.value}}
						</li>

					</ul>
				</div>
			</div> -->
		</div>
	</div>
</template>

<script>
import axios from 'axios'
const api_server = process.env.VUE_APP_API

import HeatMap from './HeatMap.vue'

export default {
	name: 'Home',
	components: {
		HeatMap
	},
	data () {
		return {
			computed_data : {},
			days: []
		}
	},
	methods: {
		getComputed: function () {
			axios
				.get(`${api_server}/computed`)
				.then(response => {
					this.computed_data = response.data
					this.days = JSON.parse(response.data.days_count)
				})
				.catch(error => console.log(error))
		}
	},
	mounted() {
		this.getComputed()
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.main {
	padding: 7% 0;
	width: 95%;
}
.total-section {
	h2 {
		margin: 0;
	}
	.number {
		font-size: 6em;
		line-height: 1em;
		margin: 0;
	}
}

.since-section {
	h2 {
		margin: 0;
	}
	.number {
		font-size: 5em;
		line-height: 1em;
		margin: 0;
	}
}

.info-wrap {
	display: flex;
    flex-wrap: wrap;

	.info-item {
		width: 50%;
		h4 {
			margin: 0;
		}
		.number {
			line-height: 1em;
			font-size: 3em;
			margin: 0;
		}
	}
}
</style>
