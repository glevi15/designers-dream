import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import Paintable from 'vue-paintable';

Vue.use(Paintable, {
  // optional methods
  setItem(key, image) {
    localStorage.setItem(key, image);
  },
  // you also can use async
  getItem(key) {
    return localStorage.getItem(key);
  },
  removeItem(key) {
    localStorage.removeItem(key);
  }
});

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
