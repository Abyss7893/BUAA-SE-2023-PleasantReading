<template>
  <div class="rs-wrap">
    <a href="/allbook">
      <div>
        推荐作品
      </div>
      <el-icon>
        <ArrowRight />
      </el-icon>
    </a>
    <a href="/rank">
      <div>排行作品</div><el-icon>
        <ArrowRight />
      </el-icon>
    </a>
    <a @click="randomReading">
      <div>随机阅读</div><el-icon>
        <ArrowRight />
      </el-icon>
    </a>
    <a href="/allbook?vip=true">
      <div>会员服务</div><el-icon>
        <ArrowRight />
      </el-icon>
    </a>
  </div>
</template>

<script>
export default {
  methods: {
    randomReading() {
      this.$router.push("/book/" + Math.ceil(Math.random() * 250))
    }
  },
};
</script>
<style lang="scss" scoped>
.rs-wrap {
  position: absolute;
  left: 98%;
  top: -90px;
  z-index: 151;
  width: 200px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

.rs-wrap>a {
  display: block;
  position: relative;
  padding: 8px 12px;
  margin: 12px 8px;
  width: 160px;
  border-radius: 6px;
  cursor: pointer;
}

.rs-wrap>a:hover {
  background-color: #f8b2b27d;
}

.rs-wrap>a>.el-icon {
  float: right;
  position: absolute;
  left: calc(100% - 24px);
  top: calc(50% - 8px);
}
</style>