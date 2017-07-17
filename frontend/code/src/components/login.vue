<template>
  <div id="navbar" class="navbar-collapse collapse">
    <ul class="nav navbar-nav navbar-right">
      <li v-if="is_authenticated"><a v-on:click="logout" href="#">Logout</a></li>
      <li v-else><a v-on:click="login" href="#">Login</a></li>
    </ul>
  </div>
</template>

<script>
  import AjaxView from '../models/ajax'

  export default {
    data () {
      return {
        is_authenticated: false
      }
    },
    created: function () {
      var self = this
      new AjaxView(function (response) {
        self.is_authenticated = response.data.is_authenticated
      }).run('/api/auth').then(self.fillWidget)
    },
    methods: {
      login: function (event) {
        event.preventDefault()
        var self = this
        new AjaxView(function (response) {
          self.menu = response.data.menu
        }).run('/api/auth/login').then(this.after)
      },
      logout: function (event) {
        event.preventDefault()
        var self = this
        new AjaxView(function (response) {
          self.menu = response.data.menu
        }).run('/api/auth/logout').then(this.after)
      },
      after: function (event) {
        location.reload()
      }
    }
  }
</script>
