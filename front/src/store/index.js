import { createStore } from 'vuex'
const store = createStore({
  state() {
    return {
      isLogin: false,
    }
  },
  mutations: {
    refresh(state) {
      state.isLogin = !state.isLogin
    }
  }
})
export default store