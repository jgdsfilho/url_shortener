import { zuck } from './db_people'
import { all_url } from './db_url'
import { mockasync } from './mockutils'

const keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    return mockasync({})
  },
  whoami () {
    const iam = {authenticated: keepLoggedIn}
    if (iam.authenticated) {
      iam.user = zuck
    }
    return mockasync(iam)
  },
  settings () {
    return mockasync({
      SENTRY_DSN_FRONT: ''
      // SENTRY_DSN_FRONT: 'https://abcd1234@sentry.example.com/10'
    })
  },
  list_urls () {
    return mockasync(all_url)
  },
  new_url (url) {
    return mockasync({url, new_url: 'url_curta'})
  },
  redirect_url (url) {
    return mockasync({url, new_url: 'google.com'})
  }
}
