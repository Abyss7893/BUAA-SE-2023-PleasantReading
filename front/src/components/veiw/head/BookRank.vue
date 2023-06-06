<template>
  <div class="leaderboard">
    <h1>
      <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M822.997333 910.037333H201.002667a33.450667 33.450667 0 0 1-30.336-34.133333 32.64 32.64 0 0 1 30.336-30.336H477.866667v-166.869333a227.456 227.456 0 0 1-189.610667-166.869334h-3.797333A111.744 111.744 0 0 1 170.666667 398.037333V170.496h113.792a62.506667 62.506667 0 0 1 64.469333-56.874667h326.186667a62.506667 62.506667 0 0 1 64.469333 56.874667H853.333333v227.541333a111.701333 111.701333 0 0 1-113.749333 113.792h-7.594667a222.378667 222.378667 0 0 1-189.653333 166.869334v166.869333H819.2a29.866667 29.866667 0 0 1 30.336 30.336 28.330667 28.330667 0 0 1-26.538667 34.133333zM348.928 178.090667v276.864a163.114667 163.114667 0 0 0 326.186667 0V178.090667z m390.656 56.874666v212.394667a50.176 50.176 0 0 0 49.28-49.322667V234.965333z m-504.448 0v163.072a50.218667 50.218667 0 0 0 49.322667 49.493334V235.136z">
        </path>
      </svg>
      好评排行榜
    </h1>
    <ol>
      <li v-for="(item, index) in tableData.slice(0, 5)" :key="index" @click="this.$router.push('/book/' + item.id)">
        <mark>{{ item.title || '还未加载' }}</mark>
        <small>{{ item.score.slice(0, 4) || '还未加载' }}</small>
      </li>
    </ol>
  </div>
</template>

<script>
import { getBookList, getBookDetiles } from '@/api/api';
import axios from 'axios';

import { reactive } from 'vue';
export default {
  setup() {
    const tableData = reactive([])
    const Options = reactive({ page: 1, order: 'score' });
    function compareNum(y, x) {
      if (x.score < y.score) {
        return -1;
      } else if (x.score == y.score) {
        return 0;
      } else if (x.score > y.score) {
        return 1;
      }
    }
    function getdata() {
      var token = localStorage.getItem("token")
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;

      getBookList(Options).then((books) => {
        var sbooks = books.books;
        for (let bookid of sbooks) {
          getBookDetiles(bookid).then((book) => {
            tableData.push(book);
            tableData.sort(compareNum)
          });
        }

      });
    }
    getdata()
    return {
      tableData,
    }
  }
}
</script>

<style lang="scss" scoped>
.leaderboard {
  animation-name: fadeIn;
  animation-duration: .3s;
  position: absolute;
  top: 100%;
  width: 300px;
  height: 100%px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 7px 30px rgba(62, 9, 11, 0.3);
}

.leaderboard h1 {
  font-size: 18px;
  color: white;
  background-color: #8eb1e552;
  padding: 12px 13px 12px;
}

.leaderboard h1 svg {
  width: 25px;
  height: 26px;
  position: relative;
  top: 3px;
  margin-right: 6px;
  vertical-align: baseline;
}

.leaderboard ol {
  counter-reset: leaderboard;
  cursor: default;
}

.icon {
  width: 38px;
  fill: red;
}

.leaderboard ol li {
  line-height: 24px;
  position: relative;
  z-index: 1;
  font-size: 14px;
  counter-increment: leaderboard;
  padding: 18px 10px 18px 50px;
  cursor: pointer;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  transform: translateZ(0) scale(1, 1);
}

.leaderboard ol li::before {
  content: counter(leaderboard);
  position: absolute;
  z-index: 2;
  top: 15px;
  left: 15px;
  width: 20px;
  height: 20px;
  line-height: 20px;
  color: #f8b2b27d;
  background: #fff;
  border-radius: 20px;
  text-align: center;
}

.leaderboard ol li mark {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  position: absolute;
  z-index: 2;
  top: 0;
  left: 0;
  height: 100%;
  padding: 16px 10px 9px 50px;
  margin: 0;
  background: none;
  color: #fff;
}

.leaderboard ol li mark::before,
.leaderboard ol li mark::after {
  content: "";
  position: absolute;
  z-index: 1;
  bottom: -11px;
  left: -9px;
  border-top: 10px solid #f8b2b27d;
  border-left: 10px solid transparent;
  transition: all 0.1s ease-in-out;
  opacity: 0;
}

.leaderboard ol li mark::after {
  left: auto;
  right: -9px;
  border-left: none;
  border-right: 10px solid transparent;
}

.leaderboard ol li small {
  color: #fff;
  position: relative;
  z-index: 2;
  display: block;
  text-align: right;
}

.leaderboard ol li::after {
  content: "";
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #f8b2b27d;
  box-shadow: 0 3px 0 rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease-in-out;
  opacity: 0;
}

.leaderboard ol li:nth-child(1) {
  background: #f8b2b27d;
}

.leaderboard ol li:nth-child(1)::after {
  background: #f8b2b27d;
}

.leaderboard ol li:nth-child(2) {
  background: #f8b2b27d;
}

.leaderboard ol li:nth-child(2)::after {
  background: #f8b2b27d;
  box-shadow: 0 2px 0 rgba(0, 0, 0, 0.08);
}

.leaderboard ol li:nth-child(2) mark::before,
.leaderboard ol li:nth-child(2) mark::after {
  border-top: 6px solid #f8b2b27d;
  bottom: -7px;
}

.leaderboard ol li:nth-child(3) {
  background: #f8b2b27d;
}

.leaderboard ol li:nth-child(3)::after {
  background: #f8b2b27d;
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.11);
}

.leaderboard ol li:nth-child(3) mark::before,
.leaderboard ol li:nth-child(3) mark::after {
  border-top: 2px solid #f8b2b27d;
  bottom: -3px;
}

.leaderboard ol li:nth-child(4) {
  background: #f8b2b27d;
}

.leaderboard ol li:nth-child(4)::after {
  background: #f8b2b27d;
  box-shadow: 0 -1px 0 rgba(0, 0, 0, 0.15);
}

.leaderboard ol li:nth-child(4) mark::before,
.leaderboard ol li:nth-child(4) mark::after {
  top: -7px;
  bottom: auto;
  border-top: none;
  border-bottom: 6px solid #f8b2b27d;
}

.leaderboard ol li:nth-child(5) {
  background: #f8b2b27d;
  border-radius: 0 0 10px 10px;
}

.leaderboard ol li:nth-child(5)::after {
  background: #f8b2b27d;
  box-shadow: 0 -2.5px 0 rgba(0, 0, 0, 0.12);
  border-radius: 0 0 10px 10px;
}

.leaderboard ol li:nth-child(5) mark::before,
.leaderboard ol li:nth-child(5) mark::after {
  top: -9px;
  bottom: auto;
  border-top: none;
  border-bottom: 8px solid #f8b2b27d;
}

.leaderboard ol li:hover {
  z-index: 2;
  overflow: visible;
}

.leaderboard ol li:hover::after {
  opacity: 1;
  transform: scaleX(1.06) scaleY(1.03);
}

.the-most {
  position: fixed;
  z-index: 1;
  bottom: 0;
  left: 0;
  width: 50vw;
  max-width: 200px;
  padding: 10px;
}

.the-most img {
  max-width: 100%;
}
</style>