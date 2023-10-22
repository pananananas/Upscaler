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
    path: '/upload-image',
    name: 'upload-image',
    component: UploadImageView,
  },
  {
    path: '/display-result',
    name: 'display-result',
    component: DisplayResultView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
