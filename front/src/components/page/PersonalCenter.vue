<template>
    <div class="contain">
        <ElDialog v-model="showPayDialog" title="支付"
        width="30%">
                <PayComponent/>
            </ElDialog>
        <HeadTop />
        
        <div class="PersonTop">
            <div class="PersonTop_image">
                <ElAvatar
                    src="https://rss.sfacg.com/web/account/images/avatars/app/2010/25/1c44687f-df90-432e-8d35-cf2f46d1665b.jpg"
                    :size="170" fit="contain"></ElAvatar>
            </div>
            <div class="PersonTop_text">
                <div class="user_text">

                    <div class="imageVIP" v-if="VIP">
                        <ElAvatar
                        src="https://pic.ntimg.cn/file/20190602/29233777_112131974087_2.jpg" :size="45" fit="contain" ></ElAvatar>
                        
                    </div>
                    <div class="user_qianming">
                        <span> {{ design }}</span>
                    </div>
                    <div class="user_anniu">
                        <el-button class="el-icon-edit">上传头像</el-button>
                    </div>
                </div>
            </div>
            <div class="PersonTop_right">
                <el-button  icon="star" @click="openPayDia()">充值会员</el-button>
                <el-button  icon="star" >修改密码</el-button>
                <el-button  icon="switchButton" @click="signOut">退出登录</el-button>
            </div>
        </div>
        <div class="person_body">
            <div class="person_body_left">
                <el-card class="box-card" :body-style="{ padding: '0px' }">
                    <div class="clearfix">
                        <span class="person_body_list" style="border-bottom: none">个人中心</span>
                    </div>
                    <el-menu router active-text-color="#00c3ff" class="el-menu-vertical-demo">
                        <el-menu-item  @click="$router.push({ name: 'info' })">
                            <el-icon>
                                <User />
                            </el-icon>
                            <span>个人简介</span>
                        </el-menu-item>
                        <el-menu-item>
                            <el-icon>
                                <ChatLineSquare />
                            </el-icon>
                            <span>我的评论</span>
                        </el-menu-item>
                        <el-menu-item>
                            <el-icon>
                                <Notebook />
                            </el-icon>
                            <span>我的笔记</span>
                        </el-menu-item>
                        <el-menu-item>
                            <el-icon>
                                <Flag />
                            </el-icon>
                            <span>我的书签</span>
                        </el-menu-item>
                        <el-menu-item>
                            <el-icon>
                                <Reading />
                            </el-icon>
                            <span>我的书架</span>
                        </el-menu-item>
                        <el-menu-item>
                            <el-icon>
                                <Back />
                            </el-icon>
                            <span>返回主界面</span>
                        </el-menu-item>
                    </el-menu>
                </el-card>
            </div>
            <div class="person_body_right">
                <router-view></router-view>
            </div>
        </div>

    </div>
</template>

<script>

//import PersonalDia from "./PersonalDialog.vue";
import { ElAvatar, ElButton, ElDialog } from 'element-plus';
import HeadTop from '../veiw/head/HeadTop';

import { ref,computed } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router';
import PayComponent from './PayComponent.vue';
export default {

   name: "PersonalCenter",
    inject: ["reload"],
    components: { ElAvatar, HeadTop, ElButton,  ElDialog,PayComponent},
    setup() {
        const store=useStore();
        const router=useRouter();
        const nickname = ref("cyx");
        const design = ref("");
        const showPayDialog =ref(false);
        const isfollow = ref(true);
        const followData = ref({
            fanId: "",
            followId: "",
        });
        const isfollowid = ref([]);
        const VIP = computed(() => {
            return store.state.isVip;
        });
        function signOut() {
            store.commit('signOut');
            router.push('/');
        }
        function openPayDia(){
            showPayDialog.value=true;
            console.log("什么情况",showPayDialog.value);
        }
        return {
            nickname,
            design,
            isfollow,
            followData,
            isfollowid,
            VIP,
            showPayDialog,
            signOut,
            openPayDia
        }
    }
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
}

.PersonTop_right .el-button {
    margin-top: 30px;
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
    margin-left: 10px;
    font-weight: bold;
}
.user_anniu{
    margin-top: 140px;
    margin-right: 10px;
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