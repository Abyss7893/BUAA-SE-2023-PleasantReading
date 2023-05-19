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
                        <ElInput v-if="editing" v-model="info.name" style="border: none;"></ElInput>
                        <span v-else>{{ info.name }}</span>
                    </ElDescriptionsItem>
                    <ElDescriptionsItem>
                            <template #label>
                                <el-icon><Avatar /></el-icon>
                                账户名
                            </template>
                            {{ info.account }}
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
                        <ElInput v-if="editing" v-model="info.age"></ElInput>
                        <span v-else>{{ info.age }}</span>
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
                        <ElInput v-if="editing" v-model="info.signature"></ElInput>
                        <span v-else>{{ info.signature }}</span>
                    </ElDescriptionsItem>
                </div>
                
            </ElDescriptions>
        </el-card>
        <!-- <el-dialog title="重置密码" v-model="showPersonal" :before-close="handleClose" :close-on-click-modal="false"
          :close-on-press-escape="false" :append-to-body="false" style="min-width: 500px;border-radius: 25px;
          backdrop-filter: blur(5px);">
          <PersonalDialog @submit="handleSubmit" @close="handleClose" />
        </el-dialog> -->
    </div>
</template>

<script>
// import PersonalDialog from './PersonalDialog';
import { defineComponent,ref } from 'vue';
import { ElButton ,ElCard,ElDescriptions, ElDescriptionsItem,ElIcon,ElInput,ElDatePicker} from 'element-plus';
import { reactive } from 'vue';

export default defineComponent({
    name: 'InfoComponent',
    components: {
    ElButton,
    ElCard,
    ElDescriptions,
    ElDescriptionsItem,
    ElIcon,
    ElInput,
    ElDatePicker
},
    setup() {
        const info = reactive({
            account: 'binjie09',
            name: '小明',
            age: 18,
            gender: '男',
            birthday: '2005-06-29',
            email: '123456@qq.com',
            signature: '这个人很懒，什么都没留下。',
        });
        let editing =ref(false)
        let showPersonal = ref(false)
        const handleEdit = () => {
            editing.value=!editing.value
        };
        function showPersonalDialog() {
            showPersonal.value = false
        }
        function  handleClose() {
            showPersonal.value = false;
        }
        function handleSubmit() {
            showPersonal.value = false;
        }
        return {
            info, showPersonal,editing,
            handleEdit, showPersonalDialog,handleClose,handleSubmit
        };
    },
});
</script>
<style>

.el-input {
  border: none;
}
</style>