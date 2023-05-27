<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="cancelSettings"><el-icon class="close-panel-button-icon" size="26"
        color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel setting">
      <h4 class="lang">设置</h4>
      <div class="setting-list">
        <ul>
          <li class="theme-list"><i>阅读主题</i><span v-for="(theme, themeId) in themes" :key="themeId"
              :style="{ background: theme.color }" :title="theme.name" @click="changeAct(theme.name)"><svg
                t="1684599952852" class="icon" viewBox="0 0 1459 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="1460" width="16" height="16">
                <path
                  d="M1439.080665 18.734797a66.336804 66.336804 0 0 0-93.766391 1.361753l-818.024224 842.341234-413.389174-425.499045a66.336804 66.336804 0 0 0-95.176778 92.404639l460.75871 474.473504a66.336804 66.336804 0 0 0 95.176778 0l865.685564-891.364327a66.28817 66.28817 0 0 0-1.361753-93.766392z"
                  p-id="1461" :fill=theme.color></path>
              </svg></span>
          </li>
          <li class="font-list"><i>正文字体</i><span :class="actFont === 'yahei' ? 'act' : ''"
              @click="setFont('yahei')">雅黑</span><span :class="actFont === 'songti' ? 'act' : ''"
              @click="setFont('songti')">宋体</span><span :class="actFont === 'kaishu' ? 'act' : ''"
              @click="setFont('kaishu')">楷书</span></li>
          <li class="size-list"><i>字体大小</i><cite><span class="sub" @click="subFontSize"><svg t="1684673318490"
                  class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3636"
                  width="20" height="20">
                  <path
                    d="M661.333333 938.666667a21.333333 21.333333 0 0 1-19.886666-13.606667L547.186667 682.666667H178.146667l-94.266667 242.4a21.333333 21.333333 0 1 1-39.76-15.466667l298.666667-768a21.333333 21.333333 0 0 1 39.76 0l298.666666 768A21.333333 21.333333 0 0 1 661.333333 938.666667zM194.74 640h335.853333L362.666667 208.193333zM960 256h-256a21.333333 21.333333 0 0 1 0-42.666667h256a21.333333 21.333333 0 0 1 0 42.666667z"
                    fill="#262626" p-id="3637"></path>
                </svg></span><b></b><span class="number">{{ this.fontSize }}</span><b></b><span class="add"
                @click="addFontSize"><svg t="1684673259505" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="2713" width="20" height="20">
                  <path
                    d="M661.333333 938.666667a21.333333 21.333333 0 0 1-19.886666-13.606667L547.186667 682.666667H178.146667l-94.266667 242.4a21.333333 21.333333 0 1 1-39.76-15.466667l298.666667-768a21.333333 21.333333 0 0 1 39.76 0l298.666666 768A21.333333 21.333333 0 0 1 661.333333 938.666667zM194.74 640h335.853333L362.666667 208.193333zM832 384a21.333333 21.333333 0 0 1-21.333333-21.333333V256h-106.666667a21.333333 21.333333 0 0 1 0-42.666667h106.666667V106.666667a21.333333 21.333333 0 0 1 42.666666 0v106.666666h106.666667a21.333333 21.333333 0 0 1 0 42.666667h-106.666667v106.666667a21.333333 21.333333 0 0 1-21.333333 21.333333z"
                    fill="#262626" p-id="2714"></path>
                </svg></span></cite></li>
          <li><i>页面宽度</i><cite><span class="sub" @click="subPageWidth"><svg t="1684678251975" class="icon"
                  viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="13102" width="20"
                  height="20">
                  <path
                    d="M213.333333 0l426.666667 0 298.666667 298.666667 0 597.333333q0 52.992-37.504 90.496t-90.496 37.504l-597.333333 0q-52.992 0-90.496-37.504t-37.504-90.496l0-768q0-52.992 37.504-90.496t90.496-37.504zM384 597.333333l256 0q17.664 0 30.165333 12.501333t12.501333 30.165333-12.501333 30.165333-30.165333 12.501333l-256 0q-17.664 0-30.165333-12.501333t-12.501333-30.165333 12.501333-30.165333 30.165333-12.501333zM554.666667 384l0-298.666667-341.333333 0q-18.005333 0-30.336 12.330667t-12.330667 30.336l0 768q0 18.005333 12.330667 30.336t30.336 12.330667l597.333333 0q18.005333 0 30.336-12.330667t12.330667-30.336l0-512-298.666667 0zM818.005333 298.666667l-178.005333-178.005333 0 178.005333 178.005333 0z"
                    fill="#262626" p-id="13103"></path>
                </svg></span><b></b><span class="number">{{ this.pageWidth }}</span><b></b><span class="add"
                @click="addPageWidth"><svg t="1684678411452" class="icon" viewBox="0 0 1024 1024" version="1.1"
                  xmlns="http://www.w3.org/2000/svg" p-id="14497" width="20" height="20">
                  <path
                    d="M213.34016 0l426.65984 0 298.65984 298.65984 0 597.34016q0 53.00224-37.49888 90.50112t-90.50112 37.49888l-597.34016 0q-53.00224 0-90.50112-37.49888t-37.49888-90.50112l0-768q0-53.00224 37.49888-90.50112t90.50112-37.49888zM512 469.34016q17.67424 0 30.16704 12.4928t12.4928 30.16704l0 85.34016 85.34016 0q17.67424 0 30.16704 12.4928t12.4928 30.16704-12.4928 30.16704-30.16704 12.4928l-85.34016 0 0 85.34016q0 17.67424-12.4928 30.16704t-30.16704 12.4928-30.16704-12.4928-12.4928-30.16704l0-85.34016-85.34016 0q-17.67424 0-30.16704-12.4928t-12.4928-30.16704 12.4928-30.16704 30.16704-12.4928l85.34016 0 0-85.34016q0-17.67424 12.4928-30.16704t30.16704-12.4928zM554.65984 384l0-298.65984-341.34016 0q-18.00192 0-30.33088 12.32896t-12.32896 30.33088l0 768q0 18.00192 12.32896 30.33088t30.33088 12.32896l597.34016 0q18.00192 0 30.33088-12.32896t12.32896-30.33088l0-512-298.65984 0zM817.99168 298.65984l-177.99168-177.99168 0 177.99168 177.99168 0z"
                    fill="#262626" p-id="14498"></path>
                </svg></span></cite></li>
        </ul>
        <div class="button">
          <a class="save-button" @click="saveSettings">保存</a>
          <a class="cancel-button" @click="cancelSettings">取消</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import 'css/reader/reader.css'
