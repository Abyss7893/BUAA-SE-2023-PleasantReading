<template>
  <div class="container">
    <div class="head">
      <button class="button-big" @click="showAdd=true">添加书籍</button>
    </div>
    <!--添加图书的弹窗-->
    <ElDialog v-model="showAdd" :destroy-on-close="true">
      <ElDescriptions border :column="1">
          <ElDescriptionsItem label="图书名称"><ElInput v-model="newBook.title"></ElInput></ElDescriptionsItem>
          <ElDescriptionsItem label="图书作者"><ElInput v-model="newBook.author"></ElInput></ElDescriptionsItem>
          <ElDescriptionsItem label="VIP"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"  v-model="newBook.vip" active-text="true" inactive-text="false" /></ElDescriptionsItem>
          <ElDescriptionsItem  label="图书状态"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="newBook.status" active-text="完结" inactive-text="连载" active-value="完结" inactive-value="连载"/></ElDescriptionsItem>
          <ElDescriptionsItem label="图书简介"><ElInput type="textarea" rows="10" v-model="newBook.brief"></ElInput></ElDescriptionsItem>
          <ElDescriptionsItem label="图书分类"><ElInput v-model="newBook.category"></ElInput></ElDescriptionsItem>
          <ElDescriptionsItem label="是否上架"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="newBook.onshelf" active-text="true" inactive-text="false" /></ElDescriptionsItem>
        </ElDescriptions>
        <ElButton style="margin-left: 550px; margin-top: 50px;" @click="addBook">确认提交</ElButton>
    </ElDialog>
    <!-- 修改图书信息的弹窗 -->
    <ElDialog v-model="showInfo" :destroy-on-close="true">
      <ElDescriptions border :column="1">
        <ElDescriptionsItem label="图书名称"><span>{{ selectRow.title }}</span></ElDescriptionsItem>
        <ElDescriptionsItem label="VIP"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="selectRow.vip" active-text="true" inactive-text="false" /></ElDescriptionsItem>
        <ElDescriptionsItem  label="图书状态"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="selectRow.status" active-text="完结" inactive-text="连载" active-value="完结" inactive-value="连载"/></ElDescriptionsItem>
        <ElDescriptionsItem label="图书简介"><ElInput type="textarea" rows="10" v-model="selectRow.brief"></ElInput></ElDescriptionsItem>
        <ElDescriptionsItem label="图书分类"><ElInput v-model="selectRow.category"></ElInput></ElDescriptionsItem>
        <ElDescriptionsItem label="是否上架"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="selectRow.onshelf" active-text="true" inactive-text="false" /></ElDescriptionsItem>
      </ElDescriptions>
      <ElButton style="margin-left: 550px; margin-top: 50px;" @click="InfoSubmit">确认提交</ElButton>
    </ElDialog>
    <!-- 修改图书内容的弹窗 -->
    <ElDialog v-model="showBook" :destroy-on-close="true">
      <ElDescriptions border :column="1">
        <ElDescriptionsItem label="图书id"><span>{{ selectRow.id }}</span></ElDescriptionsItem>
        <ElDescriptionsItem label="图书章节"><ElInput v-model="selectRow.chapter"></ElInput> </ElDescriptionsItem>
        <ElDescriptionsItem label="图书内容"><ElInput type="textarea" rows="10" v-model="selectRow.context"> </ElInput></ElDescriptionsItem>
        <ElDescriptionsItem label="图书标题"><ElInput v-model="selectRow.title"></ElInput></ElDescriptionsItem>
      </ElDescriptions>
      <ElButton style="margin-left: 550px; margin-top: 50px;" @click="BookSubmit">确认提交</ElButton>
    </ElDialog>
    <div class="table">
      <!-- 图书管理表格 -->
      <ElTable :data="tableData" :default-sort="{ prop: 'id', order: 'increasing' }" style="width: 1150px;">
        <ElTableColumn
          fixed
          prop="id"
          label="书籍id"
          sortable
          width="100px"
        ></ElTableColumn>
        <ElTableColumn prop="cover" label="封面" sortable width="105px">
          <template v-slot="{row}">
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
          sortable
        ></ElTableColumn>
        <ElTableColumn
          prop="author"
          label="作 者"
          width="100px"
          sortable
        ></ElTableColumn>
        <ElTableColumn
          prop="category"
          label="分类"
          width="110px"
          sortable
        ></ElTableColumn>
        <ElTableColumn prop="status" label="状态" width="80px" sortable></ElTableColumn>
        <ElTableColumn prop="cnt" label="字数" width="110px" sortable></ElTableColumn>
        <ElTableColumn
          prop="favorcnt"
          label="收藏人数"
          width="110px"
          sortable
        ></ElTableColumn>
        <ElTableColumn prop="vip" label="VIP书目" width="100px" sortable></ElTableColumn>
        <ElTableColumn label="Operations">
          <template v-slot="scope">
            <div class="button">
              <div class="button1">
                <el-button @click="setInfo(scope.row)">设置信息</el-button>
              </div>
              <div class="button2">
                <el-button size="small" @click="updateInfo(scope.row)">更新内容</el-button>
              </div>
            </div>
            <div class="button3">
                <el-button size="small" @click="updateAvatar(scope.row)">更新封面</el-button>
            </div>
          </template>
        </ElTableColumn>
      </ElTable>
    </div>
    <div class="pagination-block">
      <ElPagination v-model:current-page="pageNum" background layout="prev, pager, next" :total="1000"/>
    </div>
  </div>
