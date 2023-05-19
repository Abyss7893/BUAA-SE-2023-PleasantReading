<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="head-top">
    <div>
      <a class="logoa" href="/"><img class="logo" src="~assets/logo-yixinyuedu.png" alt=""></a>
    </div>
    <div class="dropdown">
      <form action="" method="get">
        <div class="search">
          <input type="text" name="" id="" placeholder="想看什么我这里都有哟~" @focusin="drop" @focusout="hide" />
          <input type="submit" value="" />
        </div>
      </form>
      <div class="dropdown-content" ref="hidden">
        <div class="first-want">大家都想看</div>
        <div class="want">重生之我在北航卖西瓜</div>
        <div class="want">青春北航男童不会梦到清华女学长</div>
        <div class="want">你还爱我吗</div>
        <div class="want">占位符1</div>
        <div class="want">占位符2</div>
      </div>
    </div>
    <div class="login-register">
      <template v-if="isLogin === false">
        <!-- <LoginComponent></LoginComponent> -->
        <router-link to="/login">登录</router-link>
        <a href="#" @mousedown="login">登录</a>
        <router-link to="/register">注册</router-link>
      </template>
      <template v-if="isLogin === true">
        <div class="avatar">
          <ElDropdown trigger="click">
            <ElAvatar icon="user">
            </ElAvatar>
            <template #dropdown>
              <el-dropdown-menu class="dropDownMenu">
                <el-dropdown-item icon="house">个人中心</el-dropdown-item>
                <el-dropdown-item icon="memo">我的书架</el-dropdown-item>
                <el-dropdown-item icon="notebook">我的书签</el-dropdown-item>
                <el-dropdown-item icon="user">VIP管理</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </ElDropdown>
        </div>
      </template>
    </div>
  </div>
</template>


<script>
import "css/head/headtop.css";
//import LoginComponent from "@/components/login/LoginComponent.vue";
import { ElAvatar, ElDropdown, ElDropdownMenu, ElDropdownItem } from "element-plus";
export default {
  name: "Head_Top",
  components: {
    //LoginComponent
    ElAvatar,
    ElDropdown,
    ElDropdownItem,
    ElDropdownMenu,
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin
    },
  },

  methods: {
    login() {
      this.$store.commit('refresh')
    },
    drop() {
      this.$refs.hidden.style.display = "block"
    },
    hide() {
      this.$refs.hidden.style.display = "none"
    }
  }
};
</script>
<style>
.dropDownMenu {
  --el-dropdown-menuItem-hover-fill: #f56c6c;
  --el-dropdown-menuItem-hover-color: white;
}
</style>