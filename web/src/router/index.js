import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => {
        return import('../views/Home.vue')
      },
      meta: { authRequired: true },
    },
    {
      path: '/sign-in',
      name: 'sign-in',
      component: () => import('../views/SignIn.vue'),
      meta: { authProhibited: true },
    },
    {
      path: '/register',
      name: 'register',
      component: (to, from, next) => {
        return import('../views/Register.vue')
      },
      meta: { authProhibited: true },
    },
  ]
})

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();

  if (to.meta.authRequired && !auth.isSignedIn) { return next({ name: 'sign-in' }); }
  else if (to.meta.authProhibited && auth.isSignedIn) { return next({ name: 'home' })}

  return next();
})


export default router
