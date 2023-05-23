import { createApp } from 'vue'
<<<<<<< HEAD
import vuetyped from 'vue3typed'
=======

>>>>>>> a38170724539145ca537acb44895efb1dde67647
import App from './App.vue'
import router from './route/index'
import store from './store/index'
import ElementPlus from 'element-plus';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


// import loginState from './store/loginState'
import axios from 'axios'
axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.directive("shake", (el) => {
  el.addEventListener('click', () => {
    el.style.animation = "shake 0.82s cubic-bezier(.36,.07,.19,.97) both"
    el.addEventListener('animationend', () => {
      el.style.animation = ""
    })
  })
})
app.use(ElementPlus)
app.use(router)
app.use(store)
<<<<<<< HEAD
app.use(vuetyped)
=======
>>>>>>> a38170724539145ca537acb44895efb1dde67647
app.mount('#app')

