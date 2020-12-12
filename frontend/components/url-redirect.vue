<template>
  <div/>
</template>

<script>
import api from '~api'

export default {
  data () {
    return {
      url: '',
      adding: false,
      loading: false,
      items: [
      ]
    }
  },
  async mounted () {
    this.loading = true
    const response = await api.list_urls()
    const urls = response.urls
    this.items = urls
    console.log(this.$route)
    window.location.replace('https://google.com')
    this.loading = false
  },
  methods: {
    async add_url () {
      this.adding = true
      const response = await api.new_url(this.url)
      this.items.push(response)
      this.url = ''
      this.adding = false
    }
  }
}
</script>

{/* <a :href="myUrl">Minha URL</a>
const response = await myRequest(...)
const url = await response.json()

window.location.href = url
Felipe Gomes de Oliveira11:20 AM
window.location.replace(url) */}
