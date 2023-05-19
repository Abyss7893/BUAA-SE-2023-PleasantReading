<template>
    <div class="contain">
        <HeadTop/>
        <div class="PersonTop">
            <div class="PersonTop_image">
                <ElAvatar src="https://rss.sfacg.com/web/account/images/avatars/app/2010/25/1c44687f-df90-432e-8d35-cf2f46d1665b.jpg" :size="170" fit="contain"></ElAvatar>
            </div>
            <div class="PersonTop_text">
                <div class="user_text">
                    <div class="user_name">
                        <span> 小明 </span>
                    </div>
                    <div class="user_qianming">
                        <span> {{ design }}</span>
                    </div>
                    <div class="user_anniu">
                        <el-button class="el-icon-edit">编辑</el-button>
                    </div>
                </div>
            </div>
        </div>
        <div class="person_body">
            <div class="person_body_left">
                <el-card class="box-card" :body-style="{ padding: '0px' }">
                    <div  class="clearfix">
                        <span class="person_body_list" style="border-bottom: none">个人中心</span>
                    </div>
                    <el-menu router active-text-color="#00c3ff" class="el-menu-vertical-demo">
                        <el-menu-item  @click="$router.push({ name: 'info' })">
                           <el-icon><User /></el-icon>
                            <span >个人简介</span>
                        </el-menu-item>
                        <el-menu-item >
                            <el-icon><ChatLineSquare /></el-icon>
                            <span >我的评论</span>
                        </el-menu-item>
                        <el-menu-item  >
                            <el-icon><Notebook /></el-icon>
                            <span >我的笔记</span>
                        </el-menu-item>
                        <el-menu-item  >
                            <el-icon><Flag /></el-icon>
                            <span >我的书签</span>
                        </el-menu-item>
                        <el-menu-item  >
                            <el-icon><Reading /></el-icon>
                            <span >我的书架</span>
                        </el-menu-item>
                        <el-menu-item  >
                            <el-icon><Back /></el-icon>
                            <span >返回主界面</span>
                        </el-menu-item>
                    </el-menu>
                </el-card>
            </div>
            <div class="person_body_right">
                <router-view></router-view>
            </div>
        </div>
        <el-dialog title="重置密码" v-model="showPersonal" :before-close="handleClose" :close-on-click-modal="false"
              :close-on-press-escape="false" :append-to-body="false" style="min-width: 500px;border-radius: 25px;
              backdrop-filter: blur(5px);">
              <PersonalDialog @submit="handleSubmit" @close="handleClose" />
            </el-dialog>
    </div>
</template>

<script>
import PersonalDialog from './PersonalDialog';
//import PersonalDia from "./PersonalDialog.vue";
import { ElAvatar } from 'element-plus';
import HeadTop from '../veiw/head/HeadTop';
export default {
   
    components: { ElAvatar,HeadTop,PersonalDialog},
    name: "PersonalCenter",
    inject: ["reload"],
    data() {
        return {
            avatar: "",
            nickname: "cyx",
            v: 1,
            design: "",
            followCounts: "",
            fanCounts: "",
            goodCounts: "",
            isfollow: true,
            followData: {
                fanId: "",
                followId: "",
            },
            isfollowid: [],
        };
    },
    methods: {
        edit() {
            this.$refs.dia.open();
        },
    },
};
</script>

<style scoped>
.contain {
  background-image: url('../../assets/personalbg.png');
  background-size: cover;
  
  background-position: center;
   position: relative;
  width: 100%;
  height: 100vh;
}

.PersonTop {
    width: 1000px;
    height: 200px;
    padding-top: 20px;
    background-color: white;
    margin-top: 12px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
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

.user_name {
    font-weight: bold;
}

.user_qianming {
    font-size: 14px;
    color: #999;
}


/*下面部分样式*/
.person_body {
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
    height: 600px;
    border-radius: 5px;
    margin-right: 3%;
    text-align: center;
}

.person_body_list {
    width: 100%;
    height: 50px;
    margin-top: 25px;
    font-size: 22px;
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
    height: 380px;
    margin-top: 40px;
    margin-right: 30px;
}



</style>
