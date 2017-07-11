<template>
  <div class="col-sm-3 col-md-2 sidebar">
    <ul class="nav nav-sidebar">
      <li class="active"><a href="#">Overview <span class="sr-only">(current)</span></a></li>
      <li><a href="#">{{ message }}</a></li>
      <li><a href="#/car">Analytics</a></li>
      <li><a href="#">Export</a></li>
    </ul>
    <ul class="nav nav-sidebar">
      <li><a href="">Nav item</a></li>
      <li><a href="">Nav item again</a></li>
      <li><a href="">One more nav</a></li>
      <li><a href="">Another nav item</a></li>
      <li><a href="">More navigation</a></li>
    </ul>
    <ul class="nav nav-sidebar">
      <li><a href="">Nav item again</a></li>
      <li><a href="">One more nav</a></li>
      <li><a href="">Another nav item</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: ''
    }
  },
  created: function () {
    this.fetchData()
  },
  methods: {
    fetchData: function () {
      var xhr = new XMLHttpRequest()
      var self = this
      xhr.open('GET', '/api')
      xhr.onload = function () {
        self.commits = JSON.parse(xhr.responseText)
        self.message = self.commits['yey']
      }
      xhr.send()
    }
  }
}
</script>
