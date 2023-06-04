<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center" style="width: 1400px">
      <el-divider />
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
      rows: [
        // { id: 1, name: "John", age: 20, createdAt: "", score: 0.03343 },
        // {
        //   id: 2,
        //   name: "Jane",
        //   age: 24,
        //   createdAt: "2011-10-31",
        //   score: 0.03343,
        // },
        // {
        //   id: 3,
        //   name: "Susan",
        //   age: 16,
        //   createdAt: "2011-10-30",
        //   score: 0.03343,
        // },
        // {
        //   id: 4,
        //   name: "Chris",
        //   age: 55,
        //   createdAt: "2011-10-11",
        //   score: 0.03343,
        // },
        // {
        //   id: 5,
        //   name: "Dan",
        //   age: 40,
        //   createdAt: "2011-10-21",
        //   score: 0.03343,
        // },
        // {
        //   id: 6,
        //   name: "John",
        //   age: 20,
        //   createdAt: "2011-10-31",
        //   score: 0.03343,
        // },
      ],
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
    // params.row - row object
    // params.column - column object
    // params.rowIndex - index of this row on the current page.
    // params.event - click event
  },

  created() {
    // for (let i = 0; i < 19; i++) {
    //   this.mybooks.push({
    //     img: require("../../../../assets/imgs/bookcv.png"),
    //     name: "book.name",
    //     title: "book.title",
    //     bookID: 1,
    //     chapter: 1,
    //   });
    // }
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
</style>