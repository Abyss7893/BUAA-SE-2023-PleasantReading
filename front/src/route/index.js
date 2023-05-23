import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../components/page/login/LoginComponent'
import RegisterComponent from '../components/page/login/RegisterComponent'
import BookDetail from '../components/veiw/book/BookDetail'
import PersonalCenter from '../components/page/PersonalCenter'
import InfoComponent from '../components/page/Personal/InfoComponent'
import Reader from 'components/page/Reader'
import MyBookBody from '../components/veiw/body/mybooks/MyBookBody'
import RankBody from '../components/veiw/rank/RankBody'
import MyComment from '../components/page/Personal/MyComment'
// import FantasyComponent from '../components/veiw/content/category/FantasyComponent'
// import HistoryComponent from '../components/veiw/content/category/HistoryComponent'
// import MartialComponent from '../components/veiw/content/category/MartialComponent'
// import CityComponent from '../components/veiw/content/category/CityComponent'
import Home from 'components/page/Home'
import AllBook from '../components/veiw/body/AllBook'//import HelloWorld from '../components/page/HelloWolrd'
import 'css/home.css'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      children: [
        {
          path: 'fantasy',
          name: 'fantasy'
        },
        {
          path: 'martial',
          name: 'martial'
        },
        {

          path: 'city',
          name: 'city'
        },
        {

          path: 'history',
          name: 'history'
        },
      ]
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
    // {
    //   path: '/reader',
    //   component: Reader,
    // },
    {
      path: '/reader/:bookid/:chapter',
      name: 'reader',
      component: Reader,
    }
    ,
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
    }

  ]
})
export default router