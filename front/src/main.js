import { createApp } from 'vue'

import 'vue-good-table-next/dist/vue-good-table-next.css'
import _store from 'store2'
import './assets/css/body.css'
import App from './App.vue'
import router from './route/index'
import store from './store/index'
import ElementPlus from 'element-plus';
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import VueGoodTablePlugin from 'vue-good-table-next';
import hovercss from 'hover.css';
import axios from 'axios'

_store({ initState: store.state })
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
const debounce = (fn, delay) => {
  let timer = null;
  return function () {
    let context = this;
    let args = arguments;
    clearTimeout(timer);
    timer = setTimeout(function () {
      fn.apply(context, args);
    }, delay);
  }
}

const _ResizeObserver = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
  constructor(callback) {
    callback = debounce(callback, 16);
    super(callback);
  }
}
app.use(ElementPlus)
app.use(router)
app.use(store)
app.use(VueGoodTablePlugin)
app.use(hovercss);
// 屏蔽错误信息
app.config.errorHandler = () => null;
// 屏蔽警告信息
app.config.warnHandler = () => null;
app.mount('#app')

