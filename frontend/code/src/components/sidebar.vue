<template>
  <div class="col-sm-3 col-md-2 sidebar">
    <ul class="nav nav-sidebar" v-for="group in menu">
      {{ group.name }}
      <li v-for="element in group.elements" v-bind:class="{ active: element.isActive }">
        <a v-bind:href="element.url">{{ element.text }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        menu: []
      }
    },
    created: function () {
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        var xhr = new XMLHttpRequest()
        var self = this
        xhr.open('GET', '/api/menu')
        xhr.onload = function () {
          self.menu = JSON.parse(xhr.responseText).menu
        }
        xhr.send()
      }
    }
  }
</script>
