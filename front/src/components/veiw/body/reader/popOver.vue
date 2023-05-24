<template>
  <div>
    <div v-show="showMenu" class="popover" :style="{
      left: `${x}px`,
      top: `${y}px`
    }" @mousedown.prevent="">
      <!-- <span class="item" @mousedown.prevent="handleAction('share')">
        Share
      </span> -->
      <span class="item" @mousedown.prevent="highlight">高亮</span>
      <!-- more buttons here -->
    </div>

    <!-- insterted text is displayed here -->
    <div ref="slot" tabindex="0">
      <slot></slot>
    </div>
  </div>
</template>
<script>

export default {
  name: "popOver",
  data() {
    return {
      x: 0,
      y: 0,
      showMenu: false,
      nowSelectionRange: null,
      nowSelection: null,
      selectionRanges: [],
    }
  },
  computed: {
    highlightableEl() {
      return this.$refs.slot
    }
  },
  mounted() {
    window.addEventListener('mouseup', this.onMouseup)
  },

  unmounted() {
    window.removeEventListener('mouseup', this.onMouseup)
  },
  methods: {
    onMouseup() {
      const selection = window.getSelection()
      let selectionRange = null
      if (selection.rangeCount) {
        selectionRange = selection.getRangeAt(0)
      }
      else
        return
      // startNode 是选取开始的元素
      const startNode = selectionRange.startContainer.parentNode

      // endNode 是选取结束的元素
      const endNode = selectionRange.endContainer.parentNode

      // 如果选中部分不在 <VueSelectionShare> 里头
      // 或者
      // 如果 startNode !== endNode
      // 不显示菜单
      if (!this.highlightableEl.contains(startNode) || !this.highlightableEl.contains(endNode)) {
        this.showMenu = false
        return
      }

      // 获取选中文本的 x, y, width
      const { x, y, width } = selectionRange.getBoundingClientRect()

      // 如果 width === 0，隐藏菜单
      if (!width) {
        this.showMenu = false
        return
      }

      // 设置菜单的位置
      // 设置 selectedText 设置成选中的文本
      // 显示菜单
      this.x = x + (width / 2) - this.highlightableEl.offsetParent.offsetLeft
      this.y = y + window.scrollY - this.highlightableEl.offsetParent.offsetTop - 10
      this.showMenu = true
      this.nowSelectionRange = selectionRange
      this.nowSelection = selection
    },
    highlight() {
      if (CSS.highlights) {
        this.selectionRanges.push(this.nowSelectionRange)
        // 下面这个注释千万别删，不然编译过不去
        // eslint-disable-next-line no-undef
        const highlight = new Highlight(...this.selectionRanges)
        CSS.highlights.set("highlight1", highlight)
        this.nowSelection.removeAllRanges();
        this.showMenu = false
      }
    },
  }
}
</script>
<style>
::highlight(highlight1) {
  color: #d7cb1e;
}

.popover {
  font-size: 15px;
  height: 20px;
  padding: 5px 10px;
  background: #f56c6c;
  border: 2px solid rgba(0, 0, 0, .1);
  border-radius: 3px;
  position: absolute;
  top: 0;
  left: 0;
  transform: translate(-50%, -100%);
  transition: 0.2s all;
  display: flex;
  justify-content: center;
  align-items: center;
}

.popover:after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: -5px;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #f56c6c;
}

.item {
  /* hover 前颜色 */
  color: aliceblue;
  cursor: pointer;
}

.item:hover {
  /* hover 后颜色（粉色） */
  color: wheat;
}




.item+.item {
  margin-left: 10px;
}
</style>