// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import alert from 'vue-strap'
import styles from './assets/dashboard.css'

import sidebar from './components/sidebar'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App, styles, alert }
})

new Vue({
  el: '#sidebar',
  router,
  template: '<sidebar/>',
  components: { sidebar }
})
