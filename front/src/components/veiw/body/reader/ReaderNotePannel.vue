<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="closeNote"><el-icon class="close-panel-button-icon" size="26" color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel note">
      <h4 class="lang">笔记</h4>
      <div class="note-box" v-if="this.notes.length != 0">
        <ul>
          <li v-for="(note, idx) in this.notes" :key="idx">
            {{ note }}
          </li>
        </ul>
        <el-pagination small hide-on-single-page layout="prev, pager, next" :total="this.pages * 5" :page-size="5"
          @current-change="handleCurrentChange" :current-page="thisPage" class="page-control"></el-pagination>
      </div>
      <div class="null-note" v-if="this.notes.length == 0">
        <!-- <el-empty description="本章节你还没有做笔记哟~快来试试吧"></el-empty> -->
        <svg viewBox="0 0 160 160" width="200" height="200">
          <defs>
            <linearGradient x1="50%" x2="50%" y2="100%" id="van-empty-1-5">
              <stop stop-color="#F2F3F5" offset="0%"></stop>
              <stop stop-color="#DCDEE0" offset="100%"></stop>
            </linearGradient>
            <linearGradient x1="95%" y1="48%" x2="5.5%" y2="51%" id="van-empty-1-6">
              <stop stop-color="#EAEDF1" offset="0%"></stop>
              <stop stop-color="#DCDEE0" offset="100%"></stop>
            </linearGradient>
            <linearGradient y1="45%" x2="100%" y2="54%" id="van-empty-1-7">
              <stop stop-color="#EAEDF1" offset="0%"></stop>
              <stop stop-color="#DCDEE0" offset="100%"></stop>
            </linearGradient>
          </defs>
          <defs>
            <linearGradient id="van-empty-1-a" x1="64%" y1="100%" x2="64%">
              <stop stop-color="#FFF" offset="0%" stop-opacity="0.5"></stop>
              <stop stop-color="#F2F3F5" offset="100%"></stop>
            </linearGradient>
          </defs>
          <g opacity=".8">
            <path d="M36 131V53H16v20H2v58h34z" fill="url(#van-empty-1-a)"></path>
            <path d="M123 15h22v14h9v77h-31V15z" fill="url(#van-empty-1-a)"></path>
          </g>
          <defs>
            <linearGradient id="van-empty-1-b" x1="64%" y1="97%" x2="64%" y2="0%">
              <stop stop-color="#F2F3F5" offset="0%" stop-opacity="0.3"></stop>
              <stop stop-color="#F2F3F5" offset="100%"></stop>
            </linearGradient>
          </defs>
          <g opacity=".8">
            <path d="M87 6c3 0 7 3 8 6a8 8 0 1 1-1 16H80a7 7 0 0 1-8-6c0-4 3-7 6-7 0-5 4-9 9-9Z"
              fill="url(#van-empty-1-b)"></path>
            <path d="M19 23c2 0 3 1 4 3 2 0 4 2 4 4a4 4 0 0 1-4 3v1h-7v-1l-1 1c-2 0-3-2-3-4 0-1 1-3 3-3 0-2 2-4 4-4Z"
              fill="url(#van-empty-1-b)"></path>
          </g>
          <g transform="translate(36 50)" fill="none">
            <g transform="translate(8)">
              <rect fill="#EBEDF0" opacity=".6" x="38" y="13" width="36" height="53" rx="2"></rect>
              <rect fill="url(#van-empty-1-5)" width="64" height="66" rx="2"></rect>
              <rect fill="#FFF" x="6" y="6" width="52" height="55" rx="1"></rect>
              <g transform="translate(15 17)" fill="url(#van-empty-1-6)">
                <rect width="34" height="6" rx="1"></rect>
                <path d="M0 14h34v6H0z"></path>
                <rect y="28" width="34" height="6" rx="1"></rect>
              </g>
            </g>
            <rect fill="url(#van-empty-1-7)" y="61" width="88" height="28" rx="1"></rect>
            <rect fill="#F7F8FA" x="29" y="72" width="30" height="6" rx="1"></rect>
          </g>
        </svg>
        <div>本章节你还没有做笔记哟~快来试试吧</div>
      </div>
      <div class="comment-input-box">
        <textarea v-model="mynote" wrap="soft" rows="1" placeholder="做做笔记让本书充实你的灵魂吧~"></textarea><input type="button"
          value="发送" @click="submitMyNote">
      </div>
    </div>
  </div>
