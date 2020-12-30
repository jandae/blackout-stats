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
			<h5>Cause Categories</h5>
			<pie-chart :list="JSON.parse(computed_data.categories)"/>
		</div>

		<div class="section pie-section">
			<h5>Interesting Causes</h5>
			<ul>
				<li>Birds {{computed_data.birds}}</li>
				<li>
					<ul>
						<li>Martinez {{computed_data.martinez}}</li>
						<li>Crow {{computed_data.crow}}</li>
					</ul>
				</li>
			</ul>
			<div>Trees {{computed_data.trees}}</div>
			<div>
				<ul>
					<li>Bumped {{computed_data.bumped}}</li>
					<li>
						<ul>
							<li>Backhoe {{computed_data.backhoe}}</li>
						</ul>
					</li>
				</ul>

				</div>
			<div>Lightning {{computed_data.lightning}}</div>
		</div>

		<div class="section cloud-section separator">
			<h5>Cause Wordcloud</h5>
			<wordcloud
			:data = "words"
			nameKey = "name"
			valueKey = "value"
			:color = "myColors"
			:showTooltip = "true"
			:spiral = "'rectangular'"
			:rotate = "{from: 0, to: 0, numOfOrientation: 1 }"
			:wordPadding = "20"
			font = "Arial"
			>
			</wordcloud>
		</div>

		<p class="source">Source: <a href="https://www.facebook.com/benguetelectric" target="_blank">Beneco - Benguet Electric Cooperative, Inc. Facebook Page</a></p>
		<p>First Post: {{computed_data.first_post}}</p>
		<p>last Post: {{computed_data.last_post}}</p>
		<p>Last Updated: {{computed_data.updated_at}}</p>
	</div>
</template>

<script>
import axios from 'axios'
import HeatMap from './HeatMap.vue'
import PieChart from './PieChart.vue'
import wordcloud from 'vue-wordcloud'

const api_server = process.env.VUE_APP_API

export default {
	name: 'Home',
	components: {
		HeatMap,
		PieChart,
		wordcloud
	},
	data () {
		return {
			myColors: ['#000', '#333333', '#555555', '#777777', '#fffde5'],
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
			},
			defaultWords: [{
				"name": "Cat",
				"value": 26
				},
				{
				"name": "fish",
				"value": 19
				},
				{
				"name": "things",
				"value": 18
				},
				{
				"name": "look",
				"value": 16
				},
				{
				"name": "two",
				"value": 15
				},
				{
				"name": "fun",
				"value": 9
				},
				{
				"name": "know",
				"value": 9
				},
				{
				"name": "good",
				"value": 9
				},
				{
				"name": "play",
				"value": 6
				}
			]
		}
	},
	methods: {
		getComputed: function () {
			axios
				.get(`${api_server}/computed`)
				.then(response => {
					this.computed_data = response.data
					this.days = JSON.parse(response.data.days_count)
					this.words = JSON.parse(response.data.words)
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
