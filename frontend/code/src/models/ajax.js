import axios from 'axios'

class AjaxView {
  constructor (fillWidget) {
    this.fillWidget = fillWidget
  }

  showError (error) {
    console.log(error)
  }

  run (url) {
    axios.get(url, {
      responseType: 'json'}
    ).then(this.fillWidget)
    .catch(this.showError)
  }
}

export default AjaxView
