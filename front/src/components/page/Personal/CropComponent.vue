<template>
    <div class="hello">
        <p>预览</p>
        <div class="before"></div>
        <el-button style="margin: 30px auto;"  @click="sureSava">裁剪</el-button>
        <div class="container">
            <div class="img-container">
                <img :src="tempAvatar" ref="image" alt="">
            </div>
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
            console.log(this.tempAvatar)
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

        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    display: flex;
}

.before {
    width: 100px;
    height: 100px;
    overflow: hidden;
    /* 这个属性可以得到想要的效果 */
}

.img-container {
    height: 400px;
    overflow: hidden;
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
