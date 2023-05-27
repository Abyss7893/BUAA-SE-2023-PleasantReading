<template>
  <div class="container">
    <div class="search ">
            <form autocomplete="off">
              <div class="finder">
                <div class="finder__outer">
                  <div class="finder__inner">
                    <div class="finder__icon" ref="icon"></div>
                    <input class="finder__input" type="text" v-model="searchContent" />
                  </div>
                </div>
              </div>
            </form>
        </div>
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
        <ElDescriptionsItem label="是否上架"><ElSwitch style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949" v-model="selectRow.onShelf" active-text="true" inactive-text="false" active-value="true" inactive-value="false"/></ElDescriptionsItem>
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
    <!-- 修改作者信息的弹窗 -->
    <ElDialog v-model="showAuthor" :destroy-on-close="true">
      <ElDescriptions border :column="1">
        <ElDescriptionsItem label="头像">
          <ElAvatar :src="selectRow.img" :size="100"></ElAvatar>
          <ElButton style="margin-left: 50px;" @click="selectAvatar">上传头像</ElButton>
        </ElDescriptionsItem>
        <ElDescriptionsItem label="姓名">{{selectRow.author}}</ElDescriptionsItem>
        <ElDescriptionsItem label="简介"><ElInput type="textarea" rows="3" v-model="selectRow.profile"></ElInput></ElDescriptionsItem>
      </ElDescriptions>
      <ElButton style="margin-left: 550px; margin-top: 50px;" @click="AuthorSubmit">确认提交</ElButton>
    </ElDialog>
    <div class="table">
      <!-- 图书管理表格 -->
      <ElTable :data="tableData" :default-sort="{ prop: 'id', order: 'increasing' }" style="width: 1250px;">
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
        <ElTableColumn prop="onShelf" label="是否上架" width="120px" sortable></ElTableColumn>
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
            <div class="button">
              <div class="button3">
                  <el-button size="small" @click="updateAvatar(scope.row)">更新封面</el-button>
              </div>
              <div class="button4">
                    <el-button size="small" @click="updateAuthor(scope.row)">更新作者</el-button>
              </div>
            </div>
            
          </template>
        </ElTableColumn>
      </ElTable>
    </div>
    <div class="pagination-block">
      <ElPagination v-model:current-page="pageNum" background layout="prev, pager, next,jumper" :total="maxPages*10"/>
    </div>
  </div>
</template>

