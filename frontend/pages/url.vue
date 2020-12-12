<template>
  <v-layout justify-left>
    <urlRedirect />
  </v-layout>
</template>

<script>
import urlRedirect from '~/components/url-redirect.vue'

export default {
  layout: 'complex',
  components: {
    urlRedirect
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
