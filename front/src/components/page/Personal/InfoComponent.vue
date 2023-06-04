<template>
    <div class="profile">
        <el-card shadow="hover">
            <ElDescriptions class="mycontext" title="简介" :column="1" border>
                <template #extra>
                    <el-button v-if="!editing" type="primary"  size="large" @click="handleEdit" class="pink-button">修改个人信息</el-button>
                    <div v-else>
                        <el-button type="primary" class="pink-button"  size="large" @click="handleEdit">提交修改</el-button>
                        <el-button  type="primary" class="pink-button"  size="large" @click="cancleEdit">取消</el-button>
                    </div>
                    
                </template>
                <div>
                    <ElDescriptionsItem  width="40px" >
                        <template #label>
                            <el-icon :style="iconStyle">
                                <user />
                            </el-icon>
                            昵称
                        </template>
                        <ElInput v-if="editing" v-model="tempInfo.nickname" style="border: none; height: 45px;" ></ElInput>
                        <span v-else class="item">{{ info.nickname }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                            <template #label>
                                <el-icon><Avatar /></el-icon>
                                账户名
                            </template>
                            <span class="item">{{ info.username }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem >
                            <template #label >
                                <el-icon v-if="info.gender
                                    === '男'"><Male /></el-icon>
                                <el-icon v-else-if="info.gender === '保密'"><Lock /></el-icon>
                                <el-icon v-else><Female /></el-icon>
                                  
                                   
                                性别
                             </template>
                            <el-radio-group v-if="editing" v-model="tempInfo.gender" style="height: 45px;">
                                <el-radio :label="'男'">男</el-radio>
                                <el-radio :label="'女'">女</el-radio>
                                <el-radio :label="'保密'">保密</el-radio>
                            </el-radio-group>
                            <!-- <ElInput v-if="editing" v-model="tempInfo.gender" style="height: 45px;"></ElInput> -->
                            <span v-else class="item">{{ info.gender }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Clock /></el-icon>
                            年龄
                        </template>
                        <span class="item">{{ age }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Message /></el-icon>
                            邮箱
                        </template>
                        <span  class="item"> {{ info.email }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Timer /></el-icon>
                            生日
                        </template>
                        <el-date-picker v-if="editing" v-model="tempInfo.birthday" type="date" placeholder="请选择生日" :picker-options="pickerOptions"></el-date-picker>
                        <span v-else  class="item">{{ info.birthday }}</span>
                    </ElDescriptionsItem>          
                    <ElDescriptionsItem class="motto" style="font-size: 16px;">
                        <template #label>
                            <el-icon><ChatDotSquare /></el-icon>
                            个人简介
                        </template>
                        <ElInput type="textarea" maxlength="27" show-word-limit autosize="true" resize="none" v-if="editing" v-model="tempInfo.motto"></ElInput>
                        <span v-else style="line-height: 50px;">{{ info.motto }}</span>
                    </ElDescriptionsItem>
                </div>
                
            </ElDescriptions>
        </el-card>
    </div>
</template>
<script>
// import PersonalDialog from './PersonalDialog';
import { defineComponent ,ref,computed} from 'vue';
import { ElButton ,ElCard,ElDescriptions, ElDescriptionsItem,ElIcon,ElInput,ElDatePicker,ElMessage} from 'element-plus';
import { reactive } from 'vue';
import { useStore} from 'vuex';
import axios from 'axios';
export default defineComponent({
    name: 'InfoComponent',
    components: {
    ElButton,
    ElCard,
    ElDescriptions,
    ElDescriptionsItem,
    ElIcon,
    ElInput,
    ElDatePicker,

},
    setup() {
        const store=useStore()
        const state = reactive({
            info:null,
        });
        state.info = store.state.userInfo;
        const tempInfo=reactive({
            nickname:state.info.nickname,
            gender:state.info.gender,
            birthday:state.info.birthday,
            motto:state.info.motto
        })
        
        let editing=ref(false);

        // 计算属性：根据生日计算年龄
        const age = computed(() => {
            return computeAge(state.info.birthday);
        });

        // 计算年龄的函数
        function computeAge(birthday) {
            const birthDate = new Date(birthday);
            const currentDate = new Date();
            state.info.birthday= birthDate.toLocaleDateString('zh-CN').replace(/\//g, '-');

            let age = currentDate.getFullYear() - birthDate.getFullYear();
            const monthDiff = currentDate.getMonth() - birthDate.getMonth();
            if (monthDiff < 0 || (monthDiff === 0 && currentDate.getDate() < birthDate.getDate())) {
                age--;
            }
            return age;
        }
        function cancleEdit(){
            editing.value=false;
            tempInfo.nickname = state.info.nickname
            tempInfo.gender = state.info.gender
            tempInfo.birthday = state.info.birthday
            tempInfo.motto = state.info.motto
        }
        const handleEdit = () => {
            if(editing.value==true&& tempInfo.motto.length>27){
                ElMessage({
                    message: '因为个人简介超过最大字数限制，修改失败',
                    grouping: true,
                    type: 'error',
                })
                return;
            }
            
            if (!editing.value) {
                // 编辑状态下不执行保存操作
                editing.value = !editing.value;
                return;
            }
            
            // TODO: 接下来需要做的是把修改的值传回数据库中
            const birthDate = new Date(tempInfo.birthday);
            tempInfo.birthday = birthDate.toLocaleDateString('zh-CN').replace(/\//g, '-');
            
            axios({
                method: 'post',
                url: 'http://154.8.183.51/user/changeinfo',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(tempInfo)
            })
                .then(() => {
                    state.info.nickname=tempInfo.nickname
                    state.info.motto = tempInfo.motto
                    state.info.birthday = tempInfo.birthday
                    state.info.gender = tempInfo.gender
                    store.commit('updateUserInfo', state.info)
                 
                    ElMessage({
                        message: '修改成功',
                        grouping: true,
                        type: 'success',
                    })
                    editing.value = !editing.value;
                })
                .catch(() => {
                    
                    tempInfo.nickname= state.info.nickname
                    tempInfo.gender= state.info.gender
                    tempInfo.birthday= state.info.birthday
                    tempInfo.motto= state.info.motto
                    ElMessage({
                        message: '修改失败',
                        grouping: true,
                        type: 'error',
                    })
                    editing.value = !editing.value;
                });

        };
        return {
            tempInfo,
            ...state, editing,age,
            handleEdit,
            cancleEdit
        };
    },
});
</script>
<style scoped>
.clamp{
    overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 最多显示两行内容 */
  line-height: 25px;
  -webkit-box-orient: vertical;
   overflow-y: auto; /* 自动添加滚动条 */
}
.item{
   line-height: 36px;
}
.mycontext{
height: 480px;
}
.pink-button {
  font-weight: bold;
  background-color: #ffafc9; /* 设置按钮默认背景色为白粉色 */
  color: #fff; /* 设置文字颜色为白色 */
  padding: 10px 20px; /* 设置按钮内边距 */
  border-radius: 4px; /* 设置按钮圆角 */
  border: none; /* 去掉按钮边框 */
}

/* 使用 hover 伪类实现鼠标悬浮时改变背景色的效果 */
/* 当鼠标悬浮时，将背景色改为红粉色 */
.pink-button:hover {
  background-color: #ff5e7d; /* 设置鼠标悬浮时的背景色为红粉色 */
}
.el-input {
  border: none;
}
</style>