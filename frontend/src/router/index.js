import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/pages/Home.vue'
import TopOperadoras from '@/pages/TopOperadoras.vue'
import BuscaOperadoras from '@/pages/BuscaOperadoras.vue'

const routes = [
    { path: '/', component: Home },
    { path: '/top-operadoras', component: TopOperadoras },
    { path: '/buscar-operadoras', component: BuscaOperadoras },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
