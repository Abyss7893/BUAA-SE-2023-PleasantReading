<template>
  <div class="pop-wrap">
    <div class="pop">
      <router-link to="/user/info">
        <div class="username">{{ this.$store.state.userInfo.username }}</div>
      </router-link>
      <div class="motto">{{ this.$store.state.userInfo.motto }}</div>
      <div v-if="this.$store.state.userInfo.VIPDate" class="vipicon"><svg t="1685449539862" class="icon"
          viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2404" width="24" height="24">
          <path
            d="M512 256a85.333333 85.333333 0 1 0 0-170.666667 85.333333 85.333333 0 0 0 0 170.666667z m0-42.666667a42.666667 42.666667 0 1 1 0-85.333333 42.666667 42.666667 0 0 1 0 85.333333z m-202.218667 317.397334a21.333333 21.333333 0 0 0 26.069334-4.458667L512 330.56l176.149333 195.712a21.333333 21.333333 0 0 0 26.069334 4.458667l196.522666-107.2L835.136 896H188.949333l-14.122666-91.968H738.346667a21.333333 21.333333 0 1 0 0-42.666667H149.973333a21.333333 21.333333 0 0 0-21.077333 24.576l20.693333 134.634667A21.333333 21.333333 0 0 0 170.666667 938.666667h682.666666a21.333333 21.333333 0 0 0 21.056-17.962667l85.333334-533.333333a21.333333 21.333333 0 0 0-31.274667-22.101334l-219.861333 119.936-180.736-200.810666a21.333333 21.333333 0 0 0-31.701334 0l-180.736 200.810666L95.573333 365.269333a21.333333 21.333333 0 0 0-31.274666 22.208l46.165333 278.677334A21.333333 21.333333 0 0 0 152.533333 659.2L113.536 423.68l196.266667 107.050667z"
            fill="#ed4259" p-id="2405"></path>
        </svg>会员到期时间:<div class="vip-date">{{ this.$store.state.userInfo.VIPDate }}<div class="vip-goon" @click="openPay">
            续费</div>
        </div>
      </div>
      <div class="vip-null" v-else>
        您还不是会员哦~<div class="vip-on" @click="openPay">开通</div>
      </div>
      <div class="fav">
        <div class="shelf">
          <div class="num">123</div>
          <div>收藏</div>
        </div>
        <div class="note">
          <div class="num">123</div>
          <div>笔记</div>
        </div>
        <div class="mark">
          <div class="num">123</div>
          <div>书签</div>
        </div>
      </div>
      <div class="vip-entry-containter">
        <div class="vip-entry-desc">
          <p class="vip-entry-desc-title" style="color: rgb(255, 102, 153);">我的VIP</p>
          <p class="vip-entry-desc-subtitle" style="color: rgb(97, 102, 109);">热门书籍看不停</p>
        </div>
        <div @click="jumpToVip" class="vip-entry-btn" style="color: rgb(255, 102, 153); background: rgb(255, 255, 255);">
          会员中心</div>
      </div>
      <router-link to="/user/info">
        <li class="usercenter">
          <div><el-icon>
              <UserFilled />
            </el-icon>个人中心</div><el-icon>
            <ArrowRight />
          </el-icon>
        </li>
      </router-link>
      <li class="service">
        <div><el-icon>
            <Star />
          </el-icon>推荐服务</div><el-icon>
          <ArrowRight />
        </el-icon>
      </li>
      <el-divider direction="horizontal" />
      <li class="logout" @click="signOut()">
        <div><el-icon>
            <SwitchButton />
          </el-icon>退出登录</div>
      </li>
    </div>
  </div>
  <el-dialog v-model="pay" title="充值VIP" :destroy-on-close="true" width="900px">
    <PayComponent />
  </el-dialog>
</template>

<script>
import PayComponent from '@/components/page/Personal/PayComponent.vue';
import { getBriefInfo } from '@/api/api'
export default {
  name: "popUserInfo",
  components: { PayComponent, },
  data() {
    return {
      pay: false,
    };
  },
  created() {
    getBriefInfo().then((data) => {
      if (data.status && data.status == 200)
        console.log(data)
    })
  },
  methods: {
    jumpToVip() {
      this.$router.push("/allbook?vip=true")
    },
    signOut() {
      this.$store.commit("signOut")
      console.log(this.$route.path)
      if (this.$route.path === '/user/info' || this.$route.path === '/user/comment' || this.$route.path === '/user')
        this.$router.push('/');
    },
    openPay() {
      this.pay = true
    },
  },
};
</script>
<style lang="scss" scoped>
.pop-wrap {
  position: absolute;
  top: 20px;
  left: -8px;
  z-index: 150;
}

.pop {
  padding: 24px;
  position: absolute;
  background-color: #fff;
  width: 300px;
  border-radius: 10px;
  transform: translate(-50%, 0);
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, .2);
}


.username {
  font-family: PingFang SC, HarmonyOS_Regular, Helvetica Neue, Microsoft YaHei, sans-serif;
  font-weight: 500;
  font-size: 24px;
  color: rgb(251, 114, 153);
  margin-top: 12px;
  width: 100%;
  display: flex;
  justify-content: center;
}

.vip-entry-containter {
  background-image: url("~assets/imgs/vipcenter.png");
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 12px;
  border-radius: 6px;
  background-size: cover;
  transition: background-color .2s;
}

.vip-entry-btn {
  cursor: pointer;
  padding: 6px 0;
  margin-left: 8px;
  width: 68px;
  line-height: 17px;
  font-size: 14px;
  text-align: center;
  border-radius: 6px;
}

.pop li {
  cursor: pointer;
  transition: background-color .3s ease-in-out;
  display: flex;
  justify-content: space-between;
  border-radius: 6px;
  padding: 12px;
  margin: 4px 0 4px 0;
  font-size: 18px;
  text-align: center;
  position: relative;
}

.pop li .el-icon {
  position: relative;
  top: 3px;
}

.pop li div .el-icon {
  margin-right: 8px;
}

.pop .el-divider {
  margin: 8px 0 8px;
}

.pop li:hover {
  background-color: #f8b2b27d;
}

.fav {
  padding-top: 8px;
  display: flex;
  justify-content: space-between;
}

.fav div.shelf,
.fav div.note,
.fav div.mark {
  transition: color .2s;
  margin: 16px;
  color: #9499A0;
}

.fav div.num {
  transition: color .2s;
  color: #000;
  font-weight: bold;
  font-size: 20px;
}

.fav .shelf:hover,
.fav .note:hover,
.fav .mark:hover {
  color: #f8b2b27d;
  cursor: pointer;
}

.fav .shelf:hover .num,
.fav .note:hover .num,
.fav .mark:hover .num {
  color: #f8b2b27d;
  cursor: pointer;
}

.vipicon {
  font-size: 18px;
  font-weight: 900;
  margin-top: 8px;
}

.vipicon svg {
  position: relative;
  top: 4px;
}

.vipicon .vip-date,
.motto,
.vip-null {
  display: flex;
  justify-content: center;
}

.vipicon .vip-date {
  font-weight: 100;
  font-size: 16px;
  margin-top: 16px;
  width: 100%;
}

.vip-null {
  margin-top: 16px;
  width: 100%;
}


.motto {
  padding-top: 8px;
  font-weight: 100;
  font-size: 16px;
}

.vip-on,
.vip-goon {
  position: absolute;
  font-size: 14px;
  border: 1px solid #9499A0;
  cursor: pointer;
  border-radius: 6px;
  padding: 2px 8px;
  left: 100%;
  transition: background-color .3s ease-in-out;
}

.vip-goon {
  margin-left: -130px;
  margin-top: -2px;
}

.vip-on {
  position: static;
}

.vip-goon:hover,
.vip-on:hover {
  background-color: #f8b2b27d;
}
</style>