import { createStore } from 'vuex'
const store = createStore({
  state() {
    return {
      isLogin: false,
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