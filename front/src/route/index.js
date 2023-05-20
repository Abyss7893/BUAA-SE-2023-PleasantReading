import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../components/page/login/LoginComponent'
import RegisterComponent from '../components/page/login/RegisterComponent'
import BookDetail from '../components/book/BookDetail'
import PersonalCenter from '../components/page/PersonalCenter'
import InfoComponent from '../components/page/InfoComponent'
import Reader from 'components/page/Reader'
import MyBookBody from '../components/veiw/body/mybooks/MyBookBody'
// import FantasyComponent from '../components/veiw/content/category/FantasyComponent'
// import HistoryComponent from '../components/veiw/content/category/HistoryComponent'
// import MartialComponent from '../components/veiw/content/category/MartialComponent'
// import CityComponent from '../components/veiw/content/category/CityComponent'
import Home from 'components/page/Home'

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
        }

      ]
    },
    {
      path: '/reader',
      component: Reader,
    }
    ,
    {
      path: '/mybook',
      component: MyBookBody,
      name: 'mybook',
    }

  ]
})
export default router