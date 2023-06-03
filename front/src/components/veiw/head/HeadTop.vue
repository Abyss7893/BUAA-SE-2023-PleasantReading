<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="proeffect">
    <ElDialog v-model="showLogin" style="background-color: transparent; width: 800px;">
      <newLogin class="mycardlogin" style="z-index: 1000; background-color: transparent;" @submit="showLogin = false"
        ref="login"></newLogin>
    </ElDialog>
  </div>
  <link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.0.0/animate.min.css" />
  <div class="head-top">
    <!-- <check-login/> -->
    <div>
      <a class="logoa" href="/"><img class="logo" src="~assets/logo-yixinyuedu.png" alt="" /></a>
    </div>
    <div class="dropdown">
      <div class="search">
        <div class="shell">
          <input type="text" placeholder="Search" v-model="keywords" @focusin="drop" @focusout="hide">
          <svg @mousedown="clearwords" v-show="keywords !== ''" class="clear" width="16" height="16" viewBox="0 0 16 16"
            fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd"
              d="M8 14.75C11.7279 14.75 14.75 11.7279 14.75 8C14.75 4.27208 11.7279 1.25 8 1.25C4.27208 1.25 1.25 4.27208 1.25 8C1.25 11.7279 4.27208 14.75 8 14.75ZM9.64999 5.64303C9.84525 5.44777 10.1618 5.44777 10.3571 5.64303C10.5524 5.83829 10.5524 6.15487 10.3571 6.35014L8.70718 8.00005L10.3571 9.64997C10.5524 9.84523 10.5524 10.1618 10.3571 10.3571C10.1618 10.5523 9.84525 10.5523 9.64999 10.3571L8.00007 8.70716L6.35016 10.3571C6.15489 10.5523 5.83831 10.5523 5.64305 10.3571C5.44779 10.1618 5.44779 9.84523 5.64305 9.64997L7.29296 8.00005L5.64305 6.35014C5.44779 6.15487 5.44779 5.83829 5.64305 5.64303C5.83831 5.44777 6.15489 5.44777 6.35016 5.64303L8.00007 7.29294L9.64999 5.64303Z"
              fill="#ff7575"></path>
          </svg>
          <div class="proshake">
            <a @click="searchBooks">
              <i class="fa fa-hand-o-right"></i>
              <i class="fa fa-search"></i>
            </a>
          </div>
        </div>
      </div>
      <div class="dropdown-content" ref="hidden">
        <div class="first-want">大家都想看</div>
        <div class="want" v-for="(searchHot, idx) in searchHots" :key="idx" @click="searchBooks(searchHot)">{{ searchHot
        }}</div>
      </div>
    </div>
    <div class="login-register">
      <template v-if="!isLogin">
        <div class="avatar">
          <el-popover trigger="hover" :show-arrow=false transition="el-zoom-in-top" width="480">
            <div class="logininfo">登录后你可以</div>
            <div class="login-pri">
              <li><svg t="1685433487956" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="2670" width="24" height="24">
                  <path
                    d="M880 184H712v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H384v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H144c-17.7 0-32 14.3-32 32v664c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V216c0-17.7-14.3-32-32-32z m-40 656H184V256h128v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h256v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h128v584z"
                    p-id="2671" fill="#ed4259"></path>
                  <path
                    d="M639.5 414h-45c-3 0-5.8 1.7-7.1 4.4L514 563.8h-2.8l-73.4-145.4c-1.4-2.7-4.1-4.4-7.1-4.4h-46c-1.3 0-2.7 0.3-3.8 1-3.9 2.1-5.3 7-3.2 10.9l89.3 164h-48.6c-4.4 0-8 3.6-8 8v21.3c0 4.4 3.6 8 8 8h65.1v33.7h-65.1c-4.4 0-8 3.6-8 8v21.3c0 4.4 3.6 8 8 8h65.1V752c0 4.4 3.6 8 8 8h41.3c4.4 0 8-3.6 8-8v-53.8h65.4c4.4 0 8-3.6 8-8v-21.3c0-4.4-3.6-8-8-8h-65.4v-33.7h65.4c4.4 0 8-3.6 8-8v-21.3c0-4.4-3.6-8-8-8h-49.1l89.3-164.1c0.6-1.2 1-2.5 1-3.8 0.1-4.4-3.4-8-7.9-8z"
                    p-id="2672" fill="#ed4259"></path>
                </svg>免费阅读大量书籍</li>
              <li><svg t="1685433539490" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="3810" width="24" height="24">
                  <path d="M192 320l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3811"></path>
                  <path d="M320 320l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3812"></path>
                  <path d="M192 512l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3813"></path>
                  <path d="M320 512l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3814"></path>
                  <path d="M192 704l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3815"></path>
                  <path d="M320 704l448 0 0 64-448 0 0-64Z" fill="#ed4259" p-id="3816"></path>
                  <path d="M320 64l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3817"></path>
                  <path
                    d="M832 75.776l0 65.984C872.64 161.152 896 200.704 896 256l0 576c0 66.688-45.312 128-128 128L192 960c-61.312 0-128-64-128-128L64 256c0-46.592 25.6-87.872 64-110.272L128 75.776C53.568 102.208 0 172.544 0 256l0 576c0 106.048 85.952 192 192 192l576 0c106.048 0 192-85.952 192-192L960 256C960 172.544 906.432 102.208 832 75.776z"
                    fill="#ed4259" p-id="3818"></path>
                  <path d="M576 64l64 0 0 64-64 0 0-64Z" fill="#ed4259" p-id="3819"></path>
                  <path d="M192 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3820"></path>
                  <path d="M448 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3821"></path>
                  <path d="M704 0l64 0 0 192-64 0 0-192Z" fill="#ed4259" p-id="3822"></path>
                </svg>发表评论/记录笔记</li>
              <li><svg t="1685433591589" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="4934" width="24" height="24">
                  <path
                    d="M282.766507 610.432L100.494507 401.92 370.361173 340.48 512.014507 102.656l141.610666 237.909333 269.824 61.397334-182.272 208.512 27.306667 300.757333a42.666667 42.666667 0 0 0 84.992-7.722667l-24.021333-264.405333 174.634666-199.722667c38.144-43.648 19.2-102.229333-37.418666-115.114666l-258.474667-58.794667-135.68-228.010667c-29.738667-49.877333-91.306667-49.92-121.045333 0L315.74784 265.429333 57.273173 324.224C0.953173 337.066667-18.33216 395.648 19.854507 439.338667l174.634666 199.722666-24.021333 264.405334c-5.248 57.770667 44.544 94.037333 97.877333 71.125333l260.48-111.786667a42.666667 42.666667 0 1 0-33.706666-78.378666L257.721173 886.314667l25.045334-275.882667z"
                    fill="#ed4259" p-id="4935"></path>
                </svg>收藏喜欢的图书</li>
              <li><svg t="1685433451224" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="1480" width="24" height="24">
                  <path
                    d="M748.739048 352.865524c-32.743619-40.496762-29.915429 86.893714-68.169143 67.462095-38.253714-19.431619-27.087238-285.891048-259.169524-354.230857-92.769524-27.306667 36.766476 218.35581-104.374857 331.751619-141.165714 113.371429-340.845714 359.765333 113.615238 562.151619 0 0-235.398095-269.409524 68.144762-427.227429 69.632-36.205714-22.723048 89.941333 90.89219 179.882667 113.615238 89.965714 0 247.344762 0 247.344762s516.291048-165.059048 159.061334-607.134476z"
                    p-id="1481" fill="#ed4259"></path>
                </svg>热门书籍看不停</li>
            </div>
            <el-button class="login-button" type="primary" color="#f33f3f" @click="showLoginblock">立即登录</el-button>
            <div class="register"><span>首次使用?<a @click="showRegister">点我注册</a></span></div>
            <template #reference>
              <ElAvatar class="login-avatar" size="large"><span @click="showLoginblock">登录</span></ElAvatar>
            </template>
          </el-popover>
        </div>
      </template>
      <template v-else>
        <div class="avatar" @mouseleave="popleave">
          <!-- <ElDropdown trigger="click"> -->
          <div class="edavatar" ref="edavatar" @mouseenter="popover">
            <router-link to="/user/info">
              <ElAvatar :src="avatar" size="large"></ElAvatar>
            </router-link>
          </div>
          <div :style="{ opacity: popShow }" class="popuserinfo" ref="popuserinfo">
            <popUserInfo />
          </div>
        </div>
      </template>
    </div>
  </div>
