<template>
  <HeadTop :holdplace="true" />
  <div class="contain">
    <div class="mask" v-if="showMyCard"></div>
    <div class="mask" v-if="showChangePwd"></div>
    <MyCard class="mycard" v-if="showMyCard" @close="showMyCard = false"></MyCard>
    <ElDialog v-model="test" :destroy-on-close="true" width="600px">
      <CropComponent @close="test = false" @reloadAvatar="setAvatar" v-if="test" />
    </ElDialog>
    <ElDialog v-model="showPayDialog" title="充值VIP" :destroy-on-close="true" width="900px">
      <PayComponent />
    </ElDialog>
    <!-- <ElDialog v-model="showChangePwd" v-if="showChangePwd" draggable style="border: none; background-color: transparent;" modal="true"  :destroy-on-close="true" width="25%"> -->
    <ChangePwd class="change-pwd" v-if="showChangePwd" @close="showChangePwd = false" />
    <!-- </ElDialog> -->
    <div class="PersonTop">
      <div class="PersonTop_image">
        <ElAvatar :src="avatar" shape="circle" fit="fill" :size="140"></ElAvatar>
      </div>
      <div class="PersonTop_text">
        <div class="user_text">
          <div class="user_qianming">
            <span> {{ store.state.userInfo.nickname }}</span>
          </div>
          <div class="motto">
            <div class="mysvg">
              <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M460.8 36.498286c8.045714 0 14.628571 6.582857 14.628571 14.628571v58.514286a14.628571 14.628571 0 0 1-14.628571 14.628571L124.342857 124.342857v775.314286h775.314286v-117.028572c0-8.045714 6.582857-14.628571 14.628571-14.628571h58.514286c8.045714 0 14.628571 6.582857 14.628571 14.628571V950.857143a36.571429 36.571429 0 0 1-36.571428 36.571428H73.142857a36.571429 36.571429 0 0 1-36.571428-36.571428V73.142857A36.571429 36.571429 0 0 1 73.142857 36.571429L460.8 36.498286z m158.573714 44.982857a43.885714 43.885714 0 0 1 61.878857-5.412572l79.140572 66.56C852.333714 19.017143 1024 68.388571 1024 217.673143c0 25.6-2.925714 42.203429-15.652571 71.753143l-8.850286 19.529143-18.505143 37.302857-7.68 15.213714c-56.685714 111.177143-61.732571 173.933714 6.436571 264.557714a36.571429 36.571429 0 0 1-58.514285 43.958857c-84.845714-112.859429-81.554286-201.142857-20.992-325.997714l25.307428-50.395428 8.557715-17.773715 6.509714-14.409143 2.486857-6.217142 3.803429-10.825143c2.048-6.582857 3.145143-12.288 3.657142-17.993143l0.292572-8.777143c0-77.531429-83.017143-101.302857-134.217143-28.013714l60.708571 50.980571a43.885714 43.885714 0 0 1 5.412572 61.805714l-378.587429 451.218286a43.885714 43.885714 0 0 1-27.501714 15.213714l-189.586286 26.843429a43.885714 43.885714 0 0 1-50.029714-41.910857l-6.509714-191.414857a43.885714 43.885714 0 0 1 10.24-29.696z m38.985143 89.965714L318.902857 576.219429l4.242286 125.805714 124.635428-17.627429 339.529143-404.699428-128.877714-108.105143z">
                </path>
              </svg>
            </div>
            <div class="user-motto">
              <span>{{ store.state.userInfo.motto }}</span>
            </div>
          </div>
          <div class="ip">
            <div class="mysvg">
              <svg style="width: 22px; " viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M511.9 938.7c-12.4 0-24.2-5.4-32.4-14.9-6.9-8.1-170.3-198.4-215-258.4-62.4-83.8-94-164.1-94-238.8 0-110.7 54-214.9 144.5-278.9 92.2-65.2 208.5-80.2 319.4-40.9 43.2 15.3 83.5 42.9 116.3 79.7 134.3 150.7 137 316.6 7.7 479.9-51.1 64.6-207.3 249.3-214 257.1-8.1 9.5-19.9 15.1-32.4 15.1 0 0.1-0.1 0.1-0.1 0.1z m0.1-767.9c-52.9 0-104 15.8-147.7 46.6-67.9 48-108.4 126.2-108.4 209.2 0 55.9 26 119.1 77.1 187.9 31.1 41.8 127.5 155.6 178.7 215.6 49.9-59.2 143.6-170.8 179.8-216.6 103-130.1 101.6-251.3-4.4-370.2-23.3-26.1-51.4-45.5-81.1-56-31.2-11-63-16.5-94-16.5z m-0.1 405.2c-82.3 0-149.3-67-149.3-149.3s67-149.3 149.3-149.3 149.3 67 149.3 149.3S594.2 576 511.9 576z m0-213.3c-35.3 0-64 28.7-64 64s28.7 64 64 64 64-28.7 64-64-28.7-64-64-64z">
                </path>
              </svg>
            </div>
            <div class="user-ip">
              <span>IP属地:北京</span>
            </div>

          </div>
          <el-divider style="width: 500px; margin: 20px 0 0 20px;"></el-divider>
          <div class="user_num">
            <div class="collections" @click="$router.push('/mybook')">
              <div class="num_number">{{ num.collections }}</div>
              <span class="num_text">收藏</span>
            </div>
            <div class="mark" @click="$router.push('/mark')">
              <div class="num_number">{{ num.marks }}</div>
              <span class="num_text">书签</span>
            </div>
            <div class="note" @click="$router.push('/mynote')">
              <div class="num_number">{{ num.notes }}</div>
              <span class="num_text">笔记</span>
            </div>
          </div>
          <!-- <div class="user_anniu">
            <el-button class="el-icon-edit pink-button" @click="setAvatar">上传头像</el-button>
          </div> -->

        </div>
      </div>
      <div class="PersonTop_right">

        <!-- <el-button icon="star" @click="openPayDia()" class="pink-button">充值会员</el-button>
        <el-button icon="star" @click="showChangePwd = true" class="pink-button">修改密码</el-button>
        <el-button icon="switchButton" @click="signOut" class="pink-button">退出登录</el-button> -->
      </div>
    </div>
    <div class="person_body">
      <div class="person_body_left">
        <el-card class="box-card" :body-style="{ padding: '0px' }">
          <div class="clearfix">
            <span class="person_body_list" style="border-bottom: none;">个人中心</span>
          </div>
          <el-divider style=" margin: 5px 0 0 0;"></el-divider>
          <el-menu router active-text-color="#fffff" class="el-menu-vertical-demo">
            <el-menu-item class="menu-item" @click="$router.push({ name: 'info' })">
              <el-icon>
                <User />
              </el-icon>
              <span class="text">个人简介</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push({ name: 'comment' })">
              <el-icon>
                <ChatLineSquare />
              </el-icon>
              <span class="text">我的评论</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push('/mynote')">
              <el-icon>
                <Notebook />
              </el-icon>
              <span class="text">我的笔记</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push('/mark')">
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
            <el-divider style=" margin: 0px 0 0 0;"></el-divider>
            <el-menu-item class="menu-item" @click="setAvatar">
              <el-icon>
                <Avatar />
              </el-icon>
              <span class="text">上传头像</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="showChangePwd = true">
              <el-icon>
                <Lock />
              </el-icon>
              <span class="text">修改密码</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="openPayDia()">
              <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M558.811429 155.574857a73.142857 73.142857 0 0 1 9.386666 9.386667L707.047619 331.580952l153.161143-113.103238a73.142857 73.142857 0 0 1 114.419809 76.556191L828.952381 877.714286H195.047619L49.371429 295.058286A73.142857 73.142857 0 0 1 163.791238 218.453333L316.952381 331.580952l138.849524-166.619428a73.142857 73.142857 0 0 1 103.033905-9.386667zM512 211.772952l-183.003429 219.623619-208.65219-154.087619L252.14781 804.571429h519.70438l131.803429-527.262477-208.65219 154.087619L512 211.772952z m170.666667 457.874286v78.019048H341.333333v-78.019048h341.333334z">
                </path>
              </svg>
              <span class="text">充值VIP</span>
            </el-menu-item>
            <el-menu-item class="menu-item" @click="$router.push('/')">
              <el-icon>
                <Back />
              </el-icon>
              <span class="text">返回主界面</span>
            </el-menu-item>
          </el-menu>
        </el-card>
      </div>

      <div class="person_body_right">
        <router-view></router-view>
      </div>
    </div>


  </div>
  <WebFoot />