</template>

<script>

import { getNotes, submitNote } from "@/api/api";
import { encodeForHTML } from "@/XSS/encode"
import { ElMessage } from "element-plus";
import { mapGetters } from "vuex";
export default {
  name: "ReaderNotePanel",
  components: {},
  data() {
    return {
      notes: ["这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。这本书很好看，我看到第三章了。", "这本书很好看，我看到第三章了。", "这本书很好看，我看到第三章了。", "这本书很好看，我看到第三章了。", "这本书很好看，我看到第三章了。", "这本书很好看，我看到第三章了。",],
      thisPage: 1,
      pages: 1,
      mynote: "",
    };
  },
  computed: {
    ...mapGetters(['islogin'])
  },
  watch: {
    islogin(newVal) {
      if (newVal)
        getNotes(this.$route.params.bookid, this.$route.params.chapter, 1).then((data) => {
          if (data.status && data.status == 200) {
            this.notes = data.data.notes
            this.pages = data.data.pages
          }
          else
            console.log(data.response)
        })
      else
        this.notes = []
    }
  },
  methods: {
    handleCurrentChange(val) {
      this.thisPage = val
      getNotes(this.$route.params.bookid, this.$route.params.chapter, val).then((data) => {
        if (data.status && data.status == 200) {
          this.notes = []
          data.data.notes.forEach(note => {
            this.notes.push(encodeForHTML(note))
          });
          this.pages = parseInt(data.data.pages)
        }
        else
          console.log(data.response)
      })
    },
    submitMyNote() {
      if (this.mynote.length === 0)
        return
      else if (this.mynote.length > 300) {
        ElMessage({
          message: '笔记不可以超过300字哦，请精简一下吧~',
          grouping: true,
          type: 'warning',
        })
        return
      }
      submitNote(this.$route.params.bookid, this.$route.params.chapter, this.mynote).then((data) => {
        if (data.status && data.status == 200) {
          // alert("提交笔记成功!WAW")
          this.handleCurrentChange(1)
          this.mynote = ''
        } else if (data.response && data.response.status == 401) {
          ElMessage({
            message: '未登录不可以提交笔记哟!QAQ~',
            grouping: true,
            type: 'info',
          })

        } else {
          ElMessage({
            message: '不可预知的错误发生了!提交笔记失败!TAT~',
            grouping: true,
            type: 'error',
          })
        }
      })
    },
    closeNote() {
      this.$parent.changeVisiable("note");
    },
  },
  created() {
    getNotes(this.$route.params.bookid, this.$route.params.chapter, 1).then((data) => {
      if (data.status && data.status == 200) {
        this.notes = data.data.notes
        this.pages = data.data.pages
      }
      else
        console.log(data.response)
    })
  },
  mounted() { }
};
</script>
<style lang="scss" scoped>
.note {
  width: 600px;
  float: left;
  padding-bottom: 24px;
  padding-right: 24px;
}

.note ul {
  height: 38vh;
  overflow: auto;
}

.note ul li {
  margin-top: 16px;
  padding: 16px;
  border-radius: 10px;
  background-color: #94919120;
  width: 540px;
}


.note .comment-input-box {
  border-top: 0;
}


.page-control {
  margin: 10px 0 10px;
  float: right;
  --el-pagination-hover-color: #f03636;
  --el-pagination-bg-color: rgba(249, 240, 223, 0.543);
  --el-pagination-button-disabled-bg-color: rgba(250, 245, 235, 0.8);
}

.null-note {
  height: 30vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.null-note div {
  font-size: var(--el-font-size-base);
  color: var(--el-text-color-secondary);
}
</style>