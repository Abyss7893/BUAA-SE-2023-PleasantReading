import { createRouter, createWebHistory } from 'vue-router'
import LoginComponent from '../components/page/login/LoginComponent'
import RegisterComponent from '../components/page/login/RegisterComponent'
import BookDetail from '../components/book/BookDetail'
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
    }

  ]
})
export default router