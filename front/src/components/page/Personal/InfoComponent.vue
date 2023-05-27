<template>
    <div class="profile">
        <el-card shadow="hover">
            <ElDescriptions class="margin-top" title="简介" :column="1" border>
                <template #extra>
                    <el-button v-if="!editing" type="primary"  size="large" @click="handleEdit">修改个人信息</el-button>
                    <el-button v-else type="primary"  size="large" @click="handleEdit">提交修改</el-button>
                </template>
                <div>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon :style="iconStyle">
                                <user />
                            </el-icon>
                            昵称
                        </template>
                        <ElInput v-if="editing" v-model="info.nickname" style="border: none;"></ElInput>
                        <span v-else>{{ info.nickname }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                            <template #label>
                                <el-icon><Avatar /></el-icon>
                                账户名
                            </template>
                            {{ info.username }}
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                            <template #label>
                                <el-icon v-if="info.gen
                                    === '男'"><Male /></el-icon>
                                <el-icon v-else><Female /></el-icon>
                                性别
                             </template>
                            <ElInput v-if="editing" v-model="info.gender"></ElInput>
                            <span v-else>{{ info.gender }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Clock /></el-icon>
                            年龄
                        </template>
                        <span >{{ age }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Message /></el-icon>
                            邮箱
                        </template>
                        {{ info.email }}
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                        <template #label>
                            <el-icon><Timer /></el-icon>
                            生日
                        </template>
                        <el-date-picker v-if="editing" v-model="info.birthday" type="date" placeholder="请选择生日" :picker-options="pickerOptions"></el-date-picker>
                        <span v-else>{{ info.birthday }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem style="font-size: 16px;">
                        <template #label>
                            <el-icon><ChatDotSquare /></el-icon>
                            个人简介
                        </template>
                        <ElInput v-if="editing" v-model="info.motto"></ElInput>
                        <span v-else>{{ info.motto }}</span>
                    </ElDescriptionsItem>
                </div>
                
            </ElDescriptions>
        </el-card>
    </div>
</template>

<script>
// import PersonalDialog from './PersonalDialog';
import { defineComponent ,ref,computed} from 'vue';
import { ElButton ,ElCard,ElDescriptions, ElDescriptionsItem,ElIcon,ElInput,ElDatePicker,ElMessageBox} from 'element-plus';
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
        const handleEdit = () => {
            editing.value=!editing.value;
            if (editing.value) {
                // 编辑状态下不执行保存操作
                return;
            }
            store.commit('updateUserInfo',state.info)
            // TODO: 接下来需要做的是把修改的值传回数据库中
            axios({
                method: 'post',
                url: 'http://154.8.183.51/user/changeinfo',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(store.state.userInfo)
            })
                .then(() => {
                    ElMessageBox.alert('修改成功', '提示', {
                        confirmButtonText: '确定',
                        type: 'success',
                    });
                })
                .catch(() => {
                    alert("修改失败");

                });

        };
        return {
            ...state, editing,age,
            handleEdit
        };
    },
});
</script>
<style scoped>

.el-input {
  border: none;
}
</style>