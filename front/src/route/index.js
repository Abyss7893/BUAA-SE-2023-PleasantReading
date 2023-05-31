import { createRouter, createWebHistory } from 'vue-router'
import { ElMessage } from 'element-plus'
import Home from 'components/page/Home'
const LoginComponent = () => import('../components/page/login/LoginComponent')
const RegisterComponent = () => import('../components/page/login/RegisterComponent')
const BookDetail = () => import('../components/veiw/book/BookDetail')
const PersonalCenter = () => import('../components/page/PersonalCenter')
const InfoComponent = () => import('../components/page/Personal/InfoComponent')
const Reader = () => import('components/page/Reader')
const MyBookBody = () => import('../components/veiw/body/mybooks/MyBookBody')
const RankBody = () => import('../components/veiw/rank/RankBody')
const MyComment = () => import('../components/page/Personal/MyComment')
// const Home = () => import('components/page/Home')
const AllBook = () => import('../components/veiw/body/AllBook')
const Search = () => import('../components/page/Search')
const Author = () => import('components/page/Author')
import 'css/home.css'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    { path: '/login', component: LoginComponent },
    // { path:'/test',name:'test',component:HelloWorld},
    { path: '/register', component: RegisterComponent },
    {
      path: '/book/:id',
      name: 'book-detail',
      component: BookDetail
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
  // 获取存储token的开始时间
  const tokenStartTime = window.localStorage.getItem('tokenStartTime')
  // 后台给出的token有效时间，一个星期 单位 是秒
  // 我们自己定义6天过期，让用户重新登录一下， 用户总不可能在一个页面挂机一天吧
  const timeOver = 24 * 3600 * 1000
  // 当前时间
  let date = new Date().getTime()
  // 如果大于说明是token过期了
  if (date - tokenStartTime > timeOver) {
    flag = true
    localStorage.clear()
  }
  // 如果token过期了
  if (token && flag) {
    // if (to.path == '/login') return next()
    // 注意要import element的Message组件
    ElMessage.error("登录状态过期，请重新登录")
    // return next('/login')
    // 如果token没有过期，又是选择了登录页面就直接重定向到首页，不需要重新输入账户密码
  }
  // else if (to.path == '/login') {
  //   return next('/home/ks')
  // }
  next()

})
export default router