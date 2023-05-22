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
import '../../../node_modules/cropperjs/dist/cropper.min.css'
//import axios from 'axios';
import { mapGetters } from 'vuex';
export default {
    name: 'HelloWorld',
    data() {
        return {
            myCropper: null,
            afterImg: ''
        }
    },
    computed: {
        ...mapGetters(['tempAvatar']), // 将 test 属性从 Vuex 模块中读取出来
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
        sureSava() {
            this.afterImg = this.myCropper.getCroppedCanvas({
                imageSmoothingQuality: 'high'
            }).toDataURL('image/jpeg')
            console.log("fasong")
            this.$emit('close');
            console.log("diaoyong")
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
