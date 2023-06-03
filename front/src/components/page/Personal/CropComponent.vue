<template>
  <div class="hello">
    <div class="cutimg">
      <div class="container">
        <div class="img-container">
          <img :src="tempAvatar" ref="image" alt="">
        </div>
        <p class="reload" @click="reloadAvatar">重新上传</p>
      </div>
      <div class="borderline"></div>
      <div class="preview">
        <div class="before"></div>
        <p>预览头像</p>
      </div>
    </div>
    <p>请选择图片上传：大小180 * 180像素支持JPG、PNG等格式，图片需小于2M</p>
    <div class="btnwrap">
      <el-button class="button" @click="sureSava">更新</el-button>
    </div>
  </div>
</template>
  
<script>
import Cropper from 'cropperjs'
import '../../../../node_modules/cropperjs/dist/cropper.min.css'
import axios from 'axios';
import { mapGetters } from 'vuex';
import { ElMessage } from 'element-plus';

export default {
  name: 'HelloWorld',
  data() {
    return {
      myCropper: null,
      afterImg: ''
    }
  },
  computed: {
    ...mapGetters(['tempAvatar']), // 将 tempAvatar 属性从 Vuex 模块中读取出来
    imageSrc() {
      return this.tempAvatar // 使用 test 计算属性代替直接引用 test 属性
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      this.myCropper = new Cropper(this.$refs.image, {
        viewMode: 1,
        dragMode: 'none',
        initialAspectRatio: 1,
        aspectRatio: 1,
        preview: '.before',
        background: false,
        autoCropArea: 0.6,
        zoomOnWheel: false,
      })
    },
    dataURLToBlob(dataURL) {
      const byteString = atob(dataURL.split(',')[1]);
      const ab = new ArrayBuffer(byteString.length);
      const ia = new Uint8Array(ab);

      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }

      return new Blob([ab], { type: 'image/jpeg' });
    },
    sureSava() {
      const dataURL = this.myCropper.getCroppedCanvas({
        imageSmoothingQuality: 'high'
      }).toDataURL('image/jpeg')
      const blob = this.dataURLToBlob(dataURL);
      const formData = new FormData();
      formData.append('img', blob);

      axios.post('http://154.8.183.51/user/setavatar', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(response => {
        this.$store.commit('setAvatarUrl', response.data.avatarUrl);
        ElMessage({
          message: '头像上传成功',
          grouping: true,
          type: 'success',
        })

      }).catch(error => {
        console.error(error)
      })
      this.$emit('close');

    },
    reloadAvatar() {
      this.$emit('reloadAvatar')
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.reload {
  margin-top: 16px;
  display: flex;
  justify-content: center;
  color: black;
  cursor: pointer;
  transition: .3s;
}

.container {
  display: block;
}

.reload:hover {
  color: #ff7575a9;
}

.btnwrap {
  width: 100%;
}

.button {
  margin: auto;
  margin-top: 32px;
  display: flex;
  width: 140px;
  height: 40px;
  font-size: 18px;
  line-height: 32px;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;

}

.button:hover {
  background-color: #f8b2b219;
  color: #ff7575a9;
  border-color: #ff7575a9;
}

.borderline {
  height: 200px;
  width: 2px;
  background: #e5e9ef;
  float: left;
}

.cutimg {
  /* float: left; */
  height: 240px;
  width: 600px;
  display: flex;
  justify-content: center;
}

p {
  margin-top: 16px;
  color: #99a2aa;
  /* width: 830px; */
  text-align: center;
  font: 16px/1.5 Microsoft YaHei, tahoma, "\5B8B\4F53", sans-serif;
}


.before {
  margin: 12px 36px;
  width: 160px;
  height: 160px;
  overflow: hidden;
  border-radius: 100%;
  /* 这个属性可以得到想要的效果 */
}

.preview {
  float: left;
}

.img-container {
  margin-right: 48px;
  height: 200px;
  width: 200px;
  overflow: hidden;
  /* margin: auto; */
}

.afterCropper {
  flex: 1;
  margin-left: 20px;
  border: 1px solid salmon;
  text-align: center;
}

.afterCropper img {
  width: 150px;
  margin-top: 30px;
}
</style>
