<template>
	<div class="main">
		<div class="section">
			<h1>Black<span :class="{blink: 'blink'}">Outs</span></h1>
		</div>
		<div class="section">
			<div>
				<h2 v-if="computed_data.total_blackouts"><number class="blk" :num="computed_data.total_blackouts"/></h2>
				<h5>Reported</h5>
			</div>
		</div>
		<div class="section two-col">
			<div>
				<h3 class="blk"><number class="blk" :num="computed_data.percent_days" after="%"/></h3>
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
					<number class="blk" :num="computed_data.total_days_down"/><span>Days</span>&nbsp;
					<number class="blk" :num="computed_data.total_hours_down"/><span>hours</span>&nbsp;
					<number class="blk" :num="computed_data.total_minutes_down"/><span>minutes</span>
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

		<div class="section interesting-section">
			<h5>Interesting Causes</h5>
			<div class="causes">
				<div class="cause-item">
					<span>Birds</span>
					<span class="blk">{{computed_data.birds}}</span>
					<div class="icon-wrap">
						<svg class="icon">
							<use xlink:href="#bullfinch"></use>
						</svg>
						<bolt class="bolt"></bolt>
					</div>
					<div class="bottom-wrap">
						<div>Martinez <span class="blk">{{computed_data.martinez}}</span></div>
						<div>Crow <span class="blk">{{computed_data.crow}}</span></div>
					</div>
				</div>
				<div class="cause-item">
					<span>Trees</span>
					<span class="blk">{{computed_data.trees}}</span>
					<div class="icon-wrap">
						<svg class="icon">
							<use xlink:href="#trees"></use>
						</svg>
					</div>
					<div class="bottom-wrap">
						<div>Pine <span class="blk">{{computed_data.pine}}</span></div>
					</div>
				</div>
				<div class="cause-item">
					<span>Bumped</span>
					<span class="blk">{{computed_data.bumped}}</span>
					<div class="icon-wrap">
						<svg class="icon">
							<use xlink:href="#construction-machine"></use>
						</svg>
					</div>
					<div class="bottom-wrap">
						<div>Backhoe <span class="blk">{{computed_data.backhoe}}</span></div>
					</div>
				</div>
				<div class="cause-item">
					<span>Lightning</span>
					<span class="blk">{{computed_data.lightning}}</span>
					<div class="icon-wrap">
						<svg class="icon">
							<use xlink:href="#flash"></use>
						</svg>
					</div>
				</div>
			</div>
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
import Bolt from './Bolt.vue'
import Number from './Number.vue'
import wordcloud from 'vue-wordcloud'

const api_server = process.env.VUE_APP_API

export default {
	name: 'Home',
	components: {
		HeatMap,
		PieChart,
		wordcloud,
		Bolt,
		Number
	},
	data () {
		return {
			myColors: ['#000', '#333333', '#555555', '#777777', '#fffde5'],
			blink: false,
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
				.finally(() => {
					this.blink = true
					console.log('done');
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
