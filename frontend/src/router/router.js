import GeneralPage from "@/pages/GeneralPage";
import {createRouter, createWebHistory} from "vue-router";
import RegistrationPage from "@/pages/RegistrationPage";

const routes = [
    {
      path: '/',
      component: GeneralPage
    },
    {
        path: '/registration',
        component: RegistrationPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;