<template>
  <div id="#app">
    <div>
      <nav class="navbar navbar-light bg-light">
        <div class="container">

          <a class="navbar-brand" href="#">
            <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
          </a>
              <div class="col-md-3 text-end">
                <router-link to="/lk" class="btn btn-outline-primary me-2"> <i class="fa  fa-user" aria-hidden="true"></i> </router-link>
                <!-- <span v-if="!!currentUser">  <a href="#"  class="btn btn-primary" @click="">Выйти</a></span> -->
                <router-link to="/ntransport" class="btn btn-outline-primary me-2"> <i class="fa  fa-bicycle" aria-hidden="true"></i> </router-link>
                <router-link to="/cat" class="btn btn-outline-primary me-2"> <i class="fa  fa-folder-open" aria-hidden="true"></i> </router-link>
                <router-link to="/mo" class="btn btn-outline-primary me-2"> <i class="fa fa-cart-plus" aria-hidden="true"></i> </router-link>
            </div>

        </div>
      </nav>
          <div class="container-sm">
              <div class="row">
                  <div class="col">

         <form @submit.prevent="postPost" type="reset" >
          <h1 class="h3 mb-3 fw-normal">Информация пользователя</h1>
          <div class="form-floating">
            <input type="text" class="form-control" id="login" placeholder="Имя пользователя" v-model="postBody.full_name">
            <label for="floatingInput">Ваше имя</label>
          </div>
                              <p></p>
                              <div class="form-floating">
            <input type="text" class="form-control" id="city" placeholder="Город" v-model="postBody.address" address>
            <label for="floatingInput">Ваш город</label>
          </div>
                              <p></p>
                              <div class="form-floating">
            <input type="text"  class="form-control" id="phone" placeholder="+7(---)-------" v-model="postBody.tel_number">
            <label for="floatingInput">Ваш телефон</label>
          </div>
              <p></p>
          <div class="form-floating">
            <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" v-model="postBody.email">
            <label for="floatingInput">Email</label>
          </div>
              <p></p>
          <div class="form-floating">
            <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="postBody.password">
            <label for="floatingPassword">Введите новый пароль</label>
          </div>
              <p></p>
          <button class="w-100 btn btn-lg btn-primary greenedtotal" type="submit">Сохранить</button>
          <p>


          </p>



        </form>


          </div>
          <div class="col">
          </div>

               </div>
          </div>
        </div>
        <div>
          <ul>

    </ul>
        </div>


          </div>
    </div>


  </div>

</template>




<script>
import axios from 'axios';



export default {


  data() {
    return {
      results: {},
      postBody:{ full_name: '',email: '', address:'', tel_number:'', username:'', password:''},
  }
  },
  methods: {
    getUserData() {
      // const axios = require('axios').default

      axios.get('http://127.0.0.1:8000/auth/users/me/',{
        headers:{
          'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
          //  Authorization: 'token [token]',
           }}).then((response) => {
           console.log(response.data);
           this.results = response.data;
           this.postBody.full_name=this.results.full_name
           this.postBody.address=this.results.address;
           this.postBody.tel_number=this.results.tel_number
           this.postBody.email=this.results.email;
           console.log( this.results )
         }).catch((error) => {
          console.error(error);
        });
},
    postPost : function () {
          console.log(this.postBody);
        axios.patch(`http://127.0.0.1:8000/auth/users/me/`, {

              "email": this.postBody.email,
              "full_name": this.postBody.full_name,
              "address": this.postBody.address,
              "tel_number": this.postBody.tel_number,
              // "username": this.results.username,
              "password": this.postBody.password,
        },{
           headers:{
          // 'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
        }})
        .then(response => {
          console.log(response);
          console.log(response.data.full_name)
          this.results = {...response.data};
        })
        .catch(e => {
          this.errors.push(e)
         })
       }
},
mounted() {
  this.getUserData();
}

}
</script>

