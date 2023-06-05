import { createRouter, createWebHistory } from 'vue-router'
import { ElMessage } from 'element-plus'
import Home from 'components/page/Home'

const MyBookBody = () => import(/* webpackChunkName: "my-book-body" */ '../components/veiw/body/mybooks/MyBookBody' /* webpackPrefetch: true */)
const RankBody = () => import(/* webpackChunkName: "rank-body" */ '../components/veiw/rank/RankBody' /* webpackPrefetch: true */)
const MyComment = () => import(/* webpackChunkName: "my-comment" */ '../components/page/Personal/MyComment' /* webpackPrefetch: true */)
// const Home = () => import('components/page/Home')
const AllBook = () => import(/* webpackChunkName: "all-book" */ '../components/veiw/body/AllBook' /* webpackPrefetch: true */)
const MyMarkBody = () => import(/* webpackChunkName: "my-mark-body" */ '../components/veiw/body/mymark/MyMarkBody' /* webpackPrefetch: true */)
const Search = () => import(/* webpackChunkName: "search" */ '../components/page/Search' /* webpackPrefetch: true */)
const Author = () => import(/* webpackChunkName: "author" */ 'components/page/Author' /* webpackPrefetch: true */)
const BookDetail = () => import(/* webpackChunkName: "book-detail" */ '../components/veiw/book/BookDetail' /* webpackPrefetch: true */)
const PersonalCenter = () => import(/* webpackChunkName: "personal-center" */ '../components/page/PersonalCenter' /* webpackPrefetch: true */)
const InfoComponent = () => import(/* webpackChunkName: "info-component" */ '../components/page/Personal/InfoComponent' /* webpackPrefetch: true */)
const Reader = () => import(/* webpackChunkName: "reader" */ 'components/page/Reader' /* webpackPrefetch: true */)
const MyNote = () => import(/* webpackChunkName: "my-note" */ '../components/veiw/body/mynote/MyNotesComponent' /* webpackPrefetch: true */)
// import 'css/home.css'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/book/:id',
      name: 'book-detail',
      component: BookDetail
    },
    {
      path: '/mark',
      name: 'mark',
      component: MyMarkBody
    }, {
      path: '/mynote',
      name: 'note',
      component: MyNote
    },
    {
      path: '/user',
      component: PersonalCenter,
      children: [
        {
          path: 'info',
          name: 'info',
          component: InfoComponent
        },
        {
          path: 'comment',
          name: 'comment',
          component: MyComment
        },
      ]
    },

    {
      path: '/reader/:bookid/:chapter',
      name: 'reader',
      component: Reader,
    },
    // {
    //   path: '/allbook/:category/:property/:status/:wordCount/:sort',
    //   name: 'bookOrder',
    //   component: AllBook,
    //   props: true,
    //   meta: {
    //     // 可选的meta数据
    //   }
    // },
    {
      path: '/mybook',
      component: MyBookBody,
      name: 'mybook',
    },
    {
      path: '/rank',
      component: RankBody,
      name: 'rank',
    },
    {
      path: '/allbook',
      component: AllBook,
      name: 'allbook',
    },
    {
      path: '/allbook',
      name: 'Child',
      component: AllBook,
      props: true,
    },
    {
      path: '/search',
      component: Search,
      name: 'search',
    },
    {
      path: '/author/:author',
      component: Author,
      name: 'author',
    },
  ],
  scrollBehavior() {
    // 始终滚动到顶部
    return { top: 0 }
  },
})

router.beforeEach((to, from, next) => {
  // 获取存储localStorage的token
  let token = window.localStorage.getItem('token')
  let flag = false
  const tokenStartTime = window.localStorage.getItem('tokenStartTime')

  const timeOver = 24 * 3600 * 1000
  // 当前时间
  let date = new Date().getTime()
  // 如果大于说明是token过期了
  if (!tokenStartTime || date - tokenStartTime > timeOver) {
    flag = true
  }
  // 如果token过期了
  if (token && flag) {
    ElMessage.error("用户登录过期，请重新登录")
    this.$store.commit("signOut")

  }
  next()
})
export default router