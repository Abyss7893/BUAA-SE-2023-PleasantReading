<template>
  <div id="login">
    <div id="contain">
      <!-- 左边的卡片 -->
      <div id="left_card">
        <img src="../../../assets/logo-yixinyuedu.png" alt="Logo" class="logo-img">
        <h1>欢迎来到怡心阅读</h1>
        <span>Welcome to yixin reading</span>
      </div>
      <!-- 右边的卡片 -->
      <div id="right_card">
        <el-card class="el-card">
          <h2>欢迎登录</h2>
          <form class="login" action="">
            <input v-shake type="text" v-model="userLoginForm.username" placeholder="请输入账号">
            <input v-shake type="password" v-model="userLoginForm.password" placeholder="请输入密码">
          </form>
          <!-- <span class="forgetPwd" >忘记密码</span> -->
          <el-button class="forgetPwd" @click="showForget = true">忘记密码</el-button>

          <div class="message">
            <span v-html="error"></span>
          </div>
          <div id="btn">
            <button class="loginbtn" @click="usreList">登陆</button>
            <router-link to="/register">
              <button class="loginbtn">注册</button>
            </router-link>
          </div>
        </el-card>
      </div>
    </div>
    <el-dialog title="重置密码" v-model="showForget" :before-close="handleClose" :close-on-click-modal="false"
      :close-on-press-escape="false" :append-to-body="false" style="min-width: 500px;border-radius: 25px;
      border: 1px solid black;
     
      backdrop-filter: blur(5px);
      box-shadow: -5px -5px 10px rgb(39, 65, 65),
        5px 5px 20px aqua;
      animation: animate 5s linear infinite;">
      <forget-dialog @submit="showForgetDialog" />
    </el-dialog>
  </div>
</template>

<script>
// import { useStore } from 'vuex'
// import { useRouter } from 'vue-router'
import { reactive, ref } from '@vue/runtime-core'
import ForgetDialog from './ForgetPwd.vue'
import { ElDialog, ElButton } from 'element-plus'
export default {
  name: "LoginComponent",
  components: {
    ForgetDialog,
    ElDialog,
    ElButton
  },
  setup() {
    let userLoginForm = reactive({
      username: "",
      password: ""
    })
    let showForget = ref(false)
    //const store = useStore()
    //const router = useRouter()
    // const { proxy } = getCurrentInstance()
    let error = ref('')
    function showForgetDialog() {
      showForget.value = false
    }
    //获取用户登录信息
    async function usreList() {

    }
    //获取用户信息
    async function getUserInfo() {

    }
    return {
      userLoginForm, error, showForget,
      usreList, getUserInfo, showForgetDialog
    }
  }
}
</script>

<style lang="less" scoped>
@keyframes animate {
  0% {
    filter: hue-rotate(0deg);
  }

  100% {
    filter: hue-rotate(360deg);
  }
}

#login {
  position: relative;
  width: 100vw;
  height: 100vh;
  background-image: url(../../../assets/loginback.jpg);
  background-size: 100% 100%;
  background-color: #a7a8bd;

  #contain {
    height: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 25px;
    border: 1px solid black;
    background-color: rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(5px);
    box-shadow: -5px -5px 10px rgb(39, 65, 65),
      5px 5px 20px aqua;
    /* 5秒 infinite循环播放无限次 linear匀速  */
    animation: animate 5s linear infinite;
  }
}

#contain {
  display: flex;
  flex-direction: row;
  text-align: center;
  align-items: center;

  #left_card {
    width: 500px;

    h1 {
      color: white;
      white-space: nowrap;
    }

    span {
      font-size: 1.2rem;
      text-align: center;
      color: white;
      white-space: nowrap;
    }
  }

  #right_card {
    width: 400px;

    .el-card {
      margin: 0 45px;
      border-radius: 25px;
      background-color: rgba(255, 255, 255, 0.1);
    }
  }
}

#right_card {
  display: flex;
  justify-content: center;
  align-items: center;

  h2 {
    margin-bottom: 5px;
  }

  position: relative;

  .forgetPwd {
    position: absolute;
    top: 172px;
    right: 65px;
    border: none;
    color: gray;
    font-size: 10px;
    text-decoration: none;
    background-color: transparent;
  }

  .forgetPwd:hover {
    text-decoration: underline;
  }

  .forgetPwd:active {
    color: lightgray;
  }

  .login {
    input {
      width: 80%;
      height: 45px;
      margin-top: 10px;
      border: 1px solid white;
      background-color: rgba(255, 255, 255, 0.5);
      border-radius: 10px;
      font-size: inherit;
      padding-left: 20px;
      outline: none;
    }
  }


  .message {
    margin-top: 26px;
    font-size: 0.9rem;
    color: red;
  }

  .loginbtn {
    width: 100%;
    height: 35px;
    margin-top: 10px;
    border-radius: 10px;
    background-color: rgba(207, 38, 38, 0.8);
  }

}
</style>
<style scoped>
.logo-img {
  width: 67%;
  /* 设置合适的宽度 */

}
</style>