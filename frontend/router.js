import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import urlList from '~/pages/urls_list'
import UrlRedirect from '~/pages/url'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/url_list', component: urlList, name: 'url_list'},
    {path: '/url/:url', component: UrlRedirect, name: 'url'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