</template>

<script>
import { ElTable, ElTableColumn, ElButton, ElDialog, ElDescriptions, ElDescriptionsItem, ElInput, ElSwitch, ElPagination } from "element-plus";
import { getBookDetiles, getBookList } from "@/api/api";
import { reactive,ref,watch} from "vue";
import '../../node_modules/element-plus/theme-chalk/index.css'
import axios from "axios";
export default {
  setup() {
    let tableData = reactive([]);
    let showAdd=ref(false)
    let showInfo=ref(false)
    let showBook = ref(false)
    let selectRow=reactive({})
    let pageNum=ref(1)
    const newBook=reactive({
      title:'',
      category:'',
      brief:'',
      author:'',
      onshelf:false,
      status:'连载',
      vip:false
    })
    const Options = reactive({ page: pageNum.value.toString() }); // Options 需要使用 reactive 定义
    function getdata() {
      getBookList(Options).then((books) => {
        
        let sbooks= books.books;
        sbooks.sort((a, b) => (a - b))
        // console.log(books);
        for (let bookid of sbooks) {
          getBookDetiles(bookid).then((book) => {
            tableData.push(book);
          });
        }
      });
    }
    getdata();
    // 使用 watch 监听 pageNum 的变化
    watch(pageNum, () => {
      console.log(pageNum)
      tableData.splice(0); // 清空原有数据
      Options.page = pageNum.value; // 更新 Options 中的 page 属性
      getdata(); // 调用 getdata 函数重新获取数据
    });
    
    console.log(tableData)
    function addBook(){
      showAdd.value=false
      console.log(newBook.vip)
      console.log(newBook.onshelf)
      axios.post('http://154.8.183.51/manager/newbook', newBook)
        .then(() => {
          alert("修改成功")
        })
        .catch(() => {
          alert("修改失败")
        })
    }
    function setInfo(row){
      showInfo.value=true;
      Object.assign(selectRow, row);
    }
    function updateInfo(row) {
      showBook.value=true;
      Object.assign(selectRow, row);
    }
    function InfoSubmit(){
      showInfo.value=false
      
      // TODO：向服务器发送修改图书信息请求
      axios.post('http://154.8.183.51/manager/newbook',selectRow)
      .then(()=>{
        alert("修改成功")
      })
      .catch(()=>{
        alert("修改失败")
      })
    }
    function updateAvatar(row) {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.click();

      input.addEventListener('change', () => {
        const imageFile = input.files[0];
        const formData = new FormData();
        formData.append('bookid', row.id);
        formData.append('img', imageFile);

        axios.post('http://154.8.183.51/manager/setcover', formData)
          .then(() => {
            alert("修改成功");
          })
          .catch(() => {
            alert("修改失败");
          });
      });
    }

    function BookSubmit() {
      // TODO：向服务器发送修改图书信息请求
      showBook.value=false
      selectRow.bookid=selectRow.id
      console.log(selectRow)
      axios.post('http://154.8.183.51/manager/uploadchapter',selectRow)
      .then(()=>{
        alert("修改成功")
      })
      .catch(()=>{
        alert("修改失败")
      })
    }
    return {
      tableData,
      pageNum,
      newBook,
      showBook,
      showAdd,
      showInfo,
      selectRow,
      addBook,
      setInfo,
      updateInfo,
      InfoSubmit,
      BookSubmit,
      updateAvatar
    };
  },
  components: { ElTable, ElTableColumn, ElButton, ElDialog, ElDescriptions, ElDescriptionsItem, ElInput, ElSwitch, ElPagination },
};
</script>

<style  scoped>

.el-table__body-wrapper {
  overflow-x: auto;
}
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
    width: 1150px;
  margin-top: 50px;
  border: 1px solid #ccc;
}
.button {
  display: flex;
  justify-content: space-between;
}
.button button {
  padding: 0%;
  margin-right: 0px;
  border: none;
  outline: none;
  background-color: transparent;
  text-decoration: solid;
  cursor: pointer;
  font-size: 15px;
}
.button button:hover {
  text-decoration: underline;
}
.button1 button {
  
  color: rgb(4, 249, 82);
}
.button2 button {
  margin-right: 10px;
  margin-top: 4px;
  color: rgb(200, 6, 6);
}
.button3 button{
  padding: 0%;
  margin-right: 0px;
  border: none;
  outline: none;
  background-color: transparent;
  text-decoration: solid;
  cursor: pointer;
  font-size: 15px;
}
.button3 button:hover {
  text-decoration: underline;
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
.pagination-block{
  margin-left: 750px;
}
</style>