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
    <div class="tab">
        <button @click="visible = 'tab1'" class="tablinks" >Мои заказы</button>
        <button @click="visible = 'tab2'" class="tablinks" >Заказано у меня</button>
    </div>

        <!-- <hr>
            <button @click="visibleTab = 'tab1'">Tab1</button>
            <button @click="visibleTab = 'tab2'">Tab2</button>
            <button @click="visibleTab = 'tab3'">Tab3</button>
            <div v-if="visibleTab == 'tab1'">tab 1</div>
            <div v-if="visibleTab == 'tab2'"> tab 2</div>
            <div v-if="visibleTab == 'tab3'"> tab 3</div>
        <hr> -->



    <!-- <!следующий div выводится, если есть заказы пользователя - Мои заказы> -->
    <div v-if="visible == 'tab1'">
        <div class="container my_own_orders">
            <div class="container-sm">
                <div class="row">
                    <div class="col centered">
                        <i class="fa fa-bullseye" aria-hidden="true"></i>
                        <h1 class="h3 mb-3 fw-normal">Мои заказы</h1>
                    </div>
                    <br>
                </div>
            </div>


        <nav class="navbar navbar-expand-md navbar-dark fixed-middle greenedtotal">
            <div class="container-fluid">
                <div class="container-small">
                    <form class="d-flex">
                        <span class="selectbox">
                            <select id="order_type" class="form-control me-2" v-model="sortOrder">
                                <option value="">Все заказы&hellip;</option>
                                <option value="подтвержден">Подтвержденные</option>
                                <option value="завершен">Закрытые</option>
                                <option value="формируется">Новые</option>
                                <option value="отменен">Отклоненные</option>
                            </select> </span>
                        <span class="whitened"> Дата от: </span>
                        <span class="selectbox">
                                <input type="date" class="form-control" id="datefrom" v-model="sortOrderDateFrom">
                        </span>
                        <span class="whitened"> Дата до: </span>
                        <span class="selectbox">
                            <div class="form">
                            <input type="date" class="form-control transparent" id="dateto" v-model="sortOrderDateTo">
                            </div>
                        </span>
                        <button class="btn btn-outline-success" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                    </form>
                </div>
            </div>
        </nav>
        <!-- <!my orders> -->            <!-- <!карточка заказа> -->
        <div class="container-md transportback_dark"><br>
            <div  v-for="order in sortedOrdersByDateTo" :key="order.id">

            <div class="container-sm transparent">
                <div class="row transparent">
                    <div class="col-sm lefted" style="max-width: 200px;">
                        <div class="card text-light bg-dark mb-3 rounded" style="max-width: 200px; --bs-bg-opacity: .1; padding-left: 10px">
                        {{ order.status }}
                        </div>
                    </div>
                    <div class="col" style="max-width: 600px;">
                        <div class="card greenedtotal text-dark mb-3 rounded" style="max-width: 600px; --bs-bg-opacity: .1; padding-left: 10px">
                                            <h5 class="light"> Заказ №
                                                {{order.id}}
                                                </h5>
                                            <h6 class="light">
                                                {{order.transport_type}} - {{order.transport_model}}
                                                <!-- Тип транспорта - Модель транспорта -->
                                                </h6>
                                            <h6 class="light"> c
                                                {{order.date_from}}
                                                <br> до
                                                {{order.date_to}}
                                                </h6>
                        </div>
                    </div>
                    <div class="col" style="max-width: 350px;">
                        <div class="card bg-dark text-light mb-3 rounded" style="max-width: 300px; --bs-bg-opacity: 0.3; padding-left: 10px">
                                        <h5 class="light"> Владелец </h5>
                                        <h6 class="light">
                                            {{order.transport_owner}}
                                            <!-- Артур -->
                                            </h6>
                                        <h6 class="light">
                                            {{order.transport_owner_phone}} - {{order.transport_owner_email}}
                                            <!-- +7918 911 79 99 / matos85@mil.ru -->
                                        </h6>
                        </div>
                    </div>
                    <div class="col" style="max-width: 150px;">
                        <div flex>
                            <!-- <button type="button" class="btn btn-primary" style="margin-bottom: 15px;"> Открыть </button> -->
                            <!-- <button v-if="(order.status == 'завершен' ? false  : true)" type="button" class="btn btn-primary" style="margin-bottom: 15px;" @click="finishOrderById(order.id)"> Завершить </button> -->
                            <!-- <button v-if="(orderme.status == 'подтвержден' ? false  : true) && (orderme.status != 'отменен') && (orderme.status != 'завершен')" -->
                            <button v-if="(order.status != 'формируется' ? false  : true)" type="button" class="btn btn-danger" @click="delOrdersById(order.id)"> Отменить </button>
                        </div>
                    </div>
                </div>
                </div>
                </div>
            </div><br>
        </div>
        <br><br>
    </div>
    <!-- <!следующий div выводится, если есть заказы транспорта пользователя - У меня заказали> -->
    <div v-else>
        <div class="container ordered_from_me">
            <div class="container-sm">
                <div class="row">
                    <div class="col centered">
                        <i class="fa fa-bullseye" aria-hidden="true"></i>
                        <h1 class="h3 mb-3 fw-normal">У меня заказали </h1>
                    <div>
                </div>
            </div>
        </div>
    </div>
    <nav class="navbar navbar-expand-md navbar-dark fixed-middle greyedtotal">
    <div class="container-fluid">
        <div class="container-small">
            <form class="d-flex">
                <span class="selectbox">
                    <select id="order_type" class="form-control me-2" v-model="sortOrderForMe">
                        <option value="">Все заказы&hellip;</option>
                        <option value="подтвержден">Подтвержденные</option>
                        <option value="завершен">Закрытые</option>
                        <option value="формируется">Новые</option>
                        <option value="отменен">Отклоненные</option>
                    </select> </span>
                <span class="whitened"> Дата от: </span>
                <span class="selectbox">
                         <input type="date" class="form-control" id="datefrom" v-model="sortOrderForMeDateFrom">
                </span>
                <span class="whitened"> Дата до: </span>
                <span class="selectbox">
                    <div class="form">
                    <input type="date" class="form-control transparent" id="dateto" v-model="sortOrderForMeDateTo">
                    </div>
                </span>
                <button class="btn btn-outline-success" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
            </form>
        </div>
    </div>