</template>


<script>
import "css/head/headtop.css";
import newLogin from "@/components/page/login/newLogin.vue";
import {
  ElAvatar, ElDialog,
  // ElDropdown,
  // ElDropdownMenu,
  // ElDropdownItem,
} from "element-plus";
import popUserInfo from "./popUserInfo.vue"
export default {
  name: "Head_Top",
  components: {
    ElAvatar,
    popUserInfo,
    newLogin,
    ElDialog
  },
  data() {
    return {
      searchHots: ["青春北航男童不会梦到清华女学长", "重生之我在北航卖西瓜", "飘飘何所似", "红楼梦", "杨过"],
      clearExit: false,
      keywords: "",
      showLogin: false,
      popShow: 0,
      throttling1: false,

    }
  },
  computed: {
    avatar() {
      return this.$store.state.userAvatar;
    },
    isLogin() {
      return this.$store.state.isLogin;
    },
    clearShow() {
      return this.clearExit
    },
  },
  mounted() {
    this.keywords = this.$route.query.keywords ? this.$route.query.keywords : ""
  },

  methods: {
    onCloseDialog(value) {
      // 接收到子组件传递过来的布尔值，赋值给 showLogin 属性
      this.showLogin = value;
    },
    drop() {
      this.$refs.hidden.style.maxHeight = '500px';
      this.$refs.hidden.style.paddingBottom = '10px'
    },
    hide() {
      this.$refs.hidden.style.maxHeight = '0';
      this.$refs.hidden.style.paddingBottom = '0'
    },
    searchBooks(keywords) {
      if (typeof (keywords) != "string")
        keywords = this.keywords
      if (keywords === '')
        return
      this.$router.push({ path: '/search', query: { "keywords": keywords, page: 1 } })
    },
    clearwords() {
      this.keywords = ""
    }, showLogina() {
      this
    },
    popover() {
      if (!this.throttling2) {
        this.throttling2 = true
        this.$refs.popuserinfo.classList.remove("hidden")
        this.popShow = "1"
        this.$refs.edavatar.classList.add("large")
        // this.$refs.edavatar.classList.add("large")
      }
    },
    popleave() {
      this.$refs.edavatar.classList.remove("large")
      this.$refs.popuserinfo.classList.add("hidden")
      this.popShow = "0"
      setTimeout(() => {
        this.throttling2 = false
      }, 400);
    },
    showLoginblock() {
      this.showLogin = true
      setTimeout(() => {
        if (this.$refs.login.showStatus())
          this.$refs.login.changeForm()
      }, 200)
    },
    showRegister() {
      this.showLogin = true
      setTimeout(() => {
        if (!this.$refs.login.showStatus())
          this.$refs.login.changeForm()
      }, 200)
    },
  },

}
</script>
<style >
.mycardlogin {
  z-index: 1000;
  background-color: transparent;

}

