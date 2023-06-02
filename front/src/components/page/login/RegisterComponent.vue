<template>
    <div id="register">
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
                    <h2>欢迎注册</h2>
                    <form class="register" action="">
                        <input v-shake type="email" v-model="userRegisterForm.email" placeholder="请输入邮箱">
                        <input v-shake type="text" v-model="userRegisterForm.username" placeholder="请输入账号">
                        <input v-shake type="password" v-model="userRegisterForm.password" placeholder="请输入密码">
                        <input v-shake type="password" v-model="userRegisterForm.confirmPassword" placeholder="请再次输入密码">
                    </form>
                    <div class="message">
                        <span v-html="error"></span>
                    </div>
                    <div id="btn">
                        <button class="loginbtn" @click="register">注册</button>
                        <router-link to="/login">
                            <button class="loginbtn">返回登录</button>
                        </router-link>
                    </div>
                </el-card>
            </div>
        </div>
    </div>
</template>

<script>
import { reactive, ref } from '@vue/runtime-core'
import axios from 'axios'
import { useRouter } from 'vue-router'
// import { useStore } from 'vuex'

export default {
    name: "RegisterComponent",
    setup() {
        const router=useRouter()
        let userRegisterForm = reactive({
            email: "",
            username: "",
            password: "",
            confirmPassword: ""
        })
        let error = ref('')

        //const router = useRouter()
        //const store = useStore()

        async function register() {
            const emailReg = /^([a-zA-Z]|[0-9])(\w|-)+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$/;
            if (!emailReg.test(userRegisterForm.email)) {
                alert('请输入正确的邮箱地址');
                return;
            }
            if (userRegisterForm.password !== userRegisterForm.confirmPassword) {
                alert('两次输入的密码不一致')
                return
            }
            if(userRegisterForm.username==''){
                alert('账号不能为空')
                return
            }
            if (userRegisterForm.password == '') {
                alert('密码不能为空')
                return
            }
            try {
                const res = await axios.post('http://154.8.183.51/user/register', userRegisterForm,
                {
                        headers: {
                            'content-type': 'application/json'
                        }
                    })
                if (res.status === 200) {
                    console.log(res.data.message)
                    if(res.data.message==='success'){
                        const isTo = confirm('注册成功!是否跳转到登录界面');
                        if (isTo) {
                            router.push('/login');
                        }
                    }
                    
                    else
                    alert("账号已存在")
                } else {
                    throw new Error('请求失败')
                }

            } catch (error) {
                alert("注册失败")
            }
            userRegisterForm.email = "";
            userRegisterForm.username = "";
            userRegisterForm.password = "";
            userRegisterForm.confirmPassword = "";
        }
        return {
            userRegisterForm,
            error, register
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
#register {
    position: relative;
    width: 100vw;
    height: 100vh;
    background-image: url(../../../assets/loginback.jpg);
    background-size: 100% 100%;
    background-color: #a7a8bd;

    #contain {
        height: 500px;
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
    justify-content: center;
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

    .register {
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