</nav>
<!-- <!my orders> -->
<div class="container-md transportback_dark">
    <div  v-for="orderme in sortedOrdersForMeByDateTo" :key="orderme.id">
    <!-- <!карточка заказа> -->
    <br>
        <div class="container-sm transparent">
            <div class="row transparent">
                <div class="col-sm lefted" style="max-width: 200px;">
                    <div class="card bg-dark text-light mb-3 rounded"
                        style="max-width: 200px; -bg-opacity: 0.3; padding-left: 10px">
                        {{orderme.status}}
                                    </div>
                                </div>
                                <div class="col" style="max-width: 600px;">
                                    <div class="card text-light greyedtotal mb-3 rounded" style="max-width: 600px; --bs-bg-opacity: 0.3; padding-left: 10px">
                                        <h5 class="light"> Заказ №
                                            {{orderme.id}}
                                            </h5>
                                        <h6 class="light">
                                            <!-- {{transportType}} {{transportModel}} -->
                                            {{orderme.transport_type}} - {{orderme.transport_model}}
                                            <!-- Тип транспорта - Модель транспорта -->
                                            </h6>
                                        <h6 class="light"> c
                                            {{orderme.date_from}} <br>
                                            <!-- 21.07.2022 16:47 -->
                                            до
                                            {{orderme.date_to}}
                                            <!-- 22.07.2022 16:47 -->
                                            </h6>
                                    </div>
                                </div>
                                <div class="col" style="max-width: 350px;">
                                    <div class="card bg-dark text-light mb-3 rounded" style="max-width: 300px; --bs-bg-opacity: 0.3; padding-left: 10px">
                                        <h5 class="light"> Заказчик </h5>
                                        <h6 class="light">
                                            <!-- {{Client name}} -->
                                            {{orderme.client_name}}
                                            <!-- Маруся -->
                                            </h6>
                                        <h6 class="light">
                                            <!-- {{client phone}} {{client e-mail}} -->
                                            {{orderme.clien_phone}} {{orderme.client_email}}

                                            <!-- +7918 911 99 99 / marus5@mail.ru -->
                                            </h6>
                    </div>
                </div>
                <div class="col" style="max-width: 150px;">
                    <div flex>
                        <button v-if="(orderme.status == 'подтвержден' ? false  : true) && (orderme.status != 'отменен') && (orderme.status != 'завершен')" type="button" class="btn btn-primary" style="margin-bottom: 15px;" @click="applyOrderById(orderme.id)"> Принять </button>
                        <button v-if="(orderme.status != 'завершен') && (orderme.status != 'отменен') && (orderme.status == 'подтвержден')  " type="button" class="btn btn-primary" style="margin-bottom: 15px;" @click="finishOrderFromMeById(orderme.id)"> Завершить </button>
                        <button v-if="(orderme.status != 'отменен') && (orderme.status != 'завершен') && (orderme.status != 'подтвержден') " type="button" class="btn btn-danger" @click="cancelOrderById(orderme.id)"> Отклонить </button>
                    </div>
                </div>
            </div>
        </div>
    </div>


    </div>
        </div>
    </div>




</div>
</template>
<script >

