import { createRouter,createWebHistory} from 'vue-router'
import LoginComponent from '../components/LoginComponent'
const router = createRouter({
    history: createWebHistory(),
    routes:[
        {
            path:'/',
            name:'login',
            component:LoginComponent
        }
    ]
})
export default router