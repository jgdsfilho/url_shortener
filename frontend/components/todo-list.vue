<template>
  <v-card>
    <v-toolbar color="cyan" dark>
      <v-text-field class="ma-4" v-model="url" @keyup.enter="add_url()" label="Add todo and hit enter" :loading="adding" />
    </v-toolbar>
    <v-progress-linear :indeterminate="true" v-if="loading" />
    <v-list two-line>
      <template v-for="item in items">
        <v-list-item :key="item.url">
          <v-list-item-content>
            {{item.url}} -> {{item.new_url}}
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
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
    console.log(this.$route.query.url)
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

<style scoped>
  .done {
    text-decoration: line-through;
  }
</style>
