import { createStore } from 'vuex'
const store = createStore({
  state() {
    return {
      tempAvatar:null,
      isLogin: false,
      isVIP: true,
      userId: null,
      userAvatar: null,
      navigationLoc: 1,
      categoriesIndex: [0, 0, 0, 0],
      userInfo:{
        username: null,
        gender: null,
        birthday: "2000-01-01",
        email: null,
        motto: "这个人很懒,什么也没留下。",
        nickname: null,
        VIPDate:null,
      },
      themes: [
        {
          "name": "默认",
          "color": "hsla(40,60%,95%,.8)",
          "bg1": require('assets/imgs/readerbcg/default/body.png'),
          "bg2": require('assets/imgs/readerbcg/default/basic.png'),
        },
        {
          "name": "牛皮纸",
          "color": "hsla(44,67%,88%,.8)",
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
          "color": "hsla(0,46%,93%,.8)",
          "bg1": require('assets/imgs/readerbcg/lightpink/body.png'),
          "bg2": require('assets/imgs/readerbcg/lightpink/basic.png'),
        },
      ],
      readerSettings: [{
        "name": "默认",
        "color": "hsla(40,60%,95%,.8)",
        "bg1": require('assets/imgs/readerbcg/default/body.png'),
        "bg2": require('assets/imgs/readerbcg/default/basic.png'),
      }, "yahei", 18, 800],

    }
  },
  getters : {
  tempAvatar: state => state.tempAvatar,
  // ...
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
    setTempAvatar(state,url){
      state.tempAvatar=url
    },
    setVIP(state) {
      state.isVIP = true
    },
    signOut(state) {
      state.isLogin = false;
    },
    setUser(state, userId) {
      state.userId = userId;
      state.isLogin = true;
    },
    setAvatarUrl(state,url){
      state.userAvatar=url
    },
    changeNaviLoc(state, num) {
      state.navigationLoc = num
    },
    changeCategoriesIndex(state, content) {
      state.categoriesIndex[content.title] = content.index
    },
    setReaderSettings(state, settings) {
      state.readerSettings = settings
    },
    updateUserInfo(state,userInfo){
      state.userInfo=userInfo
      state.isLogin=true
    }
  },
})
export default store