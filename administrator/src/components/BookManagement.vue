<template>
  <div class="container">
    <div class="head">
      <button class="button-big">添加书籍</button>
    </div>
    <div class="table">
      <ElTable :data="tableData">
        <ElTableColumn
          fixed
          prop="id"
          label="书籍id"
          sortable
          width="100px"
        ></ElTableColumn>
        <ElTableColumn prop="cover" label="封面" sortable width="105px">
          <template v-slot="row">
            <img
              :src="row.cover"
              style="width: 80px; height: 80px"
              alt=""
            />
          </template>
        </ElTableColumn>
        <ElTableColumn
          prop="title"
          label="作品名称"
          width="125px"
        ></ElTableColumn>
        <ElTableColumn
          prop="author"
          label="作 者"
          width="100px"
        ></ElTableColumn>
        <ElTableColumn
          prop="category"
          label="分类"
          width="110px"
        ></ElTableColumn>
        <ElTableColumn prop="status" label="状态" width="80px"></ElTableColumn>
        <ElTableColumn prop="cnt" label="字数" width="110px"></ElTableColumn>
        <ElTableColumn
          prop="favorcnt"
          label="收藏人数"
          width="110px"
        ></ElTableColumn>
        <ElTableColumn prop="vip" label="VIP书目" width="100px"></ElTableColumn>
        <ElTableColumn label="Operations">
          <div class="button">
            <div class="button1">
              <el-button>Edit</el-button>
            </div>
            <div class="button2">
              <el-button size="small">Edit</el-button>
            </div>
          </div>
          <div class="button">
            <div class="button3">
              <el-button>Edit</el-button>
            </div>
            <div class="button4">
              <el-button size="small">Edit</el-button>
            </div>
          </div>
        </ElTableColumn>
      </ElTable>
    </div>
  </div>
</template>

<script>
import { ElTable, ElTableColumn, ElButton } from "element-plus";
import { getBookDetiles, getBookList } from "@/api/api";
import { reactive } from "vue";
export default {
  setup() {
    let tableData = reactive([]);
    function getdata() {
      getBookList().then((books) => {
        // console.log(books);
        for (let bookid of books.books) {
          getBookDetiles(bookid).then((book) => {
            // console.log(book);
            tableData.push(book);
          });
        }
        console.log(tableData);
      });
    }
    getdata();
    return {
      tableData,
    };
  },
  components: { ElTable, ElTableColumn, ElButton },
};
</script>

<style  scoped>
.head {
  margin-top: 100px;
  display: flex;
  justify-content: center;
  text-align: center;
}
.head button {
  border: none;
  outline: none;
  background-color: transparent;
}
.table {
  margin-top: 50px;
  border: 1px solid #ccc;
}
.button {
  display: flex;
  justify-content: space-between;
}
.button button {
  margin-right: 0px;
  border: none;
  outline: none;
  background-color: transparent;
  text-decoration: solid;
  cursor: pointer;
  font-size: 25px;
}
.button button:hover {
  text-decoration: underline;
}
.button1 button {
  color: rgb(4, 249, 82);
}
.button2 button {
  margin-right: 10px;
  color: rgb(200, 6, 6);
}
.button3 button {
  color: rgb(70, 75, 72);
}
.button4 button {
  margin-right: 10px;
  color: rgb(120, 90, 189);
}
.button-big {
  background: linear-gradient(to right, #2ecc71, #3498db);
  border: 5px dotted #2ecc71;
  border-radius: 20px;
  color: white;
  width: 200px;
  height: 50px;
  padding: 20px 40px;
  transition: all 0.3s ease;
}

.button-big:hover {
  background: linear-gradient(to right, #3498db, #2ecc71);
  width: 250px;
  height: 60px;
  cursor: pointer;
}
</style>