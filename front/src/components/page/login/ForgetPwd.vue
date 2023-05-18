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
        <el-form-item label="邮箱" prop="email">
          <el-input v-model.trim="formData.email" />
        </el-form-item>
        <el-form-item label="新密码" prop="password">
          <el-input type="password" v-model.trim="formData.password" />
        </el-form-item>
        <el-form-item label="确认密码" prop="confirmPassword">
          <el-input type="password" v-model.trim="formData.confirmPassword" />
        </el-form-item>
        <el-form-item label="验证码" required>
          <el-input v-model.trim="verificationCode" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm" :loading="submitting">提交</el-button>
          <el-button @click="resetForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { ElForm, ElFormItem, ElInput, ElButton } from 'element-plus';
import '../../../../node_modules/element-plus/theme-chalk/index.css';

export default {
  components: {
    ElForm,
    ElFormItem,
    ElInput,
    ElButton,
  },
  emits: ['submit'],
  setup(_, { emit }) {
    const formData = ref({
      email: '',
      password: '',
      confirmPassword: '',
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

    const verificationCode = ref('');

    // 提交表单
    const submitting = ref(false);
    function submitForm() {
      formData.value.verificationCode = verificationCode.value;
      submitting.value = true;
      // TODO: 校验验证码、发送修改密码请求等操作
      setTimeout(() => {
        submitting.value = false;
        emit('submit', formData.value);
      }, 1000);
    }

    // 重置表单
    function resetForm() {
      verificationCode.value = '';
      formData.value = {
        email: '',
        password: '',
        confirmPassword: ''
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
      verificationCode,
      submitting,
      submitForm,
      resetForm,
    };
  },
};
</script>

<style>

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
/* .bubble::before {
    content: "";
    position: absolute;
    display: block;
    top: 100%; 
    left: 0;
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-top: 10px solid #877f7f; 
} */

</style>