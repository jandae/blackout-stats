<template>
	<div class="main">
		<div class="section">
			<h1>Black<span>Outs</span></h1>
		</div>
		<div class="section">
			<div>
				<h2 class="blk">{{computed_data.total_blackouts}}</h2>
				<h5>Reported</h5>
			</div>
		</div>
		<div class="section two-col">
			<div>
				<h3 class="blk">{{computed_data.percent_days}}%</h3>
				<h5>{{computed_data.total_days}} out of {{computed_data.total_days_since}} Days</h5>
			</div>
			<div>
				<h3 class="blk">{{computed_data.average_duration}}</h3>
				<h5>Hours Average</h5>
			</div>
		</div>

		<div class="heatmap-section">
			<heat-map :days="days"/>
		</div>

		<div class="section">
			<div>
				<h3 class="blk under">
					{{computed_data.total_days_down}}<span>Days</span>
					{{computed_data.total_hours_down}}<span>hours</span>
					{{computed_data.total_minutes_down}}<span>minutes</span>
				</h3>
				<h5>Total Equivalent</h5>
			</div>
		</div>

		<div class="since-section section">
			<div>
				<div>
					<h3 class="blk">{{computed_data.days_since}}</h3>
				</div>
				<div class="caption">Days Since Last Blackout</div>
			</div>
		</div>

		<div class="section pie-section">
			<pie-chart :list="JSON.parse(computed_data.categories)"/>
		</div>

		<p>First Post: {{computed_data.first_post}}</p>
		<p>last Post: {{computed_data.last_post}}</p>
		<p>Last Updated: {{computed_data.updated_at}}</p>




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
import HeatMap from './HeatMap.vue'
import PieChart from './PieChart.vue'

const api_server = process.env.VUE_APP_API

export default {
	name: 'Home',
	components: {
		HeatMap,
		PieChart
	},
	data () {
		return {
			computed_data : {},
			days: [],
			chartdata: {
				labels: ['January', 'February'],
				datasets: [
					{
					label: 'Data One',
					backgroundColor: '#f87979',
					data: [40, 20]
					}
				]
			},
			options: {
				responsive: true,
				maintainAspectRatio: false,
				plugins: {
					datalabels: {
						clip: true
					}
				},
			}
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
@import '@/assets/scss/breakpoints.scss';
@import '@/assets/scss/home.scss';
</style>
