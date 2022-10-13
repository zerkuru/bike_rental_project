<template>

  <div>

    <div>
       <nav class="navbar navbar-light bg-light">
  <div class="container">

    <a class="navbar-brand" href="/">
      <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
    </a>

      <div class="col-md-3 text-end">
        <router-link to="/lk" class="btn btn-outline-primary me-2"> <i class="fa fa-user-circle" aria-hidden="true"></i> </router-link>

      </div>

  </div>
</nav>
<main class="form-signin">
    <div class="container-sm">
         <div class="row">
    <div class="col">
    </div>
    <div class="col">
        <form @submit.prevent="register">
    <i class="fa fa-bullseye" aria-hidden="true"></i>
    <h1 class="h3 mb-3 fw-normal">Регистрация</h1>
    <div class="form-floating">
      <input type="text" class="form-control" id="username" placeholder="Имя пользователя" v-model="username" required autofocus>
      <label for="floatingInput">Ваше имя</label>
    </div>
    <div class="form-floating">
      <input type="email" class="form-control" id="email" placeholder="name@example.com"  v-model="email" required>
      <label for="floatingInput">Email</label>
    </div>
    <div class="form-floating">
      <input  class="form-control" id="password" placeholder="Password" type="password" v-model="password" required>
      <label for="password">Пароль</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="password-confirm" placeholder="Password" v-model="password_confirmation" required>
      <label for="floatingPassword">Повторите пароль</label>
    </div>

    <div class="checkbox mb-3">
      <label>
        <input type="checkbox" value="remember-me"> Запомнить меня
      </label>
    </div>
    <button class="w-100 btn btn-lg btn-primary greenedtotal" type="submit">Зарегистрироваться</button>
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
  export default {
    data() {
      return {
        username: "",
        email: "",
        password: "",
        password_confirmation: "",
        is_admin: null
      }
    },

    // ... методы
    methods: {
      register: function() {
        let data = {
          username: this.username,
          email: this.email,
          password: this.password,
          is_admin: this.is_admin
        }

        this.$store.dispatch('register', data)
          .then(() => this.$router.push("/login"))
          .catch(err => console.log(err))
      }
    }
  }
</script>