<template>


  <div>

    <div>
      <nav class="navbar navbar-light bg-light">
      <div class="container">

          <a class="navbar-brand" href="#">
            <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
          </a>

            <div class="col-md-3 text-end">
                <router-link to="/lk" class="btn btn-outline-primary me-2"> <i class="fa  fa-user" aria-hidden="true"></i> </router-link>
                <!-- <span v-if="!!currentUser">  <a href="#"  class="btn btn-primary" @click="">Выйти</a></span> -->
                <!-- <router-link to="/ntransport" class="btn btn-outline-primary me-2"> <i class="fa  fa-bicycle" aria-hidden="true"></i> </router-link> -->
                <router-link to="/cat" class="btn btn-outline-primary me-2"> <i class="fa  fa-folder-open" aria-hidden="true"></i> </router-link>
                <router-link to="/mo" class="btn btn-outline-primary me-2"> <i class="fa fa-cart-plus" aria-hidden="true"></i> </router-link>
            </div>

      </div>
      </nav>
      <div class="container-sm">
          <div class="row">
              <div class="col centered">
                  <i class="fa fa-bullseye" aria-hidden="true"></i>
                  <h1 class="h3 mb-3 fw-normal">Мой транспорт</h1>
                      <router-link to="/ntransport" class="btn btn-primary btn-lg">
                          Добавить
                        </router-link>
                <div>
                  <br>
                  <br>
        </div>


              </div>
          </div>
      </div>








    <div class="container-fluid transportback">
      <div class="album py-5 transparent">
        <div class="container transparent">
          <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3 transparent">
           <div class="col" v-for="transport in transports" :key="transport.id">

                  <div class="card shadow-sm">
                    <!-- <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Photo</title><rect width="100%" height="100%" fill="#55595c" ></rect></svg> -->
                    <div v-if="transport.image">
                      <img :src="`${transport.image}`" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                    </div>
                    <div v-else>
                      <img src="http://127.0.0.1:8000/media/imgTransport/default.jpg" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                    </div>
                    <div class="card-body">
                      <p class="card-text"> {{transport.transport_type}} - {{transport.transport_model}} </p>
                <p class="card-text">{{transport.information}} </p>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <!-- <button type="button" class="btn btn-sm btn-outline-secondary">Посмотреть</button> -->
                  <button type="button" class="btn btn-sm btn-outline-secondary" @click="$router.push(`/transportedit/${transport.id}`)">Редактировать</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" @click="delMyTransport(transport.id)">Удалить</button>
                  <!-- // "$router.push('/mtdelitcard')" -->
                </div>
                <small class="text-muted"></small>
                <!-- {{Занят/Свободен}} -->
                {{transport.status}}
              </div>
            </div>
          </div>
        </div>

      </div>  </div>
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
      manufactutrers: [],
      currentUser: {},
      transport_types: [],
      transports: [],
      transportBody:{
                transport_type: "",
                transport_model: "",
                manufacturer: "",
                year: "0",
                age_limit: "16",
                rental_price: "0",
                deposit: "0",
                information: ""
      }
    }
  },
   // ... методы
  methods: {
    getManufacturerData() {
      // const axios = require('axios').default
      axios.get('http://127.0.0.1:8000/api/manufacturer/',{
        headers:{
          'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
           }}).then((response) => {

           this.manufactutrers = [...response.data];
            // console.log(this.manufactutrers);
          //  this.results = response.data;
         }).catch((error) => {
          console.error(error);
        });

        },
    getTransportTypesData() {
          // const axios = require('axios').default
          axios.get('http://127.0.0.1:8000/api/transport_type/',{
            headers:{
              'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
              }}).then((response) => {

              this.transport_types = [...response.data];
                // console.log(this.transport_types);
              //  this.results = response.data;
            }).catch((error) => {
              console.error(error);
            });
        },
    getUserData() {
      // const axios = require('axios').default

      axios.get('http://127.0.0.1:8000/auth/users/me/',{
        headers:{
          'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
          //  Authorization: 'token [token]',
           }}).then((response) => {
          //  console.log(response.data);
           this.currentUser = {...response.data};
          //  console.log(this.currentUser.username);
         }).catch((error) => {
          console.error(error);
        });
        },
    getTransportsData() {
      // const axios = require('axios').default
      axios.get(`http://127.0.0.1:8000/api/mytransport/`, {
        headers:{
          'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
           }}).then((response) => {

           this.transports = [...response.data];
            // console.log(this.transports);
          //  this.results = response.data;
         }).catch((error) => {
          console.error(error);
        });
        },
    delMyTransport(id){
        axios.delete(`http://127.0.0.1:8000/api/transports/${id}`, {
           headers:{
           'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
        }})
        .then(response => {
          console.log(response);
          this.transports =  this.transports.filter(t=>t.id !== id);
          // console.log(response.data.full_name)

        })
        .catch(e => {
          this.errors.push(e)
         })
     },



},
mounted() {
  this.getManufacturerData();
  this.getTransportTypesData();
  this.getUserData();
  this.getTransportsData();


},
  }

</script>