<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center" style="width: 1400px">
      <el-divider />
      <div v-if="!this.$store.state.isLogin">
        <el-empty
          description="未登录ovo"
          :image="require('assets/imgs/unlogin.gif')"
          image-size="200px"
        />
        <div
          style="
            margin: auto;
            width: 400px;
            margin-top: 30px;
            align-items: center;
          "
        >
          <div
            class="btn twinkle"
            @click="
              () => {
                this.$store.commit('showlogin');
              }
            "
          >
            登录
          </div>
        </div>
      </div>
      <div v-else>
        <vue-good-table
          :columns="columns"
          :rows="rows"
          theme="black-rhino"
          :pagination-options="{
            enabled: true,
            mode: 'pages',
            jumpFirstOrLast: true,
            firstLabel: '首页',
            lastLabel: '尾页',
            nextLabel: '下一页',
            prevLabel: '上一页',
            rowsPerPageLabel: '每页展示',
            pageLabel: '第',
            ofLabel: '页，共有',
          }"
          @cell-click="onCellClick"
        />
        <el-divider />
      </div>
    </div>

    <!-- </el-space> -->
  </head-and-foot>
</template>
        
<script>
import HeadAndFoot from "../../HeadAndFoot.vue";
import dayjs from "dayjs";
// import BookCard from "./BookCard.vue";
// import CheckLogin from "../../../check/checkLogin.vue";
// import { nextTick } from "vue";
import { getMyNote } from "@/api/api";
export default {
  components: { HeadAndFoot },
  data() {
    return {
      columns: [
        {
          label: "书籍",
          field: "name",
        },
        {
          label: "章节",
          field: "chaptername",
        },
        {
          label: "笔记内容",
          field: "text",
          tdClass: "note-text",
        },
        {
          label: "时间",
          field: "timestamp",
          type: "date",
          dateInputFormat: "yyyy-MM-dd",
          dateOutputFormat: "yyyy-MM-dd",
          width: "80px",
        },
      ],
      rows: [],
      mybooks: [],
      rownum: 1,
      colsize: 6,
    };
  },
  methods: {
    onCellClick(params) {
      console.log("cell clicked: ", params.column);
      if (params.column.label == "书籍") {
        this.$router.push("/book/" + params.row.bookid);
      } else if (
        params.column.label == "笔记内容" ||
        params.column.label == "章节"
      ) {
        this.$router.push(
          "/reader/" + params.row.bookid + "/" + params.row.chapter
        );
      }
    },
    onRowMouseover(padding) {
      console.log("row mouseover: ", padding);
    },
  },

  created() {
    getMyNote().then((data) => {
      console.log("note", data.data.notes);
      for (let note of data.data.notes)
        this.rows.push({
          bookid: note.bookID,
          name: note.name,
          text: note.text,
          chapter: note.chapter,
          chaptername: note.title,
          timestamp: dayjs(note.timestamp).format("YYYY-MM-DD"),
        });
    });
  },
};
</script>
        
<style lang="scss">
// 引入 css
@import url(../../../../assets/css/mybooks/mybook.css);
</style>
<style >
.vgt-table.black-rhino.bordered th {
  color: #fbfdff;
  text-shadow: 1px 1px #b25050;
  border-bottom: 1px solid #435169;
  background: linear-gradient(#de6464, #f07f7f);
}

.vgt-table.black-rhino {
  border: 1px solid #435169;
  background-color: #fff7f7;
}

.vgt-left-align span {
  cursor: pointer;
}

.note-text {
  font-family: kaiti;
  color: rgb(30, 54, 100) !important;
}

.vgt-wrap.black-rhino .vgt-wrap__footer {
  color: #dae2f0;
  border: 1px solid #435169;
  background: linear-gradient(#de6464, #f07f7f);
}

.vgt-wrap.black-rhino .vgt-wrap__footer .footer__row-count__select {
  color: rgb(106 95 95);
  background: #f4f8ff;
  border: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  padding-right: 15px;
  padding-left: 5px;
  border-radius: 3px;
}

.vgt-wrap.black-rhino .vgt-wrap__footer .footer__row-count__select option {
  background: #ffffff;
}

.vgt-wrap.black-rhino .vgt-wrap__footer .footer__row-count__label {
  color: rgb(255 255 255);
}
.btn-list {
  display: grid;
  grid-template-columns: repeat(3, 200px);
  gap: 50px;
  background: #fff;
  border-radius: 20px;
  padding: 50px;
  box-shadow: 0 0 5px 5px rgb(0 0 0 / 8%);
}
</style>
<style>
.btn {
  width: 170px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  cursor: pointer;
  user-select: none;
  letter-spacing: 1rem;
  text-indent: 1rem;
  border-radius: 20px;
  box-sizing: border-box;
}
.twinkle {
  margin: auto;
  overflow: hidden;
  position: relative;
  border: 2px solid #b36161;
  color: #b36161;
  transition: background-color 0.2s;
}

.twinkle::before {
  content: "";
  position: absolute;
  width: 50px;
  height: 200%;
  background-color: rgba(255, 255, 255, 0.6);
  transform: skew(45deg) translate3d(-200px, 0, 0);
}

.twinkle:hover {
  background-color: #bd6363;
  color: #ffffff;
}

.twinkle:hover::before {
  transition: ease-in-out 0.5s;
  transform: skew(45deg) translate3d(300px, 0, 0);
}
</style>