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

        <div class="container-fluid greened-gradient" >
        <p></p>
                <div class="container-fluid orderbackground rounded">
                    <div class="container-md transparent">
                        <p> </p>
                        <p>
                        </p>
                    </div>
                    <div class="container-md">
                        <form @submit.prevent="sendOrder">
                            <div container-md centered whitened>
                                <br>
                                <p class="centered">
                                    <i class="fa fa-bullseye centered" aria-hidden="true">
                                    </i>
                                    <h1 class="h3 mb-3 fw-normal whitened centered">Заказ</h1>
                                </p>
                                        <!-- <!транспорт> -->
                            </div>
                            <div class="container-md rounded orderform">
                                <div class="row">
                                    <div class="col-md">
                                        <div class="row">
                                            <div class="col-sm">
                                                <h4 class="h6 mb-3 fw-normal greened">ТРАНСПОРТ</h4>
                                                <div class="form-floating transparent">
                                                    <!-- Велосипед -->
                                                     {{transportBody.transport_model}}
                                                </div>

                                                <div class="form-floating transparent">
                                                    <!-- Giant AX14 -->
                                                    модель: {{transportBody.manufacturer}}
                                                </div>

                                                <div class="form-floating transparent">
                                                    <!-- 16 -->
                                                    от {{transportBody.age_limit}} лет
                                                </div>
                                                <br>
                                            </div>
                                            <div class="col-sm">
                                                <h4 class="h6 mb-3 fw-normal greened">ВЛАДЕЛЕЦ</h4>

                                                <div class="form-floating transparent">
                                                    <!-- Иванов Андрей -->
                                                      {{transportBody.transport_owner}}
                                                </div>

                                                <div class="form-floating transparent">
                                                    <!-- +7(904)5354434 -->
                                                     {{transportBody.transport_phone}}
                                                </div>

                                                <div class="form-floating transparent">
                                                    <!-- Тверь -->
                                                     {{transportBody.transport_address}}
                                                </div>

                                                <div class="form-floating transparent">
                                                    <!-- ivanovtver@mail.ru -->
                                                    {{transportBody.transport_email}}
                                                </div>
                                                <br>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md rightened">
                                        <h3 class="h5 mb-3 fw-normal greened">ЗАКАЗЧИК</h3>
                                        <div class="form-floating transparent">
                                            <!-- Петренко Лидия -->
                                            {{currentUser.full_name}}
                                        </div>

                                        <div class="form-floating transparent">
                                            <!-- +7(931)2348182 -->
                                             {{currentUser.tel_number}}
                                        </div>

                                        <div class="form-floating transparent">
                                            {{currentUser.email}}
                                        </div>
                                        <p></p>
                                    </div>
                                </div>
                            </div>
                            <div class="container-md border border-light rounded">
                                <h3 class="h5 mb-3 fw-normal greened">АРЕНДА</h3>
                                <p></p>
                                <div class="row">
                                    <div class="col">
                                        <h5 class="h6 mb-3 fw-normal greened">НАЧАЛО</h5>
                                        <p></p>
                                        <div class="form-floating">
                                            <div class="flex row">
                                                <div class="col">
                                                    <div class="flex row">
                                                        <div class="col rightened">
                                                            <label for="floatingInput"  class="greened">Дата </label>
                                                        </div>
                                                        <div class="col rightened">
                                                    <input type="date" class="form-control transparent" id="datefrom" v-model="order.datefrom">
                                                    </div>
                                                    </div>
                                                    <br>
                                                </div>
                                                <div class="col">
                                                    <div class="flex row">
                                                        <div class="col rightened">
                                                            <label for="floatingInput" class="greened">время</label>
                                                        </div>
                                                        <div class="col rightened">
                                                            <input type="time" class="form-control transparent" id="timefrom" v-model="order.timefrom" >
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                            <p></p>
                                        <h5 class="h6 mb-3 fw-normal greened">ОКОНЧАНИЕ</h5>
                                        <p></p>
                                        <div class="form-floating">
                                            <div class="flex row">
                                                <div class="col">
                                                    <div class="flex row">
                                                <div class="col rightened">
                                                    <label for="floatingInput"  class="greened">Дата </label>
                                                    </div>
                                                <div class="col rightened">
                                                    <input type="date" class="form-control transparent" id="dateto" v-model="order.dateto">
                                                </div>
                                                </div>
                                                    <br>
                                                </div>
                                                <div class="col">
                                                    <div class="flex row">
                                                <div class="col rightened">
                                                    <label for="floatingInput" class="greened">время</label>
                                                </div>
                                                <div class="col rightened">
                                                    <input type="time" class="form-control transparent" id="timeto" v-model="order.timeto">
                                                </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <br>
                                    </div>
                                    <div class="col">
                                        <h5 class="h6 mb-3 fw-normal greened">КОММЕНТАРИЙ</h5>
                                        <div class="flex form-floating">
                                            <!-- </label> -->
                                            <input type="text" class="form-control" id="comment" placeholder="Комментарий" v-model="order.conditions">
                                            <br>
                                            <br>
                                            <br>
                                            <br>
                                            <br>
                                        </div>
                                    </div>
                                </div>
                                <div class="col"></div>
                            </div>
                            <br>
                            <div class="container-sm centered">
                                <div class="row">
                                    <div class="col"></div>
                                    <div class="col"></div>
                                    <div class="col">
                                        <p></p>
                                            <button class="w-100 btn btn-lg btn-primary greenedtotal" type="submit">Заказать</button>
                                            <p></p>
                                    </div>
                                    <div class="col"></div>
                                    <div class="col"></div>
                                </div>
                            </div>
                            <br>
                        </form>
                    </div>
                </div>
        </div>
    </div>


</template>



<script>
import axios from 'axios';
import moment from 'moment';

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
        let date_from = moment(new Date(this.order.datefrom + " " + this.order.timefrom)).format('YYYY-MM-DD hh:mm:ss');
        console.log('date_from', date_from);
        let date_to = moment(new Date(this.order.dateto + " " + this.order.timeto)).format('YYYY-MM-DD hh:mm:ss');
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


// Неправильный формат datetime. Используйте один из этих форматов: YYYY-MM-DD hh:mm:ss.

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
//   console.log(this.$route.params.id)
  this.getTransportByID();
},

}
</script>