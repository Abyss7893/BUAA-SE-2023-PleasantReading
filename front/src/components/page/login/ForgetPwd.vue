<template>
  <div class="container">
    <!-- 展示别的内容 -->
    <div class="image">
      <img src="../../../assets/girl.png">
    </div>
    <div class="bubble">
      <p>下次不要忘记密码噢QAQ</p>
   </div>
    <div class="form-container">
      <el-form ref="form" :model="formData" :rules="rules" label-width="100px">
        <el-form-item label="邮箱" prop="email" >
            <el-input  v-model.trim="formData.email" />
          </el-form-item>
        <el-form-item label="账号" prop="username" >
            <el-input  v-model.trim="formData.username" />
          </el-form-item>
        <el-form-item label="新密码" prop="password">
          <el-input type="password" v-model.trim="formData.password" />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input type="password" v-model.trim="formData.confirmPassword" />
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm" :loading="submitting">提交</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
      <div class="loader"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import { ElForm, ElFormItem, ElInput, ElButton ,ElMessage} from 'element-plus';
import '../../../../node_modules/element-plus/theme-chalk/index.css';
//import axios from 'axios';

export default {
  components: {
    ElForm,
    ElFormItem,
    ElInput,
    ElButton,
  },
  emits: ['submit'],
  setup(_, { emit }) {

    let waitCheck=ref(false)
    const formData = ref({
      email: '',
      password: '',
      confirmPassword: '',
      username:''
    });
    const rules = {
      email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
        { type: 'email', message: '请输入正确的邮箱', trigger: ['blur', 'change'] },
      ],
      password: [
        { required: true, message: '请输入新密码', trigger: 'blur' },
        { min: 6, max: 20, message: '密码长度在 6 到 20 个字符之间', trigger: 'blur' },
      ],
      confirmPassword: [
        { required: true, message: '请输入确认密码', trigger: 'blur' },
        { validator: validateConfirmPassword, trigger: 'blur' }
      ],
      username: [
        { required: true, message: '请输入账号', trigger: 'blur' }
      ]
    };

    // 确认密码校验方法
    function validateConfirmPassword(rule, value, callback) {
      if (value !== formData.value.password) {
        callback(new Error('两次输入密码不一致'));
      } else {
        callback();
      }
    }
    // 提交表单
    
    function submitForm() {
      const data = {
        email: formData.value.email,
        id: formData.value.username,
        pwd: formData.value.password,
      };
      const loader = document.querySelector('.loader');
      loader.classList.add('visible'); // 显示加载器
      const intervalId = setInterval(() => {
        console.log('1');
      }, 1000);
      axios.post('http://154.8.183.51/user/sendemail', data)
        .then(response => {
          console.log(response.data);

          ElMessage({
            message: '邮箱验证码已发送,请查收',
            grouping: true,
            type: 'success',
          })
         
          emit('submit')
          // 处理响应数据
        })
        .catch(error => {
          if(error.response.data.error=='not match'){
            ElMessage({
              message: '用户名与邮箱不匹配',
              grouping: true,
              type: 'error',
            })
          }
          else{
            ElMessage({
              message: '已超时,请重新处理',
              grouping: true,
              type: 'warning',
            })
          }
          // 处理错误
        })
        .finally(() => {
          clearInterval(intervalId);
          waitCheck.value = false;
          loader.classList.remove('visible'); // 隐藏加载器
        });
      
      
    }

    // 重置表单
    function resetForm() {
      waitCheck.value=false;
      formData.value = {
        email: '',
        password: '',
        confirmPassword: '',
        username:''
      };
      document.querySelectorAll('.el-form-item.is-error').forEach((item) => {
        item.classList.remove('is-error');
      });
      document.querySelectorAll('.el-form-item__error').forEach((item) => {
        item.style.display = 'none';
      });
    }
   

    return {
      formData,
      rules,
      waitCheck,
      
      submitForm,
      resetForm
    };
  },
};
</script>

<style>
.loader {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 2s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.loader.visible {
  display: block;
}
.loader:not(.visible) {
  display: none;
}

.container {
  display: flex;
  align-items: center;
  /* 垂直居中 */
}
.image{
  width: 30%;
  display: inline-flex;
}
.image img {
  border-radius: 10px;
  width: 100%;
  /* 设置图片宽度为容器的宽度 */
  height: auto;
  /* 设置图片高度为 300 像素 */
  object-fit: cover;
  /* 调整显示方式为填充容器 */
  opacity: 1;
}

.form-container {
  width: 55%;
  /* 填满剩余空间 */
}
.bubble {
    position: relative;
    border-radius: 20px;
    background-color:lightgray;
    color: black;
   
    font-size: 1em;
    margin-bottom: auto;
    padding: 20px 20px;
    /* bottom: 100px; */
    width: 15%;
    height: auto;
}

.bubble::after {
    content: "";
    position: absolute;
    display: block;
    bottom: 0px; 
    left: 0px;
    width: 0;
    height: 0;
    border-bottom: 20px solid lightgray; 
    border-right: 20px solid transparent;
}


</style>