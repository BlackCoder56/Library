import { createRouter, createWebHistory } from 'vue-router'
import AllBooksView from '@/views/AllBooksView.vue'

const routes = [
  {
    path: '/',
    name: 'book',
    component:AllBooksView
  },
  {
    path: '/addbook',
    name: 'addbook',
    component: () => import('@/views/AddBookFormView.vue')
  }
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