<script>
import { ElTable, ElTableColumn, ElButton, ElDialog, ElDescriptions, ElDescriptionsItem, ElInput, ElSwitch, ElPagination, ElAvatar } from "element-plus";
import { getBookDetiles, getBookList,getSearchBookIds } from "@/api/api";
import { reactive,ref,watch,onMounted} from "vue";
import '../../node_modules/element-plus/theme-chalk/index.css'
import axios from "axios";
export default {
  setup() {
    const input = ref(null); // 声明 ref 变量
    const finder = ref(null);
    const form = ref(null);
    const searchContent = ref('')
    const maxPages=ref(0)
    let tableData = reactive([]);
    let showAdd=ref(false)
    let showInfo=ref(false)
    let showBook = ref(false)
    let showAuthor = ref(false)
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
    const formData=new FormData()
    const Options = reactive({ page: pageNum.value.toString() }); // Options 需要使用 reactive 定义
    const handleFocus = () => {
      finder.value.classList.add("active");
    }
    const handleBlur = () => {
      if (searchContent.value.length === 0) {
        finder.value.classList.remove("active");
      }
    }
    const handleSubmit = (ev) => {
      ev.preventDefault();
      finder.value.classList.add("processing");
      finder.value.classList.remove("active");
      input.value.disabled = true;
      // TODO：对接其他人写好的搜索接口，需要更新图书内容
      getSearchBooks(searchContent.value,Options.page)
      setTimeout(() => {
        finder.value.classList.remove("processing");
        input.value.disabled = false;
        if (input.value.value.length > 0) {
          finder.value.classList.add("active");
        }
      }, 1000);
    }
    onMounted(() => {
      input.value = document.querySelector(".finder__input");
      finder.value = document.querySelector(".finder");
      form.value = document.querySelector("form");
      input.value.addEventListener("focus", handleFocus);
      input.value.addEventListener("blur", handleBlur);
      form.value.addEventListener("submit", handleSubmit);
    })
    function getdata() {
      var token = localStorage.getItem("token")
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
      getBookList(Options).then((books) => {
        maxPages.value=books.pages
        let sbooks= books.books;
        sbooks.sort((a, b) => (a - b))
        for (let bookid of sbooks) {
          getBookDetiles(bookid).then((book) => {
            tableData.push(book);
          });
        }
      });
    }
    function getSearchBooks(keywords, page) {
      console.log("123")
      tableData.splice(0);
      getSearchBookIds(keywords, page).then((data) => {
        if (data.status && data.status == 200) {
          let bookids= data.data.books
          let pages= data.data.pages
          maxPages.value=pages
          if (Options.page > pages) {
            alert("非法页面访问！")
            return
          }
          if (bookids.length == 0) {
            alert("该查询结果为空！")
            return
          }
          for (let index = 0; index < bookids.length; index++) {
            getBookDetiles(bookids[index]).then((data) => {
              tableData.push(data)
            })
          }
        } else {
          alert("该关键词查询不到任何结果！")
        }
      })
    }
    getdata();
    // 使用 watch 监听 pageNum 的变化
    watch(pageNum, () => {
      tableData.splice(0); // 清空原有数据
      Options.page = pageNum.value; // 更新 Options 中的 page 属性
      if(searchContent.value.length==0)
      getdata(); // 调用 getdata 函数重新获取数据
      else
      getSearchBooks(searchContent.value,Options.page)
    });
    
    function addBook(){
      showAdd.value=false
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
      if(selectRow.onShelf=='true') selectRow.onshelf=true
      else selectRow.onshelf = false
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
    function updateAuthor(row){
      showAuthor.value=true
      Object.assign(selectRow, row);

      console.log(selectRow.author)
      axios.post(`http://154.8.183.51/book/author/${selectRow.author}`,
      {
        Headers:{
          'Content-Type': 'application/json',
        }
      })
      .then((response)=>{
        selectRow.profile=response.data.profile
        selectRow.img=response.data.img
      })
      console.log(formData)
    }
    function selectAvatar(){
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.click();
      input.addEventListener('change', () => {
        const imageFile = input.files[0];
        formData.append('img',imageFile)
        selectRow.img= URL.createObjectURL(imageFile)
      });
    }
    function AuthorSubmit(){
      showAuthor.value=false
      formData.append('name',selectRow.author)
      formData.append('profile',selectRow.profile)
      console.log(formData)
      axios.post('http://154.8.183.51/manager/uploadauthor',formData)
      .then(()=>{
        alert("更新作者信息成功")
      })
      .catch(console.error())
    }
    function BookSubmit() {
      // TODO：向服务器发送修改图书信息请求
      showBook.value=false
      selectRow.bookid=selectRow.id
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
      showAuthor,
      searchContent,
      formData,
      maxPages,
      addBook,
      setInfo,
      updateInfo,
      InfoSubmit,
      BookSubmit,
      updateAvatar,
      updateAuthor,
      selectAvatar,
      AuthorSubmit,
    };
  },
  components: { ElTable, ElTableColumn, ElButton, ElDialog, ElDescriptions, ElDescriptionsItem, ElInput, ElSwitch, ElPagination, ElAvatar },
};
</script>

<style  scoped>
.container{
  
  margin-right: 520px;
  width: 100%;
  
}
.el-table__body-wrapper {
  overflow-x: auto;
}
.head {
  margin-top: 150px;
  margin-left: 200px;
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
  width: 1250px;
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
.button4 button{
  margin-right: 10px;
  margin-top: 4px;
  color: #3498db;
}
.button4 button:hover {
  text-decoration: underline;
}
.button-big {
  background: linear-gradient(to right, #2ecc71, #3498db);
  border: 5px dotted #2ecc71;
  border-radius: 20px;
  color: white;
  width: 200px;
  height: 50px;
  transition: all 0.3s ease;
}

.button-big:hover {
  background: linear-gradient(to right, #3498db, #2ecc71);
  width: 250px;
  height: 60px;
  cursor: pointer;
}
.pagination-block{
  margin-left: 850px;
  margin-bottom: 50px;
}
.search {
  position: fixed;
  top: 50px;
  margin-left: 200px;
  
  z-index: 1000;
  width: 100%;
}

form {
  transition: all 0.5s;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.finder {
  border: 1px solid #fff;
  background-color: #f6f5f0;
  
  border-radius: 15px;
  padding: 8px;
  box-shadow: 9px 9px 16px rgba(189, 189, 189, 0.6), -9px -9px 16px rgba(255, 255, 255, 0.5);
}

.finder__outer {
  display: flex;
  width: 800px; /* 修改为更宽的宽度 */
  height: 0px;
  padding: 2rem 3rem; /* 修改内边距 */
  border-radius: 10px;
  box-shadow: inset 10px 10px 15px -10px #c3c3c3, inset -10px -10px 15px -10px #ffffff;
}


.finder__inner {
  display: flex;
  align-items: center;
  position: relative;
  flex: 1;
}


.finder__input {
  height: calc(100% + 2rem); /* 修改为更小的高度 */
  border: none;
  background-color: transparent;
  outline: none;
  font-size: 1.5rem;
  letter-spacing: 0.75px;
}


.finder__icon {
  width: 40px;
  height: 40px;
  margin-right: 1rem;
  transition: all 0.2s;
  box-shadow: inset 0 0 0 20px #292929;
  border-radius: 50%;
  position: relative;
}
.finder__icon:after, .finder__icon:before {
  display: block;
  content: "";
  position: absolute;
  transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.finder__icon:after {
  width: 10px;
  height: 10px;
  background-color: #292929;
  border: 3px solid #f6f5f0;
  top: 50%;
  position: absolute;
  transform: translateY(-50%);
  left: 0px;
  right: 0;
  margin: auto;
  border-radius: 50%;
}
.active .finder__icon:after {
  border-width: 10px;
  background-color: #f6f5f0;
}
.finder__icon:before {
  width: 4px;
  height: 13px;
  background-color: #f6f5f0;
  top: 50%;
  left: 20px;
  transform: rotateZ(45deg) translate(-50%, 0);
  transform-origin: 0 0;
  border-radius: 4px;
}
.active .finder__icon:before {
  background-color: #292929;
  width: 6px;
  transform: rotateZ(45deg) translate(-50%, 25px);
}
.processing .finder__icon {
  transform-origin: 50%;
  animation: spinner 0.3s linear infinite;
  animation-delay: 0.5s;
}
.active .finder__icon {
  transform: translateY(-5px);
}

@keyframes spinner {
  0% {
    transform: rotateZ(45deg);
  }
  100% {
    transform: rotateZ(405deg);
  }
}
</style>