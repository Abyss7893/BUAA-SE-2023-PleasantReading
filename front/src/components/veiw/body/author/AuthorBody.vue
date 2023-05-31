<template>
  <div class="author-header">
    <div class="author-info">
      <div class="header-bcg"></div>
      <div class="author-avatar"><img :src="this.author.img" alt="">
      </div>
      <div class="author-msg">
        <h1>{{ this.$route.params.author }}</h1>
        <div class="author-msg-brief">{{ this.author.profile }}</div>
        <div class="author-msg-data">
          <span style="margin-right: 12px">作品总数<strong class="msg-strong">{{ this.author.works.length }}</strong></span>
          <span style="margin-right: 12px">累计写作<strong class="msg-strong">{{ workCounttoWAN }}</strong>万字</span>
        </div>
      </div>
    </div>
  </div>
  <div class="author-content" v-if="this.books.length != 0">
    <h2>全部作品</h2>
    <li v-for="(book, idx) in this.books" :key="idx">
      <BookInfoCompnent :book="book" />
    </li>
    <div class="line"></div>
  </div>
  <div class="author-content-null" v-if="this.books.length == 0">
    <el-empty description="该作者暂无作品哦~" :image="require('assets/imgs/book_null.png')" image-size="300px" />
  </div>
</template>

<script>
import BookInfoCompnent from '../search/BookInfoCompnent.vue';
import { getAuthor, getBookDetiles } from '@/api/api'
import { ElMessage } from 'element-plus';
export default {
  components: { BookInfoCompnent, },
  data() {
    return {
      author: {
        "profile": "这是一只喜欢吃花椒的猫猫，大家可以摸摸她",
        "img": "http://154.8.183.51/media/UserImg/user_img.jpg",
        "works": [
          {
            "bookID": 2,
            "name": "综武：龙之初，性本善",
            "profile": "苍龙大陆；\n十八岁的林魏一朝觉醒前世记忆，原本计划着继承父亲家业，苟且度日。\n没曾想，这里竟是一个综武世界。\n人在江湖飘，哪能不挨刀，为了更好活着，林魏努力变强。\n白天是名传天下的大善人，晚上就成了要人小命的毒阎罗！\n大明，大宋，大秦……那里有好处，那里就有他的身影。\n……\n多年以后，林魏遍览身边，人间已无对手！\n…………",
            "img": "BookImg/ELOymcKb.jpg"
          }
        ]
      },
      workCount: 0,
      books: [],
    };
  },
  computed: {
    workCounttoWAN() {
      return (this.workCount / 10000).toFixed(2);
    }
  },
  methods: {
    getAuthorInfo() {
      getAuthor(this.$route.params.author).then((data) => {
        if (data.status && data.status == 200) {
          this.author = data.data
          for (let index = 0; index < this.author.works.length; index++) {
            getBookDetiles(this.author.works[index].bookID).then((data) => {
              this.books.push(data)
              this.workCount += data.cnt
            })
          }
        } else {
          ElMessage({
            message: '该作者不存在',
            grouping: true,
            type: 'error',
          })
        }
      })
    }
  },
  created() {
    this.getAuthorInfo()
  },
  mounted() { }
};
</script>
<style lang="scss" scoped>
.author-header {
  width: auto;
  min-height: 200px;
  // color: #fff;
  // background: #fb62971a;
  background-size: cover;
  padding: 10px 0;
}

.header-bcg {
  background: url('~assets/imgs/author_bcg.png');
  background-size: cover;
  // position: absolute;
  float: right;
  margin-top: -30px;
  min-width: 300px;
  height: 200px;
}

.author-info {
  position: relative;
  padding: 40px 20px 20px 20px;
  margin: auto;
  width: 1000px;
  border: 1px solid #e6e6e6;
  background: linear-gradient(to right, #e1a7a4de, #fb62971a);
  border-radius: 15px;
}

.author-avatar {
  position: relative;
  float: left;
  width: 100px;
  text-align: center;

}

.author-avatar img {
  width: 100px;
  height: 100px;
  vertical-align: top;
  border-radius: 50%;
}

.author-msg {
  position: relative;
  margin: 0 0 0 100px;
  padding: 16px 0 0 16px;

}

.author-msg h1 {
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
  font-weight: 600;
}

.author-msg-brief {
  padding: 7px 80px 40px 0;
  opacity: .8;
}

.author-msg-data {
  padding: 17px 0;
  // color: rgba(255, 255, 255, .8);
  border-top: 1px solid rgba(255, 255, 255, .2);
}

.msg-strong {
  font-family: arial;
  font-size: 20px;
  line-height: 0;
  margin: 0 8px 0 8px;
  vertical-align: -.2ex;
  // color: #fff;
}

.author-content {
  margin: auto;
  width: 1000px;
  min-height: 400px;
}

.author-content li {
  border-top: 1px solid #e6e6e6;
  height: 180px;
  padding-top: 25px;
}

.author-content h2 {
  font: 28px/1.5 KaiTi;
  font-weight: bolder;
  margin: 16px 0 0 0;
  padding: 0 0 6px;
  color: #262626;
  border-bottom: 1px solid #7f7f7f;
}

.line {
  width: 100%;
  border-top: 1px solid #e6e6e6;
  margin-bottom: 16px;
}

.author-content-null {
  min-height: 350px;
  width: 1000px;
  margin: auto;
}
</style>