// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import alert from 'vue-strap'
import './assets/dashboard.css'

import sidebar from './components/sidebar'
import login from './components/login'

Vue.config.productionTip = false

/* eslint-disable no-new */
var appWidget = new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App, alert }
})

var loginWidget = new Vue({
  el: '#login',
  template: '<login/>',
  components: { login }
})

var sidebarWidget = new Vue({
  el: '#sidebar',
  template: '<sidebar/>',
  components: { sidebar }
})

export default {
  appWidget,
  sidebarWidget,
  loginWidget
}