</template>

<script>

//import PersonalDia from "./PersonalDialog.vue";
//import Cropper from 'cropperjs';
import CropComponent from './Personal/CropComponent.vue'
import ChangePwd from './Personal/ChangePwd.vue';
import '../../../node_modules/cropperjs/dist/cropper.min.css'
import WebFoot from '../veiw/foot/WebFoot.vue';
import { ElAvatar, ElDialog } from 'element-plus';
import HeadTop from '../veiw/head/HeadTop';
//import axios from 'axios';
import { ref, computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router';
import PayComponent from './Personal/PayComponent.vue';
export default {

  name: "PersonalCenter",
  inject: ["reload"],
  components: { ElAvatar, HeadTop, ElDialog, PayComponent, WebFoot, CropComponent, ChangePwd },
  setup() {
    const test = ref(false)
    const store = useStore();
    const router = useRouter();
    const design = ref("");
    const showPayDialog = ref(false);
    const isfollow = ref(true);
    const showChangePwd = ref(false)
    const showMyCard = ref(false)
    const followData = ref({
      fanId: "",
      followId: "",
    });
    const isfollowid = ref([]);
    const num = computed({
      get() {
        return store.state.num;
      },
      set(value) {
        store.commit('updateNum', value);
      }
    });

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
          test.value = false
          setTimeout(() => {
            test.value = true
          }, 200);
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
      store,
      showMyCard,
      num,
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
  background-image: url('../../assets/personalbg2.png');
  background-size: 100%;
  background-color: #f7f8fc !important;
  display: flex;
  background-position: center;
  background-attachment: fixed;
  /* 添加属性 */
  position: relative;
  flex-direction: column;
  width: 100%;
  height: 850px;
  min-height: 70vh;
}

.mycard {
  z-index: 1000;
}

.el-menu-vertical-demo {
  font-size: 20px;
}

.text {

  font-size: 20px;
}

.clearfix {
  margin-top: 10px;
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

.person_bottom {
  width: 100%;
  height: 50px;
  min-height: 50px;
  justify-content: space-between;
  font-size: 14px;
  position: fixed;
  /* 修改属性 */
  bottom: 121px;
  /* 添加属性 */
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
  background-image: url("../../assets/imgs/personaltop.png");
  background-size: 332.8px 300.2px;
  background-repeat: no-repeat;

  background-position: 720px -70px;
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

.user-motto {
  margin: 10px 0 0 10px;
}

.user_text {
  width: 60%;
  height: 100%;
  line-height: 30px;
}


.user_anniu {
  margin-top: 20px;
  margin-left: 25px;
  margin-right: 10px;
}

.user_qianming {
  font-size: 16px;
  line-height: 21px;
  font-weight: 600;
  margin: 15px 0 0 25px;
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

.icon {
  width: 18px;
  margin-left: 0px;
  margin-right: 10px;
}

.person_body_left {
  width: 27%;
  height: 480px;

  border-radius: 5px;
  margin-right: 3%;
  text-align: center;
}

.el-menu-vertical-demo .el-menu-item:hover {
  background-color: #f5e7ea;
}

.pink-button {
  background-color: #fcdfe3;
  /* 设置按钮默认背景色 */
  color: #fff;
  /* 设置文字颜色 */
  padding: 10px 20px;
  /* 设置按钮内边距 */
  border-radius: 4px;
  /* 设置按钮圆角 */
  /* 使用 hover 伪类实现鼠标悬浮时改变背景色的效果 */
  /* 当鼠标悬浮时，将背景色改为淡粉色 */
  background-color: #ffdce0;
}

.ip {
  margin-left: -3px;
  display: flex;
}

.num_number {
  font-size: 20px;
  color: #333;
}


.user_num .collections:hover,
.user_num .note:hover,
.user_num .mark:hover {
  color: #f8b2b27d;
  cursor: pointer;
}

.user_num .collections:hover .num_number,
.user_num .note:hover .num_number,
.user_num .mark:hover .num_number {
  color: #f8b2b27d;
  cursor: pointer;
}

.user_num .collections:hover .num_text,
.user_num .note:hover .num_text,
.user_num .mark:hover .num_text {
  color: #f8b2b27d;
  cursor: pointer;
}

.user_num {
  width: 200px;
  height: 100px;
  margin: -50px 0 0 20px;
  display: flex;
  align-items: center;
}


.user_num>div {
  text-align: center;
  border-right: 1px dotted #999;
  box-sizing: border-box;
  width: 80px;
  height: 40px;
  margin: 80px 20px 20px 0;
  line-height: 20px;
}

.num_text {
  color: #999;
}

.user-ip {
  margin: 12px 0 0 13px;
}

.motto {
  display: flex;
}

.mysvg {
  margin: 15px 0 5px 25px;
  height: 18px;
  width: 18px;
}

.person_body_list {
  width: 100%;
  height: 50px;
  margin-top: 20px;
  font-size: 25px;
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
  height: 550px;
  min-height: 480px;
  margin-top: 40px;
  margin-right: 30px;
}

.change-pwd {
  z-index: 1000;
  display: flex;
  position: absolute;
  margin: 200px 0 0 600px;
}</style>