<template>
  <div class="container body">
    <input id="check" type="checkbox" />
    <label for="check"></label>
    <div class="card">
      <!-- 卡片的正面 -->
      <div class="front">
        <el-icon :size="25" @click="close" style="margin-left: 390px;top: -10px;">
          <CloseBold />
        </el-icon>
        <h2>个人信息</h2>
        <h4>{{ user?.nickname }}</h4>
        <h4>{{ user?.email }}</h4>
        <h4>{{ user?.gender || "ta还没有填写性别哦" }}</h4>
        <h4>{{ user?.birthday || "ta还没有填写生日哦" }}</h4>
      </div>
      <!-- 卡片的反面 -->
      <div class="back">
        <el-icon :size="25" @click="close" style="margin-left: 410px;">
          <CloseBold />
        </el-icon>
        <h2>个人简介</h2>
        <h4>{{ user?.motto || "这个人很懒,什么也没留下" }}</h4>
      </div>
    </div>
  </div>
</template>

<script>
import { ElIcon } from 'element-plus';
import { ref, onBeforeMount } from 'vue'
import axios from 'axios';
export default {
  name: "MyCard",
  components: { ElIcon },
  emits: ['close'],
  props: {
    userID: {
      type: String,
      default: null
    }
  },

  setup(props, { emit }) {
    const user = ref(null)
    function close() {
      emit('close')
    }
    onBeforeMount(() => {
      console.log(props.userID)
      axios.get(`http://154.8.183.51/user/getinfo/${props.userID}`)
        .then(res => {
          user.value = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    })
    return {
      user,
      close,
    }
  }
}
</script>

<style scoped>
.body {
  margin: 0;
  display: flex;
  overflow: hidden;
  justify-content: center;
  align-items: center;
  font-family: "Montserrat", sans-serif;


}

.container {
  position: absolute;
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  perspective: 1000px;
}


.card {
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -120px -200px;
  perspective: 150rem;
  width: 400px;
  height: 240px;
  cursor: pointer;
  transition: all 500ms cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card .front,
.card .back {
  position: absolute;
  margin: auto;
  padding: 2em;
  display: flex;
  width: 100%;
  height: 100%;
  flex-direction: column;
  color: white;
  transition: 500ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.card .front h2,
.card .back h2 {
  margin: 0;
  text-transform: uppercase;
  font-size: 1.75rem;
}

.card .front h4,
.card .back h4 {
  margin: 0.5em 0 1em;
  font-size: 1rem;
}

.card .front .links,
.card .back .links {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  align-items: center;
}

.card .front a,
.card .back a {
  margin: 0.25em 0.5em;
  text-decoration: none;
  font-size: 2rem;
  color: white;
}

.card .front {
  z-index: 1;
  align-items: center;
  background-image: linear-gradient(135deg, #FFB6C1, #FFFFFF);
  box-shadow: 0 6px 16px #EE82EE, inset 0 0 15px #FFB6C1;
}

.card .back {
  align-items: center;
  background-image: linear-gradient(135deg, #FFB6C1, #FFFFFF);
  transform: rotateY(180deg);
}

#check {
  display: none;
}

#check+label {
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -120px -200px;
  z-index: 2;
  width: 400px;
  height: 240px;
  cursor: pointer;
}

#check:checked+label~.card .front {
  z-index: 0;
  box-shadow: none;
  transform: rotateY(-180deg);
}

#check:checked+label~.card .back {
  box-shadow: 0 6px 16px #EE82EE, inset 0 0 15px #FFB6C1;
  transform: rotateY(0deg);
}</style>