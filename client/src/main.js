import Vue from 'vue'
import App from './App.vue'
import VueSocketIO from "vue-socket.io";
import "normalize.css";

Vue.config.productionTip = false

Vue.use(new VueSocketIO({
  debug: true,
  connection: "localhost:5000"
}))


new Vue({
  render: h => h(App),
}).$mount('#app')