import axios from 'axios';
import moment from 'moment';

  export default {

    data() {
       return {
        visible: 'tab1',
        orders: [],
        ordersfromme:[],
        sortOrder: "",
        sortOrderForMe:'',
        // sortOrderDateFrom: moment().format('YYYY-MM-DD'),
        sortOrderDateFrom: '',
        sortOrderDateTo: '',
        sortOrderForMeDateFrom: '',
        sortOrderForMeDateTo: '',
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
            // console.log(this.transports);
          //  this.results = response.data;
         }).catch((error) => {
          console.error(error);
        });
        },
    getMyOrdersData() {
         axios.get(`http://127.0.0.1:8000/api/orders/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.orders = [...response.data];
                    this.orders.sort((a, b)=> a.id - b.id);
                     console.log(this.orders);
                    }).catch((error) => {
                    console.error(error);
            });
        },

    getOrdersFromMeData() {
         axios.get(`http://127.0.0.1:8000/api/orders-from-me/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.ordersfromme = [...response.data];
                    this.ordersfromme.sort((a, b)=> a.id - b.id);
                     console.log(this.ordersfromme);
                    }).catch((error) => {
                    console.error(error);
            });
        },
     async delOrdersById(id) {

         await axios.delete(`http://127.0.0.1:8000/api/orders/${id}`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    // console.log(response);
                    this.orders.forEach(order => {
                        if(order.id === id){
                            // console.log('order id', order);
                            // console.log('order id', order.status);
                            order.status = "отменен"
                        }
                    })
                    }).catch((error) => {
                    console.error(error);
            });
        },
    // http://127.0.0.1:8000/change-status/<int:id>/RDY/

    applyOrderById(id){
         axios.get(`http://127.0.0.1:8000/change-status/${id}/RDY/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.ordersfromme.forEach(order => {
                        if(order.id === id){
                            console.log('order id', order);
                            console.log('order id', order.status);
                            order.status = "подтвержден"
                        }})
                    }).catch((error) => {
                    console.error(error);
            });

    },

    // http://127.0.0.1:8000/change-status/<int:id>/CNC/
    cancelOrderById(id){
      axios.get(`http://127.0.0.1:8000/change-status/${id}/CNC/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.ordersfromme.forEach(order => {
                        if(order.id === id){
                            console.log('order id', order);
                            console.log('order id', order.status);
                            order.status = "отменен"
                        }})
                    }).catch((error) => {
                    console.error(error);
            });
    },
    finishOrderFromMeById(id){
         axios.get(`http://127.0.0.1:8000/change-status/${id}/FSD/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.orders.forEach(order => {
                        if(order.id === id){
                            console.log('order id', order);
                            console.log('order id', order.status);
                            order.status = "завершен"
                        }})
                    }).catch((error) => {
                    console.error(error);
            });

    },

    postTransport : function () {


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
          this.results = {...response.data};
        })
        .catch(e => {
          this.errors.push(e)
         })
       },
},
computed:{
        sortedOrders(){
        return [...this.orders].filter(order =>{
            return order.status.toLowerCase().includes(this.sortOrder.toLowerCase())
        })
         },
         sortedOrdersByDateFrom(){
            return [...this.sortedOrders].filter(order => {
                if (!this.sortOrderDateFrom) return true;
                return new Date(order.date_from.substring(0,10).split("-").reverse().join("-")) >= new Date(this.sortOrderDateFrom)
            })
         },
         sortedOrdersByDateTo(){
            return [...this.sortedOrdersByDateFrom].filter(order => {
                if (!this.sortOrderDateTo) return true;
                return new Date(order.date_to.substring(0,10).split("-").reverse().join("-")) <= new Date(this.sortOrderDateTo)
            })
         },


        sortedOrdersForMe(){
            return [...this.ordersfromme].filter(orderme =>{
            return orderme.status.toLowerCase().includes(this.sortOrderForMe.toLowerCase())
        })

        },
        sortedOrdersForMeByDateFrom(){
            return [...this.sortedOrdersForMe].filter(orderme => {
                if (!this.sortOrderForMeDateFrom) return true;
                return new Date(orderme.date_from.substring(0,10).split("-").reverse().join("-")) >= new Date(this.sortOrderForMeDateFrom)
            })
        },
        sortedOrdersForMeByDateTo(){
            return [...this.sortedOrdersForMeByDateFrom].filter(orderme => {
                if (!this.sortOrderForMeDateTo) return true;
                return new Date(orderme.date_to.substring(0,10).split("-").reverse().join("-")) <= new Date(this.sortOrderForMeDateTo)
            })

        },
},
mounted() {
  this.getManufacturerData();
  this.getTransportTypesData();
  this.getUserData();
  this.getTransportsData();
  this.getMyOrdersData();
  this.getOrdersFromMeData();

}
  }
</script>