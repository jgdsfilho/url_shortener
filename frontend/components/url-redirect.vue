<template>
  <div />
</template>

<script>
import api from '~api'

export default {
  data () {
    return {

    }
  },
  async mounted () {
    const response = await api.redirect_url(this.$route.params.url)
    let url = response.url
    if (!response.url.includes('http')) {
      url = `http://${response.url}`
    }
    window.location.href = url
  }
}
</script>
