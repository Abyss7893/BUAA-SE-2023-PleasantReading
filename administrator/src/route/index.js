import { createRouter,createWebHistory} from 'vue-router'
import LoginComponent from '../components/LoginComponent'
import BookManagement from '../components/BookManagement'
const router = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            name:'login',
            component:LoginComponent
        },
        {
            path:'/manage',
            name:'manage',
            component:BookManagement
        }
    ]
})
export default router