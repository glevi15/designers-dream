import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Projects from './views/Projects'
import NewProject from './views/NewProject'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: Dashboard
        },
        {
            path: '/projects',
            name: 'projects',
            component: Projects
            
        },
        {
            path: '/newproject',
            name: 'newproject',
            component: NewProject
            
        }
    ]
})