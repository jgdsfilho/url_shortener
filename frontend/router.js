import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Todos from '~/pages/todos.vue'
import UrlRedirect from '~/pages/url'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/todos', component: Todos, name: 'todos'},
    {path: '/url', component: UrlRedirect, name: 'url'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
