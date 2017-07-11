<template>
  <div class="hello">
    This is creazy.
    <h1>|{{ message }}|</h1>
    <alert type="success">
      CZABO
    </alert>
  </div>
</template>

<script>

export default {
  name: 'hello',
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

<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
