<template>
  <HeadTop />
  <div class="contain">
    <div class="mask" v-if="showMyCard"></div>
    <MyCard class="mycard" v-if="showMyCard" @close="showMyCard=false"></MyCard>
    <ElDialog v-model="test" :destroy-on-close="true">
      <CropComponent @close="test = false" />
    </ElDialog>
    <ElDialog v-model="showPayDialog" title="充值VIP" :destroy-on-close="true" width="900px">
      <PayComponent />
    </ElDialog>
    <ElDialog v-model="showChangePwd" title="修改密码" :destroy-on-close="true" width="25%">
      <ChangePwd @close="showChangePwd = false" />
    </ElDialog>


    <div class="PersonTop">
      <div class="PersonTop_image">
        <ElAvatar :src="avatar" shape="circle" fit="fill" :size="140"></ElAvatar>
      </div>
      <div class="PersonTop_text">
        <div class="user_text">
          <div class="user_qianming">
            <span> {{ design }}</span>
          </div>
          <div class="user_anniu">
            <el-button class="el-icon-edit pink-button" @click="setAvatar">上传头像</el-button>
          </div>

        </div>
      </div>
      <div class="PersonTop_right">
        <el-button icon="star" @click="openPayDia()">充值会员</el-button>
        <el-button icon="star" @click="showChangePwd = true">修改密码</el-button>
        <el-button icon="switchButton" @click="signOut">退出登录</el-button>
      </div>
    </div>
    <div class="person_body">
      <div class="person_body_left">
        <el-card class="box-card" :body-style="{ padding: '0px' }">
          <div class="clearfix">
            <span class="person_body_list" style="border-bottom: none;">个人中心</span>
          </div>
          <el-menu router active-text-color="#fffff" class="el-menu-vertical-demo">
            <el-menu-item class="menu-item" @click="$router.push({ name: 'info' })">
              <el-icon>
                <User />
              </el-icon>
              <span class="text" >个人简介</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push({ name: 'comment' })">
              <el-icon>
                <ChatLineSquare />
              </el-icon>
              <span class="text">我的评论</span>
            </el-menu-item>
            <el-menu-item class="menu-item">
              <el-icon>
                <Notebook />
              </el-icon>
              <span class="text">我的笔记</span>
            </el-menu-item>
            <el-menu-item class="menu-item">
              <el-icon>
                <Flag />
              </el-icon>
              <span class="text">我的书签</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push('/mybook')">
              <el-icon>
                <Reading />
              </el-icon>
              <span class="text">我的书架</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push('/')">
              <el-icon>
                <Back />
              </el-icon>
              <span class="text" >返回主界面</span>
            </el-menu-item>
          </el-menu>
        </el-card>
      </div>
      
      <div class="person_body_right">
        <router-view></router-view>
      </div>
    </div>
    

  </div>
  <WebFoot/>
</template>

<script>

//import PersonalDia from "./PersonalDialog.vue";
//import Cropper from 'cropperjs';
import CropComponent from './Personal/CropComponent.vue'
import ChangePwd from './Personal/ChangePwd.vue';
import '../../../node_modules/cropperjs/dist/cropper.min.css'
import WebFoot from '../veiw/foot/WebFoot.vue';
import { ElAvatar, ElButton, ElDialog } from 'element-plus';
import HeadTop from '../veiw/head/HeadTop';
//import axios from 'axios';
import { ref, computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router';
import PayComponent from './Personal/PayComponent.vue';
export default {

  name: "PersonalCenter",
  inject: ["reload"],
  components: { ElAvatar, HeadTop, ElButton, ElDialog, PayComponent, WebFoot, CropComponent, ChangePwd },
  setup() {
    const test = ref(false)
    const store = useStore();
    const router = useRouter();
    const design = ref("");
    const showPayDialog = ref(false);
    const isfollow = ref(true);
    const showChangePwd = ref(false)
    const showMyCard=ref(false)
    const followData = ref({
      fanId: "",
      followId: "",
    });
    const isfollowid = ref([]);
    const VIP = computed(() => {
      return store.state.isVip;
    });
    const avatar = computed(() => {
      return store.state.userAvatar
    })
    // router.push({ name: 'info' });

    function signOut() {
      store.commit('signOut');
      router.push('/');
    }
    function openPayDia() {
      showPayDialog.value = true;
    }
    function setAvatar() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*'
      input.click();
      input.addEventListener('change', () => {
        const imageFile = input.files[0];
        // 创建一个 FileReader 对象，将文件读取成 base64 编码的字符串
        const reader = new FileReader();
        reader.readAsDataURL(imageFile);
        reader.onload = function (event) {
          const dataURL = event.target.result;
          store.commit('setTempAvatar', dataURL)
          test.value = true
        }
      });
    }
    function closeCrop() {
      test.value = false;
    }
    return {
      avatar,
      design,
      isfollow,
      followData,
      isfollowid,
      VIP,
      showPayDialog,
      showChangePwd,
      test,
      showMyCard,
      signOut,
      openPayDia,
      setAvatar,
      closeCrop
    }
  }
};
</script>