.hidden {
  visibility: hidden;
}

.mask {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  width: 100%;
  height: 100%;
  background-color: rgba(254, 253, 253, 0.5);
}

.shell {
  position: relative;
  width: 500px;
  padding: 16px;
  background-color: #ff7575;
  border-radius: 20px;
  box-shadow: 0 10px 50px #ff7575, 0 0 0 20px #fff;
}

.shell {
  position: relative;
  width: 400px;
  padding: 8px;
  background-color: #f8b2b27d;
  border-radius: 5px;
  box-shadow: 0 2px 12px #ff7575a9, 0 0 0 8px #fff;
}

.shell input {
  width: 76%;
  height: 20px;
  color: #fff;
  font: 300 16px '优设标题黑';
  border: 0;
  background-color: transparent;
}

.shell input::placeholder {
  color: #8f36367e;
}

.shell a {
  display: flex;
  font-size: 24px;
  position: absolute;
  right: 8px;
  top: 4px;
  color: #fff;
  width: 62px;
  height: 37px;
}

.shell a .fa {
  margin: 2px 7px;
  transition: .3s;
}



.shell a .fa-search {
  transform: translateX(-20px);
  opacity: 1;
}

.shell a .fa-hand-o-right {
  transform: translateX(-25px);
  opacity: 0;
}

.shell .proshake:hover a .fa-search {
  transform: translateX(0);
  opacity: 0;
}

.shell .proshake:hover a .fa-hand-o-right {
  transform: translateX(22px);
  opacity: 1;
}

.shell a::before {
  content: 'GO!';
  position: absolute;
  display: block;
  font-size: 12px;
  background-color: #ff7575;
  padding: 1px 7px;
  top: 12px;
  right: 2px;
  border-radius: 2px;
  transition: .3s;
  opacity: 0;
  animation: box 1s infinite ease;
}

.shell .proshake:hover a::before {
  top: -22px;
  opacity: 1;
}

@keyframes box {
  0% {
    transform: rotate(0deg);
  }

  33% {
    transform: rotate(8deg);
  }

  66% {
    transform: rotate(-8deg);
  }

  100% {
    transform: rotate(0deg);
  }
}

.clear:hover path {
  fill: #f33f3f;
}

.login-avatar {
  --el-avatar-bg-color: #f56c6c;
  cursor: pointer;
}

.logininfo {
  margin: 16px 0 0 16px;
  font-size: 18px;
}

.login-button {
  margin-top: 12px;
  font-size: 16px;
  width: 100%;
  height: 42px;
}

.register {
  cursor: pointer;
  width: 100%;
  margin-top: 24px;
  display: flex;
  justify-content: center;
  font-size: 16px;
}

.register span a {
  margin-left: 8px;
  color: #f56c6c;
}

.login-pri {
  width: 100%;
  margin-top: 36px;
}

.login-pri li {
  font-size: 16px;
  width: 45%;
  float: left;
  margin: 0 0 24px 16px;
}

.login-pri li svg {
  margin-bottom: -4px;
  margin-right: 8px;
}


.edavatar {
  height: auto;
  background-color: transparent;
  position: relative;
  top: 0;
  right: 0;
  transition: all .3s ease-in-out;
  z-index: 200;
}

.edavatar:hover .el-avatar {
  box-shadow: 0 1px 20px rgba(0, 0, 0, .2);
}

.large {
  transform-origin: right top;
  transform: translateZ(0) scale(2);
}

.popuserinfo {
  transition: all .3s ease-in;
  position: absolute;
  z-index: 160;
}

.avatar {
  position: relative;
}

.proeffect .el-dialog {
  box-shadow: none;
}

.proeffect .el-dialog__headerbtn {
  left: 100%;
  top: -2px;
  margin-left: 64px;
  z-index: 1000;
}

.proeffect .el-dialog__headerbtn:focus .el-dialog__close,
.proeffect .el-dialog__headerbtn:hover .el-dialog__close {
  color: #f56c6c !important;
}
</style>