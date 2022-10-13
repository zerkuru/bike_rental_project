<template>
  <div>
    <nav class="navbar navbar-light bg-light">
        <div class="container">
          <a class="navbar-brand" href="#">
      <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
          </a>
          <div class="col-md-3 text-end">
                <router-link to="/lk" class="btn btn-outline-primary me-2"> <i class="fa  fa-user" aria-hidden="true"></i> </router-link>
                <router-link to="/ntransport" class="btn btn-outline-primary me-2"> <i class="fa  fa-bicycle" aria-hidden="true"></i> </router-link>
                <router-link to="/cat" class="btn btn-outline-primary me-2"> <i class="fa  fa-folder-open" aria-hidden="true"></i> </router-link>
          </div>
        </div>
    </nav>
    <br>
    <div class="container-sm">
        <div class="row">
            <div class="col centered">
                <i class="fa fa-bullseye" aria-hidden="true"></i><br>
            </div><br>
         </div>
    </div>
    <br>
    <div class="container-fluid greened-gradient">
        <div class="row">
          <div class="col"></div>
          <div class="col">
              <div class="form card bg-light border-grey usermargin">
                  <br>
                  <div class="card-lg bg-light text-dark border-grey usermargin">
                      <br>
                      <div class="container-sm centered" >
                          <div class="container-sm centered">
                              <div class="container-sm centered">
                                  <div class="container-sm centered">
                                      <div v-if="transportBody.image">
                                          <img :src="`${transportBody.image}`" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                                      </div>
                                      <div v-else>
                                        <img src="http://127.0.0.1:8000/media/imgTransport/default.jpg" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                                      </div>
                                  </div>
                              </div>
                          </div>
                      </div>
                  </div>
                  <div class="card-body">
                      <!-- <p class="card-text"> -->
                          <h4 class="greened">
                            <!-- Велосипед горный GIANT A31 -->
                            {{transportBody.transport_model}}
                            <!-- <!{{transport name}}> -->

                            </h4>
                          <!-- Велосипед горный -->
                          {{transportBody.transport_type}}
                          <!-- <!{{transport type}}> -->
                          <br>
                          Модель:
                          <!-- Giant A31 -->
                          {{transportBody.manufacturer}}
                          <!-- <!{{transport model}}> -->
                          <br>
                          Год выпуска:
                          <!-- 2021 -->
                          {{transportBody.year}}
                          <!-- <!{{transport date}}> -->
                          <br>
                      <!-- </p> -->
                      <hr>
                      Возраст:
                       <!-- с 16 лет -->
                       {{transportBody.age_limit}}
                      <!-- <!{{transport age}}><br> -->
                      Дополнительно:<br>
                      <p class="card-text greened">
                        <!-- Есть багажник, шлем в комплекте -->
                        {{transportBody.information}}
                          <!-- <!{{transport info}}> -->
                      </p>
                      <br>
                      <div class="card greenedtotal text-light centered">
                          <h4 class="text-white">
                          Стоимость аренды:
                          <!-- 2000 -->
                           {{transportBody.price}}
                          <!-- <!{{transport price}}> -->
                          <br>
                              Залог:
                              <!-- 4000 -->
                               {{transportBody.deposit}}
                              <!-- <!{{transport deposit}}> -->
                          </h4>

                      </div>
                      <br>
                      <hr>
                      <h4 class="h6 mb-3 fw-normal greyed">ВЛАДЕЛЕЦ</h4>
                      <div class="form-floating transparent">
                          <!-- Иванов Андрей -->
                           {{transportBody.transport_owner}}
                            <!-- <!{{owner name}}> -->
                      </div>
                      <div class="form-floating transparent">
                          <!-- +7(904)5354434 -->
                           {{transportBody.transport_owner_phone}}
                          <!-- <!{{owner phone}}> -->
                      </div>
                      <div class="form-floating transparent">
                          <!-- Тверь -->
                           {{transportBody.address}}
                          <!-- <!{{owner address}}> -->
                      </div>
                      <div class="form-floating transparent">
                         {{transportBody.transport_owner_email}}
                          <!-- ivanovtver@mail.ru -->
                      </div>
                      <br>
                  </div>
              </div>  <br>
            <br>
          </div>   <br>
          <div class="col"></div>
        </div>  <br>
    </div> <br>
  </div>



</template>




<script>
import axios from 'axios';
// import moment from 'moment';

  export default {
    props:['id'],

    data() {
       return {
        order: {
            datefrom: '',
            timefrom: '',
            dateto: '',
            timeto: '',
            conditions:'',
            transport: ''

        },
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
    sendOrder(){

    //     "date_from": [
    //     "Обязательное поле."
    // ],
    // "date_to": [
    //     "Обязательное поле."
    // ],
    // "conditions": [
    //     "Обязательное поле."
    // ],
    // "transport": [
    //     "Обязательное поле."
    // ]
        console.log(this.order);
        let date_from = new Date(this.order.datefrom + " " + this.order.timefrom);
        console.log('date_from', date_from);
        let date_to = new Date(this.order.dateto + " " + this.order.timeto);
        console.log('date_to', date_to);
        let order_transport = this.$route.params.id;
        console.log(order_transport);
        let order_conditions = this.order.conditions;
        console.log('conditions', order_conditions);

        axios.post(`http://127.0.0.1:8000/api/orders/`,{
                date_from,
                date_to,
                transport: order_transport,
                conditions: order_conditions

        },
        {

           headers:{
            // 'Content-Type': 'multipart/form-data',
            Authorization: `token ${localStorage.getItem('token')}`,
        }})
        .then(response => {
          console.log(response);
            this.$router.push('/ordersent')

          //this.results = {...response.data};
        })
        .catch(e => {
          this.errors.push(e)
         })
    },
    // uploadImg(event){
    //   //this.uploadImage = this.$refs.upImg.file.files[0];
    //   this.uploadImage = event.target.files[0];
    //         },
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
        //    console.log(response.data);

        //   console.log(response.data);

          let manArr = this.manufactutrers.find(m=> m.name == response.data.manufacturer);
          let typeArr  = this.transport_types.find(m=> m.name == response.data.transport_type);
          this.transportBody = {...response.data,
          manufacturer: manArr.id, transport_type: typeArr.id
          };

        // console.log(manArr.id);
        // console.log(typeArr.id);
          console.log(this.transportBody);
         }).catch((error) => {
          console.error(error);
        });
            },

    postTransport : function () {
          // console.log(this.postBody);
          const formData = new FormData();
          // console.log(this.currentUser.id);
          // console.log(this.currentUser.username);
          // console.log(this.currentUser.full_name);
          // formData.append({...postBody, 'image': this.uploadImage});

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

          // for (let pair of formData.entries()) {
          //   console.log(pair[0]+ ', ' + pair[1]);
          // }

        axios.post(`http://127.0.0.1:8000/api/transports/`,

                    // "transport_owner": this.currentUser.id,
                    // "age_limit": this.transportBody.age_limit,
                    // "information": this.transportBody.information,
                    // "rental_price": this.transportBody.rental_price,
                    // "deposit": this.transportBody.deposit,
                    // "year": this.transportBody.year,
                    // "transport_model": this.transportBody.transport_model,
                    // "transport_type": this.transportBody.transport_type,
                    // "manufacturer": this.transportBody.manufacturer,
                    // // "image":
                    formData,
                    this.$router.push('/mt'),
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
  console.log(this.$route.params.id)
  this.getTransportByID();
},

}
</script>