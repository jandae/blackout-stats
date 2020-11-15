<script>
import { Pie } from 'vue-chartjs'
import ChartDataLabels from 'chartjs-plugin-datalabels'; // eslint-disable-line no-unused-vars

export default {
    extends: Pie,
    props: ['list'],
	components: {
		Pie
	},
	data () {
		return {
			days: [],
		}
	},
	methods: {
    },
    computed: {
        formatted() {
            console.log(this.list)
            let data = this.list
            let labels = []
            let counts = []
            for (let item of data) {
                labels.push(item['category'])
                counts.push(item['count'])
            }

            let chartdata = {

				labels: labels,
				datasets: [
					{
                        label: 'Data One',
                        backgroundColor: 'transparent',
                        data: counts,
                        datalabels: {
                            color: '#fff',
                            anchor: 'end',
                            align: 'end',
                            offset: 10,
                            clip: false
                        }
                    }
				]
			}
			let options = {
                responsive: true,
                legend: false,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        left: 70,
                        right: 70,
                        top: 50,
                        bottom: 50
                    }
                },
                plugins: {
                    datalabels: {
                        formatter: function(value, context) {
                            return context.chart.data.labels[context.dataIndex]+': '+value;
                        }
                    }
                }
			}

            return {
                'chartdata': chartdata,
                'options': options
            }
        }
    },
	mounted() {
		this.renderChart(this.formatted['chartdata'], this.formatted['options'])
	}
}
</script>

<style scoped lang="scss">

</style>
