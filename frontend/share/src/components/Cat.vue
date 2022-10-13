<template>

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
                <!-- <router-link to="/cat" class="btn btn-outline-primary me-2"> <i class="fa  fa-folder-open" aria-hidden="true"></i> </router-link> -->
                <router-link to="/mo" class="btn btn-outline-primary me-2"> <i class="fa fa-cart-plus" aria-hidden="true"></i> </router-link>
            </div>

      </div>
        </nav>

        <nav class="navbar navbar-expand-md navbar-dark fixed-middle greenedtotal">
          <div class="container-fluid">
                    <form class="d-flex">
                <span class="selectbox">
                <select id="transport_type" class="form-control me-2" v-model="typeSort">
                  <option  value="">Весь транспорт ...</option>
                  <option v-for="typ in transport_types" :key="typ.id" :value="typ.name">{{typ.name}}</option>

                </select> </span>
            <span class="selectbox">
                      <select id="agegroup" v-model="sortAge" class="form-control me-2">
                          <option value="">Любой возраст&hellip;</option>
                          <option value="5">до 5 лет</option>
                          <option value="12">до 12 лет</option>
                          <option value="16">до 16 лет</option>
                          <option value="18">от 16 лет</option>
                      </select>
                      </span>
                      <span class="selectbox">
                      <select id="pricefrom" v-model="sortPriceFrom" class="form-control me-2">
                          <option value="">Цена от&hellip;</option>
                          <option value="100">100</option>
                          <option value="300">300</option>
                          <option value="500">500</option>
                          <option value="1000">1000</option>
                      </select>
                      </span>
                      <span class="selectbox">
                      <select id="priceupto" v-model="sortPriceUpTo" class="form-control me-2">
                          <option value="">Цена до&hellip;</option>
                          <option value="200">200</option>
                          <option value="300">300</option>
                          <option value="500">500</option>
                          <option value="1000">1000</option>
                      </select>
            </span>
             <!-- class="selectbox"> -->
                      <button class="btn btn-outline-success" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                    </form>
           </div>

        </nav>


          <div class="album py-5 bg-light">
            <div class="container greened-gradient">

              <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            <!-- <!одинаковые карточки транспорта при владелец=юзер видна кнопка редактировать иначе видна кнопка заказать> -->
                <div class="col" v-for="transport in sortedTransportWithPriceUpTo" :key="transport.id">

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
                           <button type="button" class="btn btn-sm btn-outline-secondary"
                          @click="$router.push(`/transportcard/${transport.id}`)"
                           >Подробнее</button>
                          <button type="button" class="btn btn-sm btn-outline-secondary"
                          @click="$router.push(`/ordernew2/${transport.id}`)"
                           >Заказать</button>

                          <!-- <button type="button" @click="orderSent" class="btn btn-sm btn-outline-secondary">Заказать</button> -->
                          <!-- <router-link to="/ordernew" class="btn btn-sm btn-outline-secondary" >Заказать</router-link> -->
                        </div>
                        <small class="text-muted">Цена: {{transport.rental_price}}</small>
                      </div>
                    </div>
                  </div>
                </div>







                </div>

        </div>
      </div>
    </div>
  <!-- </div> -->

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
      },
      typeSort:'',
      sortAge: "",
      sortPriceFrom: "",
      sortPriceUpTo: "",
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
      axios.get(`http://127.0.0.1:8000/api/transports/`, {
        headers:{
          'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
           }}).then((response) => {

           this.transports = [...response.data];
          //  console.log(this.transports);

          //  this.results = response.data;
         }).catch((error) => {
          console.error(error);
        });},


    postTransport : function () {
          // console.log(this.postBody);
          // console.log(this.transport_owner);
          // console.log(this.currentUser.id);

        axios.post(`http://127.0.0.1:8000/api/transports/`, {
                    "transport_owner": this.currentUser.id,
                    "age_limit": this.transportBody.age_limit,
                    "information": this.transportBody.information,
                    "rental_price": this.transportBody.rental_price,
                    "deposit": this.transportBody.deposit,
                    "year": this.transportBody.year,
                    "transport_model": this.transportBody.transport_model,
                    "transport_type": this.transportBody.transport_type,
                    "manufacturer": this.transportBody.manufacturer,
        },{
           headers:{
          // 'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
        }})
        .then(response => {
          // console.log(response);
          // console.log(response.data.full_name)
          this.results = {...response.data};
        })
        .catch(e => {
          this.errors.push(e)
         })
       }
},
computed:{
  sortedTransports(){
    return [...this.transports].filter(transport =>{

      return transport.transport_type.toLowerCase().includes(this.typeSort.toLowerCase())
    })
  },
  sortedTransportsWithAge(){
    return this.sortedTransports.filter(transport =>{

      switch(this.sortAge){
        case '5':
          console.log('5');
          return transport.age_limit <= 5

        case '12':
          console.log('12');
          return transport.age_limit <= 12

        case '16':
          console.log('16');
          return transport.age_limit <= 16

        case '18':
          console.log('18');
          return transport.age_limit >= 18

        default:
          return true
      }


    })
  },
  sortedTransportWithPriceFrom(){
    return this.sortedTransportsWithAge.filter(transport =>{

      switch(this.sortPriceFrom){
        case '100':
          console.log('100');
          return transport.rental_price >= 100

          case '300':
            console.log('300');
            return transport.rental_price >= 300

          case '500':
            console.log('500');
            return transport.rental_price >= 500

          case '1000':
            console.log('1000');
            return transport.rental_price >= 1000

          default:
            return true
      }
    })
  },
  sortedTransportWithPriceUpTo(){
    return this.sortedTransportWithPriceFrom.filter(transport =>{

      switch(this.sortPriceUpTo){
        case '100':
          console.log('100');
          return transport.rental_price <= 100

          case '300':
            console.log('300');
            return transport.rental_price <= 300

          case '500':
            console.log('500');
            return transport.rental_price <= 500

          case '1000':
            console.log('1000');
            return transport.rental_price <= 1000

          default:
            return true
      }
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