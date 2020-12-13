<template>
  <v-layout justify-left>
    <url-list />
  </v-layout>
</template>

<script>
import urlList from '~/components/url-list.vue'

export default {
  layout: 'complex',
  components: {
    urlList
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
