<template>
    <div>

        <body>
            <div class="changePwd">
                <div class="close-icon" @click="close"><svg class="closeicon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M851.416 217.84l-45.256-45.248L512 466.744l-294.152-294.16-45.256 45.256L466.744 512l-294.152 294.16 45.248 45.256L512 557.256l294.16 294.16 45.256-45.256L557.256 512z" fill="#272536"></path></svg></div>
                <h2>修改密码</h2>
                <div class="changePwd_box" style="margin-top: 50px;">
                    <input type="text"  v-model="form.oldPwd" name="name" id="name" required />
                    <label for="name">旧密码</label>
                </div>
                <div class="changePwd_box" style="margin-top: 120px;">
                    <input type="password" name="pwd" v-model="form.newPwd" id="pwd" required="required">
                    <label for="pwd">新密码</label>
                </div>
                <div class="changePwd_box" style="margin-top: 190px;">
                        <input type="password" name="pwd" v-model="form.confirmPwd"  id="pwd2" required="required">
                        <label for="pwd">确认密码</label>
                    </div>
                <a style="margin-top: 210px;" @click="submitForm">
                    确认修改
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </a>
            </div>

        </body>
    </div>
</template>

<script>
import axios from 'axios';
import {ElMessage } from 'element-plus';
import {reactive} from 'vue'
export default {
    name:'ChangePwd',

    emits:['close'],
    setup(_,{emit}){
        const form=reactive({
            oldPwd:'',
            newPwd:'',
            confirmPwd:''
        })
        const rules = {
            oldPwd: [
                { required: true, message: "旧密码不能为空", trigger: "blur" }
            ],
            newPwd: [
                { required: true, message: "新密码不能为空", trigger: "blur" },
                { min: 6, max: 20, message: '密码长度在 6 到 20 字符之间', trigger: 'blur' }
            ],
            confirmPwd: [
                { required: true, message: '确认密码不能为空', trigger: 'blur' },
                { validator: validateConfirmPassword, trigger: 'blur' }
            ]
        }
        function validateConfirmPassword(rule, value, callback) {
            if (value !== form.newPwd) {
                callback(new Error('两次输入密码不一致'));
            } else {
                callback();
            }
        }
        function close(){
            emit('close')
        }
        const submitForm = () => {
            if(form.newPwd!=form.confirmPwd){
                 ElMessage({
                    message: '两次输入密码不一致',
                    grouping: true,
                    type: 'error',
                })
                return;
            }
            // 创建一个对象来保存表单数据
            const data = {
                oldpwd: form.oldPwd, // TODO：请替换成真实的旧密码
                newpwd: form.newPwd
            };
            
            // 使用 Axios 发送 POST 请求
            axios.post('http://154.8.183.51/user/changepwd', data)
                .then(() => {
                     ElMessage({
                        message: '修改密码成功',
                        grouping: true,
                        type: 'success',
                    })
                    emit('close')
                })
                .catch(() => {
                    ElMessage({
                        message: '修改密码失败',
                        grouping: true,
                        type: 'error',
                    })
                });
        };

        return{
            form,
            rules,
            submitForm,
            close,
        }
    }
}
</script>

<style lang="scss" scoped>

.changePwd{

	display: flex;
	flex-direction: column;
	align-items: center;
	width: 400px;
    height: 300px;
	padding: 40px;
	background-color: rgba(236, 167, 167, 0.8);
	box-shadow: 0 15px 25px rgba(0, 0, 0, 0.4);

}

.changePwd h2{
	color: #fff;
	margin-bottom: 30px;
}
.changePwd .changePwd_box {
	/*相对定位*/
	position: absolute;
	width: 400px;
}
.changePwd .changePwd_box input{
	/*清除input框自带的边框和轮廓*/
	outline: none;
	border: none;
	width: 400px;
	padding: 10px 0;
	margin-bottom: 50px;
	color: #fff;
	font-size: 16px;
	border-bottom: 1px solid #fff;
	/*背景颜色为透明色*/
	background-color: transparent;
}

.changePwd .changePwd_box label{
	position:absolute;
	top: 0 ;
	left: 0;
	padding: 10px 0;
	color: #fff;
	pointer-events: none;
	transition: all 0.5s;
}

.changePwd .changePwd_box input:focus + label,
.changePwd  .changePwd_box input:valid + label{
	top: -20px;
	color: #03e9f4;
	font-size: 12px;
}

.changePwd a{
	/*overflow: hidden;*/
	position: relative;
    cursor:pointer;
	padding: 10px 20px;
	color: #fff;
	/*取消a表现原有的下划线*/
	text-decoration: none;
	/*同样加个过渡*/
	transition: all 0.5s;
}
.changePwd a:hover {
	color: #fff;
	border-radius: 5px;
	background-color: #f8b2b2;
	box-shadow: 0 0 5px #03e9f4,0 0 25px #03e9f4,0 0 50px #03e9f4,0 0 100px #03e9f4;
}
.changePwd a span{
	position: absolute;
}
.changePwd a span:first-child {
	top: 0;
	left: -100%;
	width: 100%;
	height: 2px;
	background: linear-gradient(to right,transparent,#03e9f4);
	animation: move1 1s linear infinite;

}
.changePwd a span:nth-child(2){
	right: 0;
	top: -100%;
	width: 2px;
	height: 100%;
	background: linear-gradient(transparent,#03e6f4);
	/*这里多了个0.25s其实是延迟时间*/
	animation: move2 1s linear 0.25s infinite;
}

.changePwd a span:nth-child(3){
	right: -100%;
	bottom: 0;
	width: 100%;
	height: 2px;
	background: linear-gradient(to left,transparent,#03e9f4);

	animation: move3 1s linear 0.5s infinite;
}

.changePwd a span:last-child{
	left: 0;
	bottom: -100%;
	width: 2px;
	height: 100%;
	background: linear-gradient(#03e9f4,transparent);
	animation: move4 1s linear 0.75s infinite;
}
/*写一下动画 */
@keyframes move1{
	0%{
		left: -100%;

	}
	50%,
	100%{
		left: 100%;
	}
}

@keyframes move2{
	0%{
		top: -100%;

	}
	50%,
	100%{
		top: 100%;
	}
}

@keyframes move3{
	0%{
		right: -100%;

	}
	50%,
	100%{
		right: 100%;
	}
}

@keyframes move4{
	0%{
		bottom: -100%;

	}
	50%,
	100%{
		bottom: 100%;
	}
}
.close-icon{
  position: absolute;
  margin-left: 235px;
  top: 20px;
  cursor: pointer;
  
}
.closeicon{
    margin-left: 180px;
  width: 20px;
transition: transform .4s ease-in-out;
}
.close-icon:hover .closeicon{
  transform: rotate(120deg);
}
</style>