import { createRouter, createWebHistory } from 'vue-router'
import Home from 'components/page/Home'
const newLoginComponent = () => import('../components/page/login/newLogin')
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
    { path: '/login', component: newLoginComponent },
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
export default router