<style scoped>
.contain {
  background-image: url('../../assets/personalbg.png');
  background-size: cover;
  display: flex;
  background-position: center;
  background-attachment: fixed; /* 添加属性 */
  position: relative;
  flex-direction: column;
  width: 100%;
  height: 850px;
  min-height: 70vh;
}
.mycard{
  z-index: 1000;
}
.el-menu-vertical-demo{
  font-size: 20px;
}

.text{

  font-size: 20px;
}
.clearfix{
  margin-top: 10px;
}
.menu-item{
  height: 80px;
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
.person_bottom{
  width: 100%;
  height: 50px;
  min-height: 50px;
  justify-content: space-between;
  font-size: 14px;
  position: fixed; /* 修改属性 */
  bottom: 121px; /* 添加属性 */
}
.userAvatar {
  margin-top: 10px;
  margin-left: 20px;
}

.PersonTop {
  width: 1000px;
  height: 200px;
  min-height: 200px;
  padding-top: 20px;
  background-color: white;
  background-image: url(../../assets/personTopbg.png);
  background-repeat: no-repeat;
  background-position: center;
  margin-top: 12px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  border-radius: 5px;
}

.PersonTop_right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  margin-right: 20px;
}

.PersonTop_right .el-button {
  margin-top: 20px;
}

.PersonTop_image {
  margin-left: 20px;
  margin-top: 10px;
}

.el-avatar>img {
  width: 100%;
  height: 100%;
}

.PersonTop_text {
  height: 120px;
  width: 880px;
  display: flex;
}

.user_text {
  width: 60%;
  height: 100%;
  line-height: 30px;
}


.user_anniu {
  margin-top: 140px;
  margin-right: 10px;
}

.user_qianming {
  font-size: 14px;
  color: #999;
}


/*下面部分样式*/
.person_body {
  flex-grow: 1;
  width: 1000px;
  margin-top: 230px;
  display: flex;
  position: absolute;
  left: 50%;
  
  transform: translateX(-50%);
  border-radius: 5px;
}

.person_body_left {
  width: 27%;
  height: 380px;

  border-radius: 5px;
  margin-right: 3%;
  text-align: center;
}
.pink-button {
  background-color: #fcdfe3; /* 设置按钮默认背景色 */
  color: #fff; /* 设置文字颜色 */
  padding: 10px 20px; /* 设置按钮内边距 */
  border-radius: 4px; /* 设置按钮圆角 */
  /* 使用 hover 伪类实现鼠标悬浮时改变背景色的效果 */
  /* 当鼠标悬浮时，将背景色改为淡粉色 */
  background-color: #ffdce0;
}
.person_body_list {
  width: 100%;
  height: 50px;
  margin-top: 25px;
  font-size: 30px;
  border-bottom: 1px solid #f0f0f0;
  background-image: -webkit-linear-gradient(left,
      rgb(42, 134, 141),
      #e9e625dc 20%,
      #3498db 40%,
      #e74c3c 60%,
      #09ff009a 80%,
      rgba(82, 196, 204, 0.281) 100%);
  -webkit-text-fill-color: transparent;
  background-clip: text;
  background-size: 200% 100%;
  animation: masked-animation 4s linear infinite;
}

.person_body_right {
  width: 70%;
  /* height: 500px; */
  margin-top: 40px;
  border-radius: 5px;

}

.box-card {
  height: 523px;
  min-height: 380px;
  margin-top: 40px;
  margin-right: 30px;
}
</style>