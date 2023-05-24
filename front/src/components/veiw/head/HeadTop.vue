<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="head-top">
    <!-- <check-login/> -->
    <div>
      <a class="logoa" href="/"><img class="logo" src="~assets/logo-yixinyuedu.png" alt="" /></a>
    </div>
    <div class="dropdown">
      <form action="" method="get">
        <div class="search">
          <input type="text" name="" id="" placeholder="想看什么我这里都有哟~" @focusin="drop" @focusout="hide" />
          <button type="submit">
            <el-icon>
              <Search />
            </el-icon>
          </button>
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
      <template v-if="!isLogin">
        <router-link to="/login">登录</router-link>
        <router-link to="/register">注册</router-link>
      </template>
      <template v-else>
        <div class="avatar">
          <ElDropdown trigger="click">
            <!-- 这里暂时用的是svg库里的图标，后期需要通过得到后端的数据换上人物头像 -->
            <ElAvatar :src="avatar"> </ElAvatar>
            <template #dropdown>
              <el-dropdown-menu class="personal-dropdown-menu">

                <a href="/user">
                  <el-dropdown-item icon="house">个人中心</el-dropdown-item>
                </a>

              <!-- <router-link :to="{ name: 'mybook' }">
                  <el-dropdown-item icon="memo"
                    >我的书架</el-dropdown-item
                  ></router-link
                                                    > -->

                <router-link :to="{ name: 'mybook' }">
                  <el-dropdown-item icon="memo">我的书架</el-dropdown-item>
                </router-link>
                <el-dropdown-item icon="notebook">我的书签</el-dropdown-item>
                <el-dropdown-item icon="user">VIP管理</el-dropdown-item>
                <el-dropdown-item icon="switchButton" @click="signOut">退出登录</el-dropdown-item>
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
import {
  ElAvatar,
  ElDropdown,
  ElDropdownMenu,
  ElDropdownItem,
} from "element-plus";
export default {
  name: "Head_Top",
  components: {
    ElAvatar,
    ElDropdown,
    ElDropdownItem,
    ElDropdownMenu,
  },
  computed: {
    avatar() {
      return this.$store.state.userAvatar;
    },
    isLogin() {
      return this.$store.state.isLogin;
    },
  },
  methods: {
    drop() {
      this.$refs.hidden.style.display = "block";
    },
    hide() {
      this.$refs.hidden.style.display = "none";
    },
    signOut() {
      this.$store.commit("signOut")
      this.$router.push('/');
    },
  },
};
</script>
<style>
.personal-dropdown-menu {
  --el-dropdown-menuItem-hover-fill: #f56c6c;
  --el-dropdown-menuItem-hover-color: white;
}
</style>