<!-- 网页头部顶侧，包含logo、登录&&注册、搜索栏等 -->
<template>
  <div class="head-top">
    <!-- <check-login/> -->
    <div>
      <a class="logoa" href="/"><img class="logo" src="~assets/logo-yixinyuedu.png" alt="" /></a>
    </div>
    <div class="dropdown">
      <div class="search">
        <input ref="keywords" :value="this.$route.query.keywords" type="text" name="" id="" placeholder="想看什么我这里都有哟~"
          @focusin="drop" @focusout="hide" />
        <button @click="searchBooks()">
          <el-icon>
            <Search />
          </el-icon>
        </button>
      </div>
      <div class="dropdown-content" ref="hidden">
        <div class="first-want">大家都想看</div>
        <div class="want" v-for="(searchHot, idx) in searchHots" :key="idx" @click="searchBooks(searchHot)">{{ searchHot
        }}</div>
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

                <a href="/user/info">
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
  data() {
    return {
      searchHots: ["青春北航男童不会梦到清华女学长", "重生之我在北航卖西瓜", "飘飘何所似", "红楼梦", "杨过"],
    }
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
      this.$refs.hidden.style.maxHeight = '500px';
      this.$refs.hidden.style.paddingBottom = '10px'
    },
    hide() {
      this.$refs.hidden.style.maxHeight = '0';
      this.$refs.hidden.style.paddingBottom = '0'
    },
    signOut() {
      this.$store.commit("signOut")
      this.$router.push('/');
    },
    searchBooks(keywords) {
      if (!keywords)
        keywords = this.$refs.keywords.value
      this.$router.push({ path: '/search', query: { "keywords": keywords, page: 1 } })
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