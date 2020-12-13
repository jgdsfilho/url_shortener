import {get, post} from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', {username, password})
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  },
  settings () {
    return get('/api/settings')
  },
  list_urls () {
    return get('/api/url')
  },
  new_url (url) {
    return post('/api/url', {url})
  },
  redirect_url (url) {
    console.log(`/api/redirect_url/${url}`)
    return get(`/api/redirect_url/${url}`)
  }
}
