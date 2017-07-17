<template>
  <div id="navbar" class="navbar-collapse collapse">
    <ul class="nav navbar-nav navbar-right">
      <li v-if="is_authenticated"><a v-on:click="logout" href="#">Logout</a></li>
      <li v-else><a v-on:click="login" href="#">Login</a></li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'
  // import main from '../main'

  export default {
    data () {
      return {
        is_authenticated: false
      }
    },
    created: function () {
      this.fetchData()
    },
    methods: {
      ajax: function (url, after) {
        return axios.get(url, {
          responseType: 'json'}
        ).then(this.fillWidget)
        .catch(this.showError)
      },
      fillWidget: function (response) {
        this.is_authenticated = response.data.is_authenticated
      },
      showError: function (error) {
        console.log(error)
      },
      // real methods
      fetchData: function () {
        this.ajax('/api/auth')
        // console.log(main.sidebarWidget.menu)
      },
      login: function (event) {
        event.preventDefault()
        this.ajax('/api/auth/login').then(this.after)
      },
      logout: function (event) {
        event.preventDefault()
        this.ajax('/api/auth/logout').then(this.after)
      },
      after: function (event) {
        location.reload()
      }
    }
  }
</script>
