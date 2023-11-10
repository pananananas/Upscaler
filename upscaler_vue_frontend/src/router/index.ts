import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UploadImageView from '../views/UploadImageView.vue'
import DisplayResultView from '../views/DisplayResultView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/display-result/:image_id',
    name: 'display-result',
    component: DisplayResultView,
    props: true
},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
