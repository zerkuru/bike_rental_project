<template>
 <div>

   <div>

        <nav class="navbar navbar-light bg-light">
        <div class="container">

          <a class="navbar-brand" href="/">
            <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
          </a>

            <div class="col-md-3 text-end">

              <router-link to="/register" class="btn btn-primary"><i class="fa fa-user-circle-o" aria-hidden="true"></i>Регистрация</router-link>
            </div>

        </div>
      </nav>
      <main class="form-signin">
          <div class="container-sm">
              <div class="row">
          <div class="col">
          </div>


          <div class="col">
              <form class="login" @submit.prevent="login">
          <i class="fa fa-bullseye" aria-hidden="true"></i>
          <h1 class="h3 mb-3 fw-normal">Вход</h1>
          <div class="form-floating">
            <input required v-model="username"  class="form-control" type="username" placeholder="Введите ваш логин"/>

            <label for="floatingInput">Ваше имя</label>
          </div>
          <div class="form-floating">
            <input required v-model="password" type="password" class="form-control" placeholder="Введите ваш пароль"/>
            <label for="floatingPassword">Пароль</label>
          </div>

          <div class="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me"> Запомнить меня
            </label>
          </div>
          <button class="w-100 btn btn-lg btn-primary greenedtotal" type="submit">Войти</button>
          <p class="mt-5 mb-3 text-muted">&copy; 2022 Bike&Scooter</p>
        </form>
          </div>
          <div class="col">
          </div>
        </div>

          </div>
      </main>
   </div>
 </div>
</template>


<script>
import axios from 'axios';

  export default {
    data() {
      return {
        username: "",
        password: ""
      }
    },

    // ... методы
    methods: {
      async getUserData() {
      await axios.get('http://127.0.0.1:8000/auth/users/me/',{
        headers:{
          'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
          //  Authorization: 'token [token]',
           }}).then((response) => {
            console.log(response.data);

            if(response.data.is_staff){
              console.log('You are admin!!!');
              localStorage.setItem('is_staff', 1);
            }else{
              localStorage.removeItem('is_staff');
            }

           window.location.href="/lk"


          // this.currentUser = {...response.data};
          //  console.log(this.currentUser.username);
         }).catch((error) => {
          console.error(error);
        });
        },

      login: function() {
        let username = this.username
        let password = this.password
        this.$store.dispatch('login', { username, password })
          .then(async () => {
           await this.getUserData();
          })
          .catch(err => console.log(err))
      }
    }
  }
</script>