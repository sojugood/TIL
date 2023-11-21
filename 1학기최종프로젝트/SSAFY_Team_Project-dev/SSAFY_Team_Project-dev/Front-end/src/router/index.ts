import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/bank',
      name: 'bank',
      component: () => import('../views/BankView.vue')
    },
    {
      path: '/ExchangeRate',
      name: 'ExchangeRate',
      component: () => import('../views/ExchangeRateView.vue')
    },
    {
      path: '/map',
      name: 'map',
      component: () => import('../views/MapView.vue')
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: () => import('../views/RecommendView.vue')
    },
    {
      path: '/article',
      name: 'article',
      component: () => import('../views/Article/ArticleView.vue')
    },
    {
      path: '/article/:id',
      name: 'articleDetail',
      component: () => import('../views/Article/ArticleDetailView.vue')
    },
    {
      path: '/article/post',
      name: 'article/post',
      component: () => import('../views/Article/MakeArticleView.vue')
    },
    {
      path: '/article/:id/put',
      name: 'article/Put',
      component: () => import('../views/Article/PutArticleView.vue')
    },
    {
      path: '/userInfo/:username',
      name: 'userInfo',
      component: () => import('../views/UserInfoView.vue')
    },
    {
      path: '/goldprice',
      name: 'goldprice',
      component: () => import('../views/GoldPriceView.vue')
    },
    {
      path: '/oilprice',
      name: 'oilprice',
      component: () => import('../views/OilPriceView.vue')
    },
    {
      path: '/kospi',
      name: 'kospi',
      component: () => import('../views/KospiView.vue')
    },
    {
      path: '/kosdaq',
      name: 'kosdaq',
      component: () => import('../views/KosdaqView.vue')
    },
    {
      path: '/krx',
      name: 'krx',
      component: () => import('../views/KrxView.vue')
    },
    {
      path: '/theme',
      name: 'theme',
      component: () => import('../views/ThemeView.vue')
    },
  ]
})

export default router
