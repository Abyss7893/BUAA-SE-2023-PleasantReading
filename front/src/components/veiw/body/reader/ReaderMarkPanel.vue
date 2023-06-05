<template>
  <div class="panel-box">
    <a class="close-panel-button" @click="closeMark"><el-icon class="close-panel-button-icon" size="26" color="#a6a6a6">
        <Close />
      </el-icon></a>
    <div class="panel catalog mark">
      <h4 class="lang">书签</h4>
      <div v-if="!islogin">
        <el-empty description="请登录以访问添加书签！">
          <el-button class="elbutton" @click="this.$store.commit('showlogin')">登录</el-button>
        </el-empty>
      </div>
      <ul ref="clist" v-else-if="markinfo && markinfo.marks">
        <li class="mark" v-for="(mark, markId) in markinfo.marks" :key="markId"><a
            :href="'/reader/' + markinfo.bookid + '/' + mark.chapter">
            <div class="time">{{ parseTime(mark.timestamp) }}</div>{{
              mark.title }}
          </a></li>
      </ul>
      <div v-else>
        <el-empty description="您还没有添加书签哦!"></el-empty>
      </div>
    </div>
  </div>
</template>

<script>
import { getbookMarks } from '@/api/api'
import { mapGetters } from 'vuex';
export default {
  name: "ReaderMarkPanel",
  components: {},
  props: {},
  data() {
    return {
      markinfo: {},
    };
  },
  computed: {
    ...mapGetters(['islogin', 'markupdate'])
  },
  watch: {
    islogin(newVal) {
      if (newVal)
        getbookMarks(this.$route.params.bookid).then((data) => {
          if (data.status && data.status == 200) {
            this.markinfo = data.data.markinfo
          } else
            console.log(data)
        })
      else
        this.markinfo = {}
    },
    markupdate() {
      getbookMarks(this.$route.params.bookid).then((data) => {
        if (data.status && data.status == 200) {
          this.markinfo = data.data.markinfo
        } else
          console.log(data)
      })
    }
  },
  created() {
    getbookMarks(this.$route.params.bookid).then((data) => {
      if (data.status && data.status == 200) {
        this.markinfo = data.data.markinfo
      } else
        console.log(data)
    })
  },
  methods: {
    parseTime(time) {
      var date = new Date(time);
      var year = date.getFullYear();
      var month = date.getMonth() + 1;
      var day = date.getDate();
      var hour = date.getHours();
      var minute = date.getMinutes();
      return year + "年" + month + "月" + day + "日" + hour + "时" + minute + "分"
    },
    closeMark() {
      this.$parent.changeVisiable("mark");
    },
  },

};
</script>
<style lang="scss" scoped>
.reader-menu .mark ul li {
  width: 96%;
}

.reader-menu .mark {
  width: 600px;
}

.reader-menu .mark ul {
  margin-top: 8px;
}

.reader-menu .mark ul li .time {
  float: left;
  margin-right: 12px;
}

.elbutton {
  color: #f0e8e8;
  border-color: #f37e7e;
  background-color: #f37e7e;
  transition: all .3s;
}

.elbutton:hover {
  color: #fff;
  border-color: #f37e7e;
  background-color: #ed5050;
}
</style>