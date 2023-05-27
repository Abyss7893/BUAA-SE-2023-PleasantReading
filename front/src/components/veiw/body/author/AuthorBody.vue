<template>
  <div class="author-header">
    <div class="author-info">
      <div class="header-bcg"></div>
      <div class="author-avatar"><img src="http://154.8.183.51/media/UserImg/user_img.jpg" alt="">
      </div>
      <div class="author-msg">
        <h1>花椒猫猫</h1>
        <div class="author-msg-brief">这是一只喜欢吃花椒的猫猫，大家可以摸摸她</div>
        <div class="author-msg-data">
          <span style="margin-right: 12px">作品总数<strong class="msg-strong">10</strong></span>
          <span style="margin-right: 12px">累计写作<strong class="msg-strong">3124.46</strong>万字</span>
        </div>
      </div>
    </div>
  </div>
  <div class="author-content">
    <h2>全部作品</h2>
    <li v-for="(book, idx) in this.books" :key="idx">
      <BookInfoCompnent :book="book" />
    </li>
    <div class="line"></div>
  </div>
</template>

<script>
import BookInfoCompnent from '../search/BookInfoCompnent.vue';
export default {
  components: { BookInfoCompnent, },
  props: {},
  data() {
    return {
      books: [{
        "id": 17,
        "title": "杀路寒",
        "author": "长桴",
        "category": "武侠-传统武侠",
        "status": "连载",
        "brief": "一阕《西江月》，半部《反掌录》。\n一条逃杀路，两个飘零人。\n（书友群：194388020）",
        "score": 0,
        "cnt": 810742,
        "cover": "http://154.8.183.51/media/BookImg/lDs8crqg.jpg",
        "favorcnt": 0,
        "vip": false,
        "fav": false,
        "onShelf": "true"
      }, {
        "id": 17,
        "title": "杀路寒",
        "author": "长桴",
        "category": "武侠-传统武侠",
        "status": "连载",
        "brief": "一阕《西江月》，半部《反掌录》。\n一条逃杀路，两个飘零人。\n（书友群：194388020）",
        "score": 0,
        "cnt": 810742,
        "cover": "http://154.8.183.51/media/BookImg/lDs8crqg.jpg",
        "favorcnt": 0,
        "vip": false,
        "fav": false,
        "onShelf": "true"
      }, {
        "id": 17,
        "title": "杀路寒",
        "author": "长桴",
        "category": "武侠-传统武侠",
        "status": "连载",
        "brief": "一阕《西江月》，半部《反掌录》。\n一条逃杀路，两个飘零人。\n（书友群：194388020）",
        "score": 0,
        "cnt": 810742,
        "cover": "http://154.8.183.51/media/BookImg/lDs8crqg.jpg",
        "favorcnt": 0,
        "vip": false,
        "fav": false,
        "onShelf": "true"
      }, {
        "id": 17,
        "title": "杀路寒",
        "author": "长桴",
        "category": "武侠-传统武侠",
        "status": "连载",
        "brief": "一阕《西江月》，半部《反掌录》。\n一条逃杀路，两个飘零人。\n（书友群：194388020）",
        "score": 0,
        "cnt": 810742,
        "cover": "http://154.8.183.51/media/BookImg/lDs8crqg.jpg",
        "favorcnt": 0,
        "vip": false,
        "fav": false,
        "onShelf": "true"
      }, {
        "id": 17,
        "title": "杀路寒",
        "author": "长桴",
        "category": "武侠-传统武侠",
        "status": "连载",
        "brief": "一阕《西江月》，半部《反掌录》。\n一条逃杀路，两个飘零人。\n（书友群：194388020）",
        "score": 0,
        "cnt": 810742,
        "cover": "http://154.8.183.51/media/BookImg/lDs8crqg.jpg",
        "favorcnt": 0,
        "vip": false,
        "fav": false,
        "onShelf": "true"
      },],
    };
  },
  watch: {},
  computed: {},
  methods: {},
  created() { },
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
</style>