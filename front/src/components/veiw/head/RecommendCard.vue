<template>
  <div class="left">
    <div class="title">推荐书目</div>
    <div class="book-list">
      <div class="book-list-item" @click="this.$router.push('/book/' + bookdata.bookid)" @mouseenter="showRightCard(idx)"
        @mouseleave="closeRightCard(idx)" v-for="(bookdata, idx) in bookdatas" :key="idx">{{ bookdata.title }}
        <div class="right" v-if="rightShow[idx]">
          <div class="card" id="card">
            <div class="photo">
              <img :src="bookdata.avg" alt="">
            </div>
            <h1>{{ bookdata.title }}</h1>
            <h2>{{ bookdata.author }}</h2>
            <p>{{ bookdata.profile }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecommendCard",
  components: {},
  props: {},
  data() {
    return {
      rightShow: [false, false, false, false, false,],
      showdata: { avg: "1" },
      bookdatas: [{
        bookid: 250,
        avg: '	http://154.8.183.51/media/BookImg/default.jpg',
        title: '重生之我在北航卖西瓜',
        author: '奈奈酱想摸鱼c',
        profile: '林恩挑战魔君失败后，意外获得了回溯时间的能力，当他再次睁眼，已经成了北航旁边一个...',
      },
      {
        bookid: 185,
        avg: 'http://154.8.183.51/media/BookImg/abCZwBoz.jpg',
        title: '英灵时代，十连保底',
        author: '苹果咖啡味',
        profile: '我叫白榆，是一个超能力者。 超能力名为保底法则。 买饮料十次，最后一次必然是...',
      },
      {
        bookid: 1,
        avg: '	http://154.8.183.51/media/BookImg/teeZ85vW.jpg',
        title: '综武：偷看我的日记',
        author: '路人.v1',
        profile: '人在综武，每天写日记就能变强。 定个小目标，没成天下第一之前好好苟起来。 只是...',
      },
      {
        bookid: 2,
        avg: 'http://154.8.183.51/media/BookImg/ELOymcKb.jpg',
        title: '综武：龙之初，性本善',
        author: '扫墓上坟',
        profile: '苍龙大陆； 十八岁的林魏一朝觉醒前世记忆，原本计划着继承父亲家业，苟且度日。没曾想...',
      },
      {
        bookid: 5,
        avg: 'http://154.8.183.51/media/BookImg/XjymiETu.jpg',
        title: '被迫当反派的我义字为先',
        author: '夜影.cs',
        profile: '我行我的路，你笑你的痴。利字腰间挂，情义两肩挑。侠情柔骨何处觅，自上心乡寻宝刀。',
      },
      ],
    };
  },
  watch: {},
  computed: {},
  methods: {
    closeIcon() {
      const mycard = document.getElementById('card');
      mycard.classList.toggle('show-card')
    },
    showRightCard(id) {
      this.rightShow[id] = true
    },
    closeRightCard(id) {
      this.rightShow[id] = false
    },
  },
  created() { },
  mounted() { }
};
</script>
<style lang="scss" scoped>
.left-navi div.left {
  animation: fadeIn .3s;
  top: 60px;
  position: absolute;
  background: white;
  width: 240px;
  border-radius: 12px;
  cursor: default;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.left-navi div.left .title {
  line-height: 20px;
  height: 20px;
  font-size: 20px;
  font-weight: bold;
  padding: 8px;
  margin: 8px 8px;
  color: #231e1e;
  width: 200px;
}

.left-navi div.left .book-list-item {
  border-radius: 12px;
  line-height: 20px;
  margin: 4px auto 12px auto;
  width: 198px;
  padding: 12px 16px;
  cursor: pointer;
}

.left-navi div.left .book-list-item:hover {
  background-color: rgba(248, 178, 178, 0.4901960784);
}

.card {
  top: 0;
  left: 95%;
  z-index: 1;
  position: absolute;
  width: 240px;
  height: 100%;
  background-color: #758a99;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  color: #fff;
  box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
  flex-shrink: 0;
  overflow: hidden;
}

.card .photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}


.card .photo {
  /* 绝对定位 */
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  border-radius: 0%;
  overflow: hidden;
  transition: 0.5s;
}


.card:hover .photo {
  top: 30px;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
}


.card .photo::before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, transparent 50%, #222);
}

.card h1 {
  position: absolute;
  top: 100%;
  font-size: 16px;
  transition: 0.5s;
}

.card:hover h1 {
  top: 140px;
}

.card h2 {
  position: absolute;
  margin: auto;
  top: 58%;
  z-index: -1;
  font-size: 16px;
}

.card p {
  position: absolute;
  margin: auto;
  width: 80%;
  top: 68%;
  z-index: -1;
  font-size: 16px;
}
</style>