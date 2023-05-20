<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="head-top">
    <!-- <check-login/> -->
    <div>
      <a class="logoa" href="/"><img class="logo" src="../../../assets/logo-yixinyuedu.png" alt=""></a>
    </div>
    <form action="" method="get">
      <div class="search">
        <input type="text" name="" id="" placeholder="查询" />
        <input type="submit" value="" />
      </div>
    </form>

    <div class="login-register">
      <template v-if="!isLogin">

        <router-link to="/login">登录</router-link>
        <a href="#" @mousedown="login">登录</a>
        <router-link to="/register">注册</router-link>
      </template>
      <template v-else>
        <div class="avatar">
          <ElDropdown trigger="click">
            <!-- 这里暂时用的是svg库里的图标，后期需要通过得到后端的数据换上人物头像 -->
            <ElAvatar icon="user">
            </ElAvatar>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item icon="house">
                  <RouterLink to="/user">个人中心</RouterLink>
                </el-dropdown-item>
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
// import CheckLogin from '../../check/checkLogin.vue';
export default {
  name: "Head_Top",
  components: {
    //LoginComponent
    ElAvatar,
    ElDropdown,
    ElDropdownItem,
    ElDropdownMenu,
    // CheckLogin,
  },
  computed: {
    isLogin() {
      // console.log(this.$store.state.isLogin)
      return this.$store.state.isLogin
    },
  },
  methods: {
    login() {
      this.$store.commit('refresh')
    },
  }
};
</script>
<style>
.personal-dropdown-menu {
  --el-dropdown-menuItem-hover-fill: #f56c6c;
  --el-dropdown-menuItem-hover-color: white;
}
</style>