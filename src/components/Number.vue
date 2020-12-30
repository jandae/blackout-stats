<template>
    <div>{{number}}{{after}}</div>
</template>

<script>
export default {
    props: ['num', 'after'],
    data () {
		return {
            number: ''
        }
    },
    mounted() {
        let sub = Math.floor((20/100)*this.num) // 20%
        console.log(sub)
        this.number = this.num - sub

        let tick = setInterval(() => {
            if (this.number == this.num) {
                clearInterval(tick)
                return
            }
            this.number += 1
        }, 5)

    }
}
</script>