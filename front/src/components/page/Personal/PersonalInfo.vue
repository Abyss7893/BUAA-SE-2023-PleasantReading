<template>
  <div class="infocard">
    <div class="imgBx">
      <img :src="img">
    </div>
    <div class="content">
      <div class="details">
        <h2>{{ user?.nickname }}<br><span>{{ user?.motto || "这个人很懒,什么也没留下" }}</span></h2>
        <div class="brief">
          <span>{{ user?.gender || "ta还没有填写性别哦" }}</span>
          <span>{{ user?.birthday || "ta还没有填写生日哦" }}</span>
        </div>
        <div class="data">
          <h3>342<br><span>收藏</span></h3>
          <h3>120k<br><span>笔记</span></h3>
          <h3>285<br><span>书签</span></h3>
        </div>
        <div class="actionBtn">
          <button>Follow</button>
          <button>Message</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onBeforeMount, onMounted } from 'vue'
import axios from 'axios';
export default {
  name: "PersonalInfo",
  components: {},
  props: {
    userID: {
      type: String,
      default: null
    },
    userImg: {
      type: String,
      default: ""
    }
  },
  setup(props) {
    const img = ref("")
    const user = ref(null)
    onBeforeMount(() => {
      axios.get(`http://154.8.183.51/user/getinfo/${props.userID}`)
        .then(res => {
          user.value = res.data
        })
        .catch(err => {
          console.log(err)
        })
    })
    onMounted(() => {
      img.value = new URL(props.userImg, import.meta.url).href
    })
    return {
      user,
      img,
    }
  }
};
</script>
<style lang="scss" scoped>
/* 这是引入了一些字体 */
@import url('https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}

.brief {
  font-size: 0.8em;
  font-weight: 500;
  opacity: 0.9;
}

.brief span {
  display: block;
  margin: 4px 0;
}

.infocard {
  position: relative;
  width: 350px;
  height: 250px;
  /* height: 450px; */
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 35px 80px rgba(0, 0, 0, 0.15);
  transition: 0.5s;
}

.infocard:hover {
  height: 510px;
}

.imgBx {
  position: absolute;
  left: 50%;
  top: -50px;
  transform: translateX(-50%);
  width: 150px;
  height: 150px;
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.35);
  overflow: hidden;
  transition: 0.5s;
}

.infocard:hover .imgBx {
  width: 250px;
  height: 250px;
}

.imgBx img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.infocard .content {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  overflow: hidden;
}

.infocard .content .details {
  padding: 40px;
  text-align: center;
  width: 100%;
  transition: 0.5s;
  transform: translateY(150px);
}

.infocard:hover .content .details {
  transform: translateY(0px);
}

.infocard .content .details h2 {
  font-size: 1.25em;
  font-weight: 600;
  color: #555;
  line-height: 1.2em;
  // display: inline-block;
  white-space: nowrap;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
}

.infocard .content .details h2 span {
  font-size: 0.75em;
  font-weight: 500;
  opacity: 0.5;
}

.infocard .content .details .data {
  display: flex;
  justify-content: space-between;
  margin: 20px 0;
}

.infocard .content .details .data h3 {
  font-size: 1em;
  color: #555;
  line-height: 1.2em;
  font-weight: 600;
}

.infocard .content .details .data h3 span {
  font-size: 0.85em;
  font-weight: 400;
  opacity: 0.5;
}

.infocard .content .details .actionBtn {
  display: flex;
  justify-content: space-between;
}

.infocard .content .details .actionBtn button {
  padding: 10px 30px;
  border-radius: 5px;
  border: none;
  outline: none;
  font-size: 1em;
  font-weight: 500;
  background: #ff5f95;
  color: #fff;
  cursor: pointer;
}

.infocard .content .details .actionBtn button:nth-child(2) {
  border: 1px solid #999;
  color: #999;
  background: #fff;
}
</style>