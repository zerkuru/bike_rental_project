import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {}
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,

  },
  mutations: {
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, payload) {
      state.status = 'success'
      state.token = payload.token
      state.user = payload.user
    },
    auth_error(state) {
      state.status = 'error'
    },
    logout(state) {
      state.status = ''
      state.token = ''
    },

  },
  actions: {
    // ... авторизация
    login({commit}, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:8000/auth/token/login/', data: user, method: 'POST' })
        .then(resp => {
          console.log('login', resp);
          const token = resp.data.auth_token
          const user = resp.data.user

          localStorage.setItem('token', token)
          localStorage.setItem('user', user)
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', { token: token, user: user })
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error')
          localStorage.removeItem('token')
          reject(err)
        })
      })
    },
    // ... регистрация
    register({commit}, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        axios({ url: 'http://localhost:8000/auth/users/', data: user, method: 'POST' })
        .then(resp => {
          console.log('REG',resp);
          const token = resp.data.auth_token
          const user = resp.data.user

          localStorage.setItem('token', token)
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', { token: token, user: user })
          resolve(resp)
        })
        .catch(err => {
          commit('auth_error', err)
          localStorage.removeItem('token')
          reject(err)
        })
      })
    },
      // ... редактирование пользователя
      // editusers({commit}, user) {
      //   return new Promise((resolve, reject) => {
      //     commit('auth_request')
      //     axios({ url: 'http://localhost:8000/auth/users/', data: user, method: 'POST' })
      //     .then(resp => {
      //       const token = resp.data.token
      //       const user = resp.data.user

      //       localStorage.setItem('token', token)
      //       axios.defaults.headers.common['Authorization'] = token
      //       commit('auth_success', { token: token, user: user })
      //       resolve(resp)
      //     })
      //     .catch(err => {
      //       commit('auth_error', err)
      //       localStorage.removeItem('token')
      //       reject(err)
      //     })
      //   })
      // },
    // ...выход
    logout({commit}) {
      return new Promise((resolve, reject) => {
        console.log(resolve, reject)
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    }
  },
  modules: {

  }
})



