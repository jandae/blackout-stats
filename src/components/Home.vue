<template>
	<div class="main">
		<div class="total-section">
			<h2>Total Blackouts</h2>
			<h3 class="number">{{computed_data.total}}</h3>
			<span>Last Updated: {{computed_data.last_updated}}</span>
		</div>

		<div class="heatmap-section">

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

			<div class="info-wrap">
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
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Home',
	data () {
		return {
			computed_data : {
				total: "148",
				days_since: "4",
				last_updated: "Oct. 25, 2020 4:55 PM",
				categories: {
					all: {
						average_restoration: "2 Hours",
						average_days_week: "1.3 days",
						photo_verification: "119/148",
						top_causes: [
							{
								name: "tree",
								value:  10
							},
							{
								name: "bird",
								value:  10
							},
							{
								name: "post",
								value:  10
							},
						]
					}
				}
			}
		}
	},
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
