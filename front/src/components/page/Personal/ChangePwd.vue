<template>
    <div>
        <ElForm :model="form" :rules="rules">
            <ElFormItem label="旧密码&nbsp&nbsp&nbsp" prop="oldPwd">
                    <ElInput v-model="form.oldPwd" type="password"
            placeholder="请输入旧密码"
            show-password ></ElInput>
                </ElFormItem>
            <ElFormItem label="新密码&nbsp&nbsp&nbsp" prop="newPwd">
                <ElInput v-model="form.newPwd" type="password"
        placeholder="请输入新密码"
        show-password ></ElInput>
            </ElFormItem>
            <ElFormItem label="确认密码" prop="confirmPwd">
                <ElInput v-model="form.confirmPwd" type="password"
        placeholder="请再次输入密码以确认"
        show-password ></ElInput>
            </ElFormItem>
            
        </ElForm>
        <div class="button">
            <ElButton @click="submitForm">确认修改</ElButton>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios';
import { ElButton, ElForm, ElFormItem, ElInput,ElMessage } from 'element-plus';
import {reactive} from 'vue'
export default {
    name:'ChangePwd',
    components: { ElForm, ElFormItem, ElInput, ElButton },
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
            submitForm
        }
    }
}
</script>

<style lang="scss" scoped>
.button{
    display: flex;
    justify-content: flex-end;
}
</style>