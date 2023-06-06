<template>
  <div>
    <ElForm>
      <ElFormItem label="昵称">
        <ElInput v-model="form.name"></ElInput>
      </ElFormItem>
      <ElFormItem label="性别">
        <ElInput v-model="form.gender"></ElInput>
      </ElFormItem>
      <ElFormItem label="年龄">
        <ElInput v-model="form.age"></ElInput>
      </ElFormItem>
      <ElFormItem label="生日">
        <ElInput v-model="form.birthday"></ElInput>
      </ElFormItem>
      <ElFormItem label="个人简介">
        <ElInput v-model="form.signature"></ElInput>
      </ElFormItem>
    </ElForm>
    <el-button @click="handleClose">取 消</el-button>
    <el-button type="primary" @click="submitForm">提 交</el-button>
  </div>
</template>

<script>
import { ElForm, ElFormItem, ElInput } from "element-plus";
import { reactive } from "vue";

export default {
  components: {
    ElForm,
    ElFormItem,
    ElInput,
  },
  emits: ["submit", "close"],
  setup(props, { emit }) {
    const form = reactive({
      account: "",
      name: "",
      age: null,
      gender: "",
      birthday: "",
      email: "",
      signature: "",
    });

    const handleClose = () => {
      emit("close");
    };

    const submitForm = () => {
      emit("submit");
    };

    return {
      form,
      handleClose,
      submitForm,
    };
  },
};
</script>

<style >
.el-descriptions__label.el-descriptions__cell.is-bordered-label {
  font-weight: 700;
  color: var(--el-text-color-regular);
  background: #fff1f5 !important;
}
</style>