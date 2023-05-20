import { createStore } from 'vuex'
const store = createStore({
  state() {
    return {
      isLogin: false,
      isVIP: false,
      userId: null,
      userAvatar: null,
      navigationLoc: 1,
      categoriesIndex: [0, 0, 0, 0],
    }
  },
  mutations: {
    refresh(state) {
      state.isLogin = !state.isLogin
    },
    changeLoginState(state) {
      if (this.state.isLogin) {
        state.isLogin = false
      } else {
        state.isLogin = true
        state.isVIP = false
      }
    },
    setVIP(state) {
      state.isVIP = true
    },
    setUser(state, userId) {
      state.userId = userId;
      state.isLogin = true;
    },
    changeNaviLoc(state, num) {
      state.navigationLoc = num
    },
    changeCategoriesIndex(state, content) {
      state.categoriesIndex[content.title] = content.index
    }
  }
})
export default store