export default {
  name: "ReaderSettingsPanel",
  components: {},
  created() {
    this.themes = this.$store.state.themes
  },
  mounted() {
    this.ddList = document.querySelectorAll('.reader-menu dd')
    this.readInfo()
    this.setInfo()
  },
  computed: {
    actFont() {
      return this.fontStyle
    },

  },
  data() {
    return {
      themes: {},
      ddList: null,
      theme: null,
      fontStyle: "yahei",
      fontSize: 18,
      pageWidth: 800,

    };
  },
  watch: {
    pageWidth(newVale) {
      this.$parent.setPageWidth(newVale)
    },
  },
  methods: {
    setTheme(themeName) {
      // set class 'act'
      const spans = document.querySelectorAll('.theme-list span[title]'); // 获取所有具有title属性的span元素
      spans.forEach(span => {
        if (span.getAttribute('title') === themeName) { // 检查title属性是否等于要查找的值
          // 执行操作，例如将该元素存储在变量中或添加样式等
          span.classList.add('act')
          return
        }
      });
      let old = this.theme
      this.themes.forEach(theme => {
        if (theme.name === themeName)
          this.theme = theme
        return
      });
      // set the bcg
      let body = document.getElementsByClassName("basic-bcg")[0]
      let text = document.getElementsByClassName("text")[0]
      let chapterControl = document.getElementsByClassName("chapter-control")[0]
      let panels = document.getElementsByClassName("panel")
      body.style.backgroundImage = `url(${this.theme.bg1})`;
      text.style.backgroundImage = `url(${this.theme.bg2})`;
      chapterControl.style.backgroundImage = `url(${this.theme.bg2})`;
      for (let index = 0; index < panels.length; index++) {
        panels[index].style.backgroundColor = this.theme.color
      }
      this.ddList.forEach(dd => {
        dd.style.backgroundImage = `url(${this.theme.bg2})`;
      });
      return old
    },
    undoAct(themeName) {
      const spans = document.querySelectorAll('.theme-list span[title]'); // 获取所有具有title属性的span元素
      spans.forEach(span => {
        if (span.getAttribute('title') === themeName) { // 检查title属性是否等于要查找的值
          // 执行操作，例如将该元素存储在变量中或添加样式等
          span.classList.remove('act')
          return
        }
      });
    },
    changeAct(themeName) {
      this.undoAct(this.setTheme(themeName).name)
    },
    setFont(font) {
      this.fontStyle = font
      let centerBox = document.getElementsByClassName("center-box")[0]
      switch (font) {
        case "yahei":
          centerBox.style.fontFamily = "PingFangSC-Regular, HelveticaNeue-Light, Helvetica Neue Light, Microsoft YaHei, 'sans-serif'"
          break
        case "songti":
          centerBox.style.fontFamily = "STSong,PingFangSC-Regular,-apple-system,Simsun"
          break
        case "kaishu":
          centerBox.style.fontFamily = "STKaiti,Kaiti"
          break
        default:
          break
      }
    },
    setFontSize(size) {
      let centerBox = document.getElementsByClassName("center-box")[0]
      centerBox.style.fontSize = size + "px"
    },
    addFontSize() {
      if (this.fontSize >= 48)
        return
      this.fontSize += 2
      this.setFontSize(this.fontSize)
    },
    subFontSize() {
      if (this.fontSize <= 12)
        return
      this.fontSize -= 2
      this.setFontSize(this.fontSize)
    },
    setPageWidth(size) {
      let centerBox = document.getElementsByClassName("center-box")[0]
      centerBox.style.width = size + "px"
    },
    addPageWidth() {
      if (this.pageWidth >= 1200)
        return
      this.pageWidth += 200
      this.setPageWidth(this.pageWidth)
    },
    subPageWidth() {
      if (this.pageWidth <= 600)
        return
      this.pageWidth -= 200
      this.setPageWidth(this.pageWidth)
    },
    saveInfo() {
      this.$store.commit("setReaderSettings", [this.theme, this.fontStyle, this.fontSize, this.pageWidth])
    },
    readInfo() {
      this.theme = this.$store.state.readerSettings[0]
      this.fontStyle = this.$store.state.readerSettings[1]
      this.fontSize = this.$store.state.readerSettings[2]
      this.pageWidth = this.$store.state.readerSettings[3]
    },
    setInfo() {
      this.setTheme(this.theme.name)
      this.setFont(this.fontStyle)
      this.setFontSize(this.fontSize)
      this.setPageWidth(this.pageWidth)
    },
    saveSettings() {
      this.saveInfo()
      this.setInfo()
      this.$parent.changeVisiable("settings")
    },
    cancelSettings() {
      this.undoAct(this.theme.name)
      this.readInfo()
      this.setInfo()
      this.$parent.changeVisiable("settings")
    },
  },
}


</script>