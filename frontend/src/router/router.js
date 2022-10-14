import GeneralPage from "@/pages/GeneralPage";
import {createRouter, createWebHistory} from "vue-router";
import RegistrationPage from "@/pages/RegistrationPage";
import PostPage from "@/pages/PostPage";
import UserPage from "@/pages/UserPage";

const routes = [
    {
      path: '/',
      name: "Home",
      component: GeneralPage
    },
    {
        path: '/registration',
        component: RegistrationPage
    },
    {
        path: '/posts',
        component: PostPage
    },
    {
        path: '/myprofile',
        component: UserPage
    },

]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

router.beforeEach((to, from, next) => {
    if (localStorage.getItem('token')) {
        next()
    } else if (to.path === '/') {
        next()
    } else {
        next({name: 'Home'})
    }
})

export default router;