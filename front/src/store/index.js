import { createStore } from 'vuex'
import _ from 'lodash'
import _store from 'store2'
import { startSakura, stopp } from '@/api/sakura'
const store = createStore({
  state() {
    return {
      tempAvatar: null,
      showLogin: false,
      isLogin: false,
      isVIP: true,
      showSakura: true,
      userId: null,
      userAvatar: null,
      loginShow: false,
      num: {
        notes: Number,
        marks: Number,
        collections: Number,
        comments: Number,
      },
      userInfo: {
        username: null,
        gender: null,
        birthday: "2000-01-01",
        email: null,
        motto: "这个人很懒,什么也没留下。",
        nickname: null,
        VIPDate: null,
      },
      themes: [
        {
          "name": "默认",
          "color": "rgba(250, 245, 235, 0.8)",
          "bg1": require('assets/imgs/readerbcg/default/body.png'),
          "bg2": require('assets/imgs/readerbcg/default/basic.png'),
        },
        {
          "name": "牛皮纸",
          "color": "rgba(245, 234, 204, 0.8)",
          "bg1": require('assets/imgs/readerbcg/lightyellow/body.png'),
          "bg2": require('assets/imgs/readerbcg/lightyellow/basic.png'),
        },
        {
          "name": "淡绿色",
          "color": "rgba(230,242,230,.8)",
          "bg1": require('assets/imgs/readerbcg/lightgreen/body.png'),
          "bg2": require('assets/imgs/readerbcg/lightgreen/basic.png'),
        },
        {
          "name": "淡蓝色",
          "color": "rgba(228,241,245,.8)",
          "bg1": require('assets/imgs/readerbcg/lightblue/body.png'),
          "bg2": require('assets/imgs/readerbcg/lightblue/basic.png'),
        },
        {
          "name": "淡粉色",
          "color": "rgba(245, 229, 229, 0.8)",
          "bg1": require('assets/imgs/readerbcg/lightpink/body.png'),
          "bg2": require('assets/imgs/readerbcg/lightpink/basic.png'),
        },
        {
          "name": "黑色",
          "color": "#000",
          "bg1": require('assets/imgs/readerbcg/dark/base.png'),
          "bg2": require('assets/imgs/readerbcg/dark/base.png'),
        },
      ],
      readerSettings: [{
        "name": "默认",
        "color": "hsla(40,60%,95%,.8)",
        "bg1": require('assets/imgs/readerbcg/default/body.png'),
        "bg2": require('assets/imgs/readerbcg/default/basic.png'),
      }, "yahei", 18, 800],
      // booklist:{
      //   page:0,
      //   books:[]
      // }

    }
  },
  getters: {
    tempAvatar: state => state.tempAvatar,
    islogin: state => state.isLogin,
    loginshow: state => state.loginShow,
    markupdate: state => state.num.marks,
    showSakura: state => state.showSakura
    // ...
  },
  mutations: {
    changeShowSakura(state, bool) {
      state.showSakura = bool;
      if (bool) { startSakura(); }
      else { stopp(); }
    },
    resetAllState(state, payload) {
      if (payload instanceof Array === false) { // 验证传入的是一个数组
        return
      }
      const initState = _store('initState') // 取出初始值的缓存
      const _initState = payload.length ? _.omit(initState, payload) : initState // 判断传入值有无数据，有数据剔除相对应的值
      _.extend(state, _initState)
    },
    showlogin(state) {
      state.loginShow = !state.loginShow
    },
    refresh(state) {
      state.isLogin = false
      this.commit('resetAllState', ["readerSettings"])
      localStorage.clear()
    },
    changeLoginState(state) {
      if (this.state.isLogin) {
        localStorage.removeItem('token')
        state.isLogin = false
        state.isVIP = false
      } else {
        state.isLogin = true
        state.isVIP = false
      }
    },
    changeShowLogin(state) {
      state.showLogin = !state.showLogin
    },
    setTempAvatar(state, url) {
      state.tempAvatar = url
    },
    setVIP(state) {
      state.isVIP = true
    },
    signOut(state) {
      state.isLogin = false;
      this.commit('resetAllState', ["readerSettings"])
      localStorage.clear()
    },
    setUser(state, userId) {
      state.userId = userId;
      state.isLogin = true;
    },
    setAvatarUrl(state, url) {
      state.userAvatar = url
    },
    changeCategoriesIndex(state, content) {
      state.categoriesIndex[content.title] = content.index
    },
    setReaderSettings(state, settings) {
      state.readerSettings = settings
    },
    updateNum(state, num) {
      state.num.notes = num.notes
      state.num.marks = num.marks
      state.num.collections = num.collections
      state.num.comments = num.comments
    },
    updateUserInfo(state, userInfo) {
      state.userInfo = userInfo
      state.isLogin = true
    },
  },
})
export default store