import Vue from 'vue'
import App from './App.vue'
import VueSocketIO from 'vue-socket.io';
import 'normalize.css';
import router from './router'
import Ionic from '@ionic/vue';
import '@ionic/core/css/ionic.bundle.css';

Vue.use(Ionic);
Vue.config.productionTip = false

Vue.use(new VueSocketIO({
  debug: true,
  connection: "localhost:5000"
}))


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')