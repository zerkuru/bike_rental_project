<template>
  <div>


    <div class="text-center">
        <nav class="navbar navbar-light bg-light">
          <div class="container">
            <a class="navbar-brand" href="/">
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
       <main class="form">
        <div class="container-sm">
            <div class="row">
        <div class="col">
        </div>
        <div class="col">
            <form @submit.prevent="editTransport" enctype="multipart/form-data">
        <i class="fa fa-bullseye" aria-hidden="true"></i>
        <h1 class="h3 mb-3 fw-normal">Редактировать транспорт</h1>
        <div class="form-floating">
          <input type="text" class="form-control" placeholder="Велосипед горный" v-model="transportBody.transport_model">


           <label for="floatingInput">Наименование транспорта</label>
        </div>
        <div class="form-floating">


          <select class="form-control"  v-model="transportBody.transport_type">

                <option disabled>Выберите тип транспорта</option>
                <option v-for="typ in transport_types" :value="typ.id" :key="typ.id">{{ typ.name}}</option>
           </select>
           <label for="floatingInput">Тип транспорта</label>
        </div>

        <div class="form-floating">

             <select class="form-control" v-model="transportBody.manufacturer">
                <option disabled>Выберите производителя</option>
                <option v-for="man in manufactutrers" :value="man.id" :key="man.id">{{ man.name}}</option>
            </select>
            <label for="floatingInput">Модель транспорта</label>
        </div>


        <div class="form-floating">
          <input type="number" class="form-control" id="year" placeholder="2013" v-model="transportBody.year">
          <label for="floatingInput">Год выпуска</label>
        </div>
        <div class="form-floating">
          <input type="number" class="form-control" id="age_limit" placeholder="16" v-model="transportBody.age_limit">
          <label for="floatingInput">Возрастное ограничение</label>
        </div>
        <div class="form-floating">
          <input type="text" class="form-control" id="information" placeholder="16" v-model="transportBody.information">
          <label for="floatingInput">Дополнительная информация</label>
        </div>
        <div class="form-floating">
          <input type="number" class="form-control" id="rental_price" placeholder="16" v-model="transportBody.rental_price">
          <label for="floatingInput">Стоимость аренды</label>
        </div>
        <div class="form-floating">
          <input type="number" class="form-control" id="deposit" placeholder="16" v-model="transportBody.deposit">
          <label for="floatingInput">Залог</label>
        </div>
        <div class="form-floating">
          <input type="file" class="form-control"  ref="upImg" @change="uploadImg($event)">
          <label for="floatingInput">Выберите изображение</label>
        </div>

        <button class="w-100 btn btn-lg btn-primary greenedtotal" type="submit">Сохранить</button>
        <!-- <router-link to="/msgedittransport" class="btn btn-lg btn-primary greenedtotal">Редактировать</router-link> -->
        <button class="w-100 btn btn-outline-primary me-2" type="reset">Очистить</button>

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
    props:['id'],

    data() {
       return {
      results: {},
      manufactutrers: [],
      currentUser: {},
      transport_types: [],
       transportBody:{
                transport_type: "",
                transport_model: "",
                manufacturer: "",
                year: "0",
                age_limit: "16",
                rental_price: "0",
                deposit: "0",
                information: "",
                image: ''
      },
      uploadImage:''
    }
  },
   // ... методы
  methods: {
    uploadImg(event){
      //this.uploadImage = this.$refs.upImg.file.files[0];
      this.uploadImage = event.target.files[0];
            },
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
        });},
    getUserData() {
      // const axios = require('axios').default

      axios.get('http://127.0.0.1:8000/auth/users/me/',{
        headers:{
          'Content-Type': 'applicatios/json',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
          //  Authorization: 'token [token]',
           }}).then((response) => {
           //console.log(response.data);
           this.currentUser = {...response.data};
          //  console.log(this.currentUser);
         }).catch((error) => {
          console.error(error);
        });
            },
     getTransportByID() {
      // const axios = require('axios').default

      axios.get(`http://127.0.0.1:8000/api/transports/${this.$route.params.id}`,{
        headers:{
          'Content-Type': 'applicatios/json',

            Authorization: `token ${localStorage.getItem('token')}`,

           }}).then((response) => {
           //console.log(response.data);

          console.log(response.data);

          let manArr = this.manufactutrers.find(m=> m.name == response.data.manufacturer);
          let typeArr  = this.transport_types.find(m=> m.name == response.data.transport_type);
          this.transportBody = {...response.data, manufacturer: manArr.id, transport_type: typeArr.id};

        // console.log(manArr.id);
        // console.log(typeArr.id);
        //   console.log(this.transportBody);
         }).catch((error) => {
          console.error(error);
        });
            },

    editTransport : function () {

          const formData = new FormData();

          formData.append("transport_owner", this.currentUser.username);
          formData.append("transport_model", this.transportBody.transport_model);
          formData.append("year", this.transportBody.year);
          formData.append("age_limit", this.transportBody.age_limit);
          formData.append("information", this.transportBody.information);
          formData.append("rental_price", this.transportBody.rental_price);
          formData.append("deposit", this.transportBody.deposit);
          formData.append("image", this.uploadImage);
          formData.append("transport_type", this.transportBody.transport_type)
          formData.append("manufacturer", Number(this.transportBody.manufacturer));


        axios.put(`http://127.0.0.1:8000/api/transports/${this.$route.params.id}/`, formData,
        {
           headers:{
            'Content-Type': 'multipart/form-data',
           //Authorization: 'token db85794c69d1203bb0e2eac613e91aefcbb005c1',
            Authorization: `token ${localStorage.getItem('token')}`,
        }})
        .then(response => {
          // console.log(response);
          // console.log(response.data.full_name)
          console.log(formData)
          this.results = {...response.data};
          this.$router.push('/mt')
        })
        .catch(e => {
          this.errors.push(e)
         })
       }
},
mounted() {
  this.getManufacturerData();
  this.getTransportTypesData();
  this.getUserData();
  // console.log(this.$route.params.id)
  this.getTransportByID();
},

}
</script>>