import Vue from 'vue'
import Router from 'vue-router'
import store from '../store/index.js'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Login from '../components/Login.vue'
import Lk from '../components/Lk.vue'
import Register from '../components/Register.vue'
import Editlk from '../components/Editlk.vue'
import Ntransport from '../components/Ntransport.vue'
import Mt from '../components/Mt.vue'
import Mo from '../components/Mo.vue'
import Cat from '../components/Cat.vue'


// import Order from '../components/Order.vue'
import MtDelitCard from '../components/MtDelitCard.vue'
// import OrderNew from '../components/OrderNew.vue'
import OrderNew2 from '../components/OrderNew2.vue'
import Ordersent from '../components/Ordersent.vue'
import TransportEdit from '../components/TransportEdit.vue'
import addTransport from '../components/addTransport.vue'
import moderators from '../components/moderators.vue'
import MsgEditTransport from '../components/MsgEditTransport.vue'
import TransportCard from '../components/TransportCard.vue'

Vue.use(Router)

// ...

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/lk',
      name: 'lk',
      component: Lk,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/editlk',
      name: 'editlk',
      component: Editlk,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/ntransport',
      name: 'ntransport',
      component: Ntransport,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/mt',
      name: 'mt',
      component: Mt,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/mo',
      name: 'mo',
      component: Mo,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/addtransport',
      name: 'addtransport',
      component: addTransport,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/cat',
      name: 'cat',
      component: Cat,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/transportcard/:id',
      name: 'transportCard',
      component: TransportCard,
      meta: {
        requiresAuth: true
      }
     },
    {
      path: '/mtdelitcard',
      name: 'mtdelitcard',
      component: MtDelitCard,
      meta: {
        requiresAuth: true
      }
    },
    // {
    //   path: '/ordernew/:id',
    //   name: 'ordernew',
    //   component: OrderNew
    // },
    {
      path: '/ordernew2/:id',
      name: 'ordernew2',
      component: OrderNew2,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/ordersent',
      name: 'ordersent',
      component: Ordersent,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/transportedit/:id',
      name: 'transportedit',
      component: TransportEdit,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/moderators',
      name: 'moderators',
      component: moderators,
      meta: {
        requiresAuth: true,
        is_staff: true
      }
    },
    {
      path: '/msgedittransport',
      name: 'msgedittransport',
      component: MsgEditTransport,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})



// ...

const is_staff = localStorage.getItem('is_staff');

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      console.log('to', to);

      if(to.name == 'moderators' && !is_staff){
        next('/lk')
        return
      }

      if(to.name == 'lk' && is_staff){
        console.log('MODERAOTR',is_staff);
        next('/moderators')
        // next('/moderators#content-1')
        return
      }


      next()
      return
    }else{
      next('/login')
    }
  } else {
    next()
  }
})

// ...

export default router