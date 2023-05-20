
import { createStore } from 'vuex'

// 创建一个新的 store 实例
const loginState = createStore({
  state() {
    return {
      isLogining: true,
      isVIP: false,
    }
  },
  mutations: {
    changeLoginingState() {
      if (this.state.isLogining) {
        this.state.isLogining = false
      } else {
        this.state.isLogining = true
        this.state.isVIP = false
      }
    },
    setVIP() {
      this.state.isVIP = true
    }
  }
})
export default loginState