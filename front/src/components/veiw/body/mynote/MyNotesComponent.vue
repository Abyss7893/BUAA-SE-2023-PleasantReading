<template>
  <head-and-foot>
    <!-- <check-login></check-login> -->
    <!-- <el-space direction="vertical" alignment="start" :size="30"> -->
    <div class="box-center">
      <el-divider />
      <vue-good-table
        :columns="columns"
        :rows="rows"
        theme="black-rhino"
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
          label: "笔记内容",
          field: "text",
        },
        {
          label: "时间",
          field: "timestamp",
          type: "date",
          dateInputFormat: "yyyy-MM-dd",
          dateOutputFormat: "yyyy MM dd",
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
      } else if (params.column.label == "笔记内容") {
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
</style>