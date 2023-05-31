<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" />
  <div class="reader-menu float" :style="[{ marginLeft: menuLoc }, { top: menuTop }]">
    <dl>
      <dd :class="isCatalogAct"><a @click="changeCatalog"><svg t="1684569489333" class="icon" viewBox="0 0 1024 1024"
            version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="41510" width="16" height="16">
            <path
              d="M838.3 895.9H197.9c-53.9 0-97.7-43.8-97.7-97.7V236.7c0-53.9 43.8-97.7 97.7-97.7h640.3c53.9 0 97.7 43.8 97.7 97.7v561.4c0.1 53.9-43.7 97.8-97.6 97.8zM197.9 203.8c-18.1 0-32.9 14.8-32.9 32.9v561.4c0 18.1 14.8 32.9 32.9 32.9h640.3c18.1 0 32.9-14.8 32.9-32.9V236.7c0-18.1-14.8-32.9-32.9-32.9H197.9z"
              fill="#262626" p-id="41511"></path>
            <path
              d="M695.1 455.2H341.2c-17.9 0-32.4-14.5-32.4-32.4s14.5-32.4 32.4-32.4h353.9c17.9 0 32.4 14.5 32.4 32.4s-14.5 32.4-32.4 32.4zM695.1 578.2H341.2c-17.9 0-32.4-14.5-32.4-32.4s14.5-32.4 32.4-32.4h353.9c17.9 0 32.4 14.5 32.4 32.4s-14.5 32.4-32.4 32.4zM695.1 701.2H341.2c-17.9 0-32.4-14.5-32.4-32.4s14.5-32.4 32.4-32.4h353.9c17.9 0 32.4 14.5 32.4 32.4s-14.5 32.4-32.4 32.4zM379.1 281.1c-17.9 0-32.4-14.5-32.4-32.4V115.4c0-17.9 14.5-32.4 32.4-32.4s32.4 14.5 32.4 32.4v133.2c0 17.9-14.5 32.5-32.4 32.5zM657.1 281.1c-17.9 0-32.4-14.5-32.4-32.4V115.4c0-17.9 14.5-32.4 32.4-32.4s32.4 14.5 32.4 32.4v133.2c0 17.9-14.5 32.5-32.4 32.5z"
              fill="#262626" p-id="41512"></path>
          </svg><span>图书目录</span></a></dd>
      <dd><a @click="addToFavor"><svg t="1684569110214" class="icon" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="32295">
            <path
              d="M248.065 833C235.527 833 223 845.6 223 864.497 223 883.395 235.527 896 248.065 896h469.88C730.473 896 743 883.395 743 864.497 743 845.6 736.736 833 724.21 833H248.064zM458.906 593.553a5.182 5.182 0 0 0 7.185 0l104.312-100.427c3.36-3.229 1.066-8.9-3.593-8.9h-77.75V228.761a7.763 7.763 0 0 0-7.764-7.761h-37.599a7.761 7.761 0 0 0-7.76 7.761v255.465h-77.75c-4.658 0-6.946 5.671-3.592 8.9l104.311 100.427z"
              p-id="32296" fill="#262626"></path>
            <path
              d="M173.722 738.095V153.117c0-42.732 34.622-77.371 77.33-77.371h415.202c33.63 0 60.892 27.275 60.892 60.92v576.13c0 11.116-9.005 20.125-20.115 20.125H225.144c-19.168 0-37.592 2.245-51.422 15.523v-10.349z m700.883-538.04c-13.448 1.284-23.327 13.351-23.327 26.867V866.1c0 46.479-37.659 84.155-84.115 84.155H209.927c-19.996 0-36.205-16.217-36.205-36.222V823.75c0-21.583 17.492-39.083 39.065-39.083h494.244c39.676 0 71.837-32.176 71.837-71.87v-576.13C778.868 74.442 728.449 24 666.254 24H251.05C179.778 24 122 81.805 122 153.112v760.92c0 48.584 39.366 87.968 87.927 87.968h557.236C842.185 1002 903 941.157 903 866.1V225.81c0-15.126-12.972-27.224-28.395-25.754z"
              p-id="32297" fill="#262626"></path>
          </svg><span>加入书架</span></a></dd>
      <dd><a :href="'/book/' + this.$route.params.bookid"><svg t="1684569584776" class="icon" viewBox="0 0 1024 1024"
            version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="45631" width="16" height="16">
            <path
              d="M511.347131 65.214281c-246.678192 0-446.650643 199.972451-446.650643 446.650643s199.972451 446.650643 446.650643 446.650643 446.650643-199.972451 446.650643-446.650643S758.025323 65.214281 511.347131 65.214281zM510.744403 894.491391c-211.92262 0-383.720382-171.797761-383.720382-383.720382s171.797761-383.720382 383.720382-383.720382 383.720382 171.797761 383.720382 383.720382S722.667024 894.491391 510.744403 894.491391z"
              fill="#262626" p-id="45632"></path>
            <path
              d="M502.173191 708.726523c8.139378 8.138354 8.139378 21.332864 0 29.471219l0 0c-8.138354 8.139378-21.332864 8.139378-29.471219 0L261.234723 526.730493c-8.139378-8.138354-8.139378-21.331841 0-29.471219l0 0c8.138354-8.138354 21.332864-8.138354 29.471219 0L502.173191 708.726523 502.173191 708.726523zM290.705941 526.470573c-8.138354 8.139378-21.332864 8.139378-29.471219 0l0 0c-8.139378-8.138354-8.139378-21.331841 0-29.471219l211.467249-211.467249c8.138354-8.138354 21.332864-8.138354 29.471219 0l0 0c8.139378 8.139378 8.139378 21.332864 0 29.472242L290.705941 526.470573 290.705941 526.470573zM290.705941 526.470573M737.565339 483.569484c15.624862-0.010233 28.296463 12.648065 28.304649 28.271904l0 0c0.010233 15.623839-12.648065 28.296463-28.271904 28.304649l-405.963988 0.233314c-15.623839 0.010233-28.29544-12.647041-28.304649-28.271904l0 0c-0.00921-15.623839 12.649088-28.29544 28.271904-28.304649L737.565339 483.569484 737.565339 483.569484z"
              fill="#262626" p-id="45633"></path>
          </svg><span>返回书页</span></a></dd>
      <dd :class="isCommentsAct"><a @click="changeComments"><svg t="1684579497399" class="icon" viewBox="0 0 1024 1024"
            version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2409" width="16" height="16">
            <path
              d="M622.56056 464.834794c0 27.928073 22.73684 50.64854 50.664913 50.64854 27.956725 0 50.693566-22.720468 50.693566-50.64854 0-27.928073-22.73684-50.66389-50.693566-50.66389C645.2974 414.171927 622.56056 436.907745 622.56056 464.834794"
              fill="#262626" p-id="2410"></path>
            <path
              d="M931.254178 211.459063c0-40.637536-33.05893-73.698512-73.728188-73.698512L166.471964 137.76055c-40.637536 0-73.727165 33.059953-73.727165 73.698512l0 506.796488c0 40.637536 33.088606 73.696466 73.727165 73.696466l251.16846 0 94.343715 94.28641 94.315062-94.28641 251.226788 0c40.669258 0 73.728188-33.05893 73.728188-73.696466l0-82.560344-0.089028-1.282203L931.254178 211.459063zM875.96699 695.220928c0 22.88522-18.558681 41.444924-41.443901 41.444924L579.446623 736.665853l-67.462484 67.490114-67.430762-67.490114L189.506587 736.665853c-22.88522 0-41.4746-18.559705-41.4746-41.444924L148.031986 234.493685c0-22.88522 18.58938-41.488927 41.4746-41.488927l645.01548 0c22.88522 0 41.443901 18.603707 41.443901 41.488927l0 396.579247 0 36.161594L875.965967 695.220928z"
              fill="#262626" p-id="2411"></path>
            <path
              d="M461.321272 464.834794c0 27.928073 22.735817 50.64854 50.662867 50.64854 27.929096 0 50.66389-22.720468 50.66389-50.64854 0-27.928073-22.734794-50.66389-50.66389-50.66389C484.057089 414.171927 461.321272 436.907745 461.321272 464.834794"
              fill="#262626" p-id="2412"></path>
            <path
              d="M300.083008 464.834794c0 27.928073 22.735817 50.64854 50.66389 50.64854 27.927049 0 50.662867-22.720468 50.662867-50.64854 0-27.928073-22.735817-50.66389-50.662867-50.66389C322.817802 414.171927 300.083008 436.907745 300.083008 464.834794"
              fill="#262626" p-id="2413"></path>
          </svg><span>章节评论</span></a></dd>
      <dd :class="isNoteAct">
        <a @click="changeNote"><svg t="1685182667046" class="icon" viewBox="0 0 1024 1024" version="1.1"
            xmlns="http://www.w3.org/2000/svg" p-id="6116" width="16" height="16">
            <path
              d="M208.896 788.48l152.576-48.128c8.192-3.072 16.384-7.168 22.528-14.336l403.456-433.152c50.176-53.248 47.104-136.192-6.144-186.368-53.248-49.152-136.192-46.08-186.368 7.168L191.488 545.792c-6.144 7.168-10.24 15.36-12.288 23.552L142.336 727.04c-9.216 38.912 27.648 73.728 66.56 61.44z m423.936-640c29.696-31.744 80.896-33.792 112.64-4.096 31.744 29.696 33.792 80.896 4.096 112.64l-29.696 31.744-112.64-112.64 25.6-27.648zM229.376 581.632l343.04-367.616 112.64 112.64-338.944 363.52-152.576 48.128 35.84-156.672zM857.088 877.568H124.928c-14.336 0-25.6 11.264-25.6 25.6s11.264 25.6 25.6 25.6h732.16c14.336 0 25.6-11.264 25.6-25.6s-11.264-25.6-25.6-25.6z"
              fill="#262626" p-id="6117"></path>
          </svg><span>章节笔记</span></a>
      </dd>
      <dd :class="isSettingAct"><a @click="changeSettings"><svg t="1684569420958" class="icon" viewBox="0 0 1036 1024"
            version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="37778" width="16" height="16">
            <path
              d="M1017.6 467.2c0-19.2 0-38.4-6.4-51.2 0-25.6-12.8-44.8-38.4-51.2-38.4-6.4-70.4-25.6-96-70.4-19.2-38.4-25.6-76.8-12.8-115.2 6.4-19.2 0-38.4-12.8-64-44.8-44.8-102.4-76.8-166.4-96-19.2-6.4-38.4 0-64 12.8-25.6 32-64 44.8-108.8 44.8-38.4 0-76.8-19.2-108.8-44.8-25.6-25.6-51.2-19.2-64-12.8-44.8 32-96 57.6-153.6 102.4-25.6 12.8-32 38.4-25.6 57.6 12.8 38.4 6.4 83.2-12.8 121.6-12.8 32-44.8 57.6-89.6 70.4H44.8c-12.8 6.4-25.6 19.2-32 44.8v19.2c-6.4 25.6-12.8 51.2-12.8 70.4 0 32 0 70.4 12.8 96 0 25.6 19.2 44.8 44.8 51.2 38.4 6.4 70.4 25.6 96 70.4 19.2 38.4 25.6 76.8 12.8 115.2-6.4 19.2 0 38.4 12.8 64 38.4 38.4 89.6 70.4 166.4 102.4h12.8c12.8 0 32-6.4 44.8-19.2 25.6-32 64-44.8 108.8-44.8 38.4 0 76.8 19.2 108.8 44.8 12.8 12.8 25.6 19.2 44.8 19.2h19.2c57.6-25.6 108.8-51.2 166.4-96 19.2-12.8 32-38.4 19.2-57.6-12.8-38.4-6.4-83.2 12.8-121.6 19.2-32 51.2-57.6 96-70.4h12.8c19.2-6.4 32-25.6 38.4-44.8l6.4-19.2c-19.2-32-12.8-51.2-12.8-76.8 0-19.2-6.4-32-6.4-51.2z m-224 384c-32 32-76.8 57.6-134.4 76.8-38.4-38.4-96-64-153.6-64-57.6 0-115.2 25.6-153.6 64-51.2-19.2-96-51.2-128-76.8 19.2-57.6 12.8-115.2-19.2-160-32-57.6-70.4-89.6-128-102.4V512c0-25.6 0-51.2 6.4-83.2 57.6-19.2 96-51.2 128-96 32-57.6 38.4-115.2 19.2-160 32-32 76.8-57.6 134.4-76.8 44.8 44.8 96 70.4 153.6 70.4 57.6 0 115.2-25.6 153.6-64 51.2 19.2 96 51.2 128 76.8-19.2 57.6-12.8 115.2 19.2 160 32 57.6 70.4 89.6 128 102.4 6.4 25.6 6.4 51.2 6.4 83.2 0 19.2 0 38.4-6.4 70.4-57.6 19.2-102.4 57.6-128 102.4-32 51.2-38.4 108.8-25.6 153.6z"
              fill="#262626" p-id="37779"></path>
            <path
              d="M691.2 428.8c-12.8-6.4-19.2-6.4-32-6.4-19.2 12.8-25.6 25.6-25.6 44.8 12.8 25.6 6.4 51.2 0 76.8v6.4c-19.2 76.8-89.6 108.8-160 89.6-32-12.8-64-32-76.8-64s-19.2-64-6.4-102.4c25.6-70.4 96-102.4 160-83.2 6.4 6.4 19.2 6.4 25.6 0 12.8-6.4 19.2-12.8 25.6-19.2 6.4-6.4 6.4-19.2 0-25.6-6.4-12.8-12.8-19.2-25.6-25.6-102.4-38.4-211.2 12.8-256 121.6-12.8 51.2-12.8 102.4 12.8 153.6 25.6 44.8 64 83.2 115.2 102.4 12.8 6.4 38.4 12.8 64 12.8 83.2 0 153.6-51.2 185.6-134.4 12.8-38.4 12.8-83.2 0-128 0-12.8-6.4-19.2-6.4-19.2z"
              fill="#262626" p-id="37780"></path>
          </svg><span>设置</span></a></dd>
    </dl>
    <!-- 目录面板浮层 -->
    <ReaderCatalogPanel ref="child2" :style="{ visibility: catalogDisplay }" />
    <!-- 设置面板浮层 -->
    <ReaderSettingsPanel ref="child1" :style="{ display: settingsDisplay }" />
    <ReaderCommentsPanel ref="child3" :style="{ display: commentsDisplay }" />
    <ReaderNotePannel ref="child4" :style="{ display: noteDisplay }" />
  </div>
</template>
<script>
import 'css/reader/reader.css'
import ReaderSettingsPanel from './ReaderSettingsPanel.vue';
import ReaderCatalogPanel from './ReaderCatalogPanel.vue';
import ReaderCommentsPanel from './ReaderCommentsPanel.vue';
import ReaderNotePannel from './ReaderNotePannel.vue';
import { addBookToFavor } from "@/api/api";
import { ElMessage } from 'element-plus';
export default {
  name: "ReaderMenu",
  components: {
    ReaderSettingsPanel,
    ReaderCatalogPanel,
    ReaderCommentsPanel,
    ReaderNotePannel,
  },
  data() {
    return {
      pageWidth: 800,
      Top: null,
      settingsExist: false,
      catalogExist: false,
      commentsExist: false,
      noteExist: false,
    }
  },
  mounted() {
    window.addEventListener("scroll", this.updateTop, true);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.updateTop, true);
  },
  watch: {
    catalogExist() {
      this.$refs.child2.scrollToThisChapter()
    }
  },
  computed: {
    isSettingAct() {
      if (this.settingsExist)
        return "act"
      return null
    },
    isCatalogAct() {
      if (this.catalogExist)
        return "act"
      return null
    },
    isCommentsAct() {
      if (this.commentsExist)
        return "act"
      return null
    },
    isNoteAct() {
      if (this.noteExist)
        return "act"
      return null
    },
    settingsDisplay() {
      if (this.settingsExist)
        return "block"
      else
        return "none"
    },
    catalogDisplay() {
      if (this.catalogExist)
        return "visible"
      else
        return "hidden"
    },
    commentsDisplay() {
      if (this.commentsExist)
        return "block"
      else
        return "none"
    },
    noteDisplay() {
      if (this.noteExist)
        return "block"
      else
        return "none"
    },
    menuLoc() {
      return -(this.pageWidth / 2) - 68 + 'px'
    },
    menuTop() {
      if (this.Top < 0)
        return "0"
      else
        return this.Top + "px"
    },
  },
  methods: {
    updateTop() {
      this.Top = document.getElementsByClassName("center-box")[0].getBoundingClientRect().top;
    },
    panelInit() {
      this.settingsExist = false
      this.catalogExist = false
      this.commentsExist = false
      this.noteExist = false
    },
    changeVisiable(pannelName) {
      switch (pannelName) {
        case "settings":
          this.settingsExist = !this.settingsExist
          break
        case "catalog":
          this.catalogExist = !this.catalogExist
          break
        case "comments":
          this.commentsExist = !this.commentsExist
          break
        case "note":
          this.noteExist = !this.noteExist
          break
        default:
          break;
      }
    },
    changeSettings() {
      if (!this.settingsExist) {
        this.panelInit()
        this.changeVisiable("settings")
      } else {
        this.$refs.child1.cancelSettings()
      }
    },
    setPageWidth(width) {
      this.pageWidth = width
    },
    changeCatalog() {
      if (!this.catalogExist) {
        this.panelInit()
        this.changeVisiable("catalog")
      } else {
        this.panelInit()
      }
    },
    changeComments() {
      if (!this.commentsExist) {
        this.panelInit()
        this.changeVisiable("comments")
      } else {
        this.panelInit()
      }
    },
    changeNote() {
      if (!this.noteExist) {
        this.panelInit()
        this.changeVisiable("note")
      } else {
        this.panelInit()
      }
    },
    addToFavor() {
      addBookToFavor(this.$route.params.bookid).then((data) => {
        const code = data.request.status
        switch (code) {
          case 200:
            ElMessage({
              message: '收藏成功',
              grouping: true,
              type: 'success',
            })
            break;
          case 401:
            ElMessage({
              message: '用户未登录！或登录失效！请重新登录',
              grouping: true,
              type: 'warning',
            })
           
            this.$store.commit('refresh')
            break;
          default:
            break;
        }
      })
    },
  },
}

</script>
<style>
.lang {
  font-family: "Times New Roman", Georgia, Serif;
}
</style>
