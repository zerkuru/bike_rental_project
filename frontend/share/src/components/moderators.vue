<template>
    <div>
        <nav class="navbar navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="/">
                <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
                </a>
                <div class="col-md-3 text-end">
                    <router-link to="/editlk" class="btn btn-outline-primary me-2"> <i class="fa  fa-address-card" aria-hidden="true"></i> </router-link>
                    <span v-if="isLoggedIn">  <a href="#"  class="btn btn-primary" @click="logout">Выйти</a></span>
                </div>
            </div>
        </nav>
        <br>

        <div class="tab">
        <button class="tablinks" :class="{active: visibleTab == 'tab1' ? true: false}" @click="visibleTab = 'tab1'" id="content-1">Каталог</button>
        <button class="tablinks" :class="{active: visibleTab == 'tab2' ? true: false}" @click="visibleTab = 'tab2'">Все заказы</button>
        <button class="tablinks" :class="{active: visibleTab == 'tab3' ? true: false}" @click="visibleTab = 'tab3'">Пользователи</button>
        <!-- <button class="tablinks" onclick="openOrders(event, 'Cabinet')">Мой кабинет</button> -->
        </div>
            <!-- <div class="tabs">
                <div class="tabs__links">
                    <a href="#content-1" @click="visibleTab = 'tab1'">Каталог</a>
                    <a href="#content-2" @click="visibleTab = 'tab2'">Все заказы</a>
                    <a href="#content-3" @click="visibleTab = 'tab3'">Пользователи</a>
                </div> -->
            <!-- <button @click="visibleTab = 'tab1'" class="tablinks">Каталог</button>
            <button @click="visibleTab = 'tab2'" class="tablinks">Все заказы</button>
            <button @click="visibleTab = 'tab3'" class="tablinks">Пользователи</button> -->

                <!-- <div id="Catalog" class="tabcontent"></div> -->
            <!-- <div v-if="currentTab === 'content-1'"> -->
                <div v-if="visibleTab == 'tab1'" > <!-- Каталог транспорта -->

                        <div id="Catalog" class="container-fluid">
                            <div class="container-sm">
                            <div class="row">
                                <div class="col centered">
                                    <i class="fa fa-bullseye" aria-hidden="true"></i>
                                    <h1 class="h3 mb-3 fw-normal">Каталог</h1>
                                </div>
                                <br>
                            </div>
                            </div>
                            <nav class="navbar navbar-expand-md navbar-dark fixed-middle greenedtotal">
                                <div class="container-fluid">
                                    <div class="container-small">
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
                                </div>
                            </nav>
                            <br>
                            <br>
                            <div class="container-sm centered">
                                <router-link to="/ntransport" class="btn btn-primary btn-lg">
                          Добавить транспорт
                        </router-link>
                            </div>
                            <br>

                            <div class="album py-5 bg-light">
                                <div class="container greened-gradient">
                                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                                <!-- <!одинаковые карточки транспорта данные> -->
                                    <div class="col"  v-for="transport in sortedTransportWithPriceUpTo" :key="transport.id">
                                        <div class="card shadow-sm">
                                         <div v-if="transport.image">
                                            <img :src="`${transport.image}`" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                                            </div>
                                            <div v-else>
                                            <img src="http://127.0.0.1:8000/media/imgTransport/default.jpg" width="100%" height="225" class="bd-placeholder-img card-img-top"/>
                                            </div>
                                        <div class="card-body">
                                            <p class="card-text">
                                                <!-- {{TransportType }} {{TransportModel}} -->
                                                {{ transport.transport_type}} - {{ transport.transport_model }}
                                            </p>
                                            <p class="card-text">
                                                <!-- {{Information }} -->
                                                {{ transport.information}}
                                            </p>
                                            <div class="d-flex justify-content-between align-items-center">
                                                <div class="btn-group">
                                                          <button type="button" class="btn btn-sm btn-outline-secondary" @click="$router.push(`/transportedit/${transport.id}`)">Редактировать</button>
                                                          <button type="button" class="btn btn-sm btn-outline-secondary" @click="delMyTransport(transport.id)">Удалить</button>
                                            </div>
                                            <small class="text-muted">
                                                    <!-- {{price}} -->
                                                    {{ transport.price}}
                                            </small>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                </div>
                                </div>
                        </div>

                    </div>
                <!-- </div> -->
            </div>

            <!-- <div v-else-if="currentTab === 'content-2'"> -->
                <div v-if="visibleTab == 'tab2'" > <!-- Каталог заказов -->
                    <div id="Orders" class="container-fluid">
                        <div class="container-fluid my_own_orders">
                            <div class="container-sm">
                                <div class="row">
                                    <div class="col centered">
                                        <i class="fa fa-bullseye" aria-hidden="true"></i>
                                        <h1 class="h3 mb-3 fw-normal">Все заказы</h1>
                                        <div><br>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <nav class="navbar navbar-expand-lg navbar-dark fixed-middle greenedtotal">
                        <div class="container-fluid">
                            <div class="container-small">
                                <form class="d-flex" @submit.prevent="">
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
                                    <span class="selectbox">
                                            <input type="text" class="form-control" id="owner" placeholder="Владелец транспорта" v-model="sortOwner">
                                    </span>
                                    <span class="selectbox">
                                            <input type="text" class="form-control" id="client" placeholder="Заказчик" v-model="sortClient">
                                    </span>
                                    <button class="btn btn-outline-success" type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
                                </form>
                            </div>
                        </div>
                    </nav>
                    <!-- <!orders данные> -->
                    <div class="container-fluid transportback">
                        <!-- <!карточка заказа> -->
                        <br>
                        <div class="container-sm transparent">
                            <div class="row transparent"  v-for="order in sortedClient" :key="order.id">
                                <div class="col-sm lefted" style="max-width: 200px;">
                                    <div class="card text-light greyedtotal mb-3 rounded orderopacity"
                                        style="max-width: 200px; --bs-bg-opacity: .1; padding-left: 10px">
                                        {{order.status}}
                                    </div>
                                </div>
                                <div class="col" style="max-width: 600px;">
                                    <div class="card greenedtotallight orderopacity text-dark mb-3 rounded"
                                        style="max-width: 600px; --bs-bg-opacity: .1; padding-left: 10px">
                                    <h5 class="light"> Заказ № {{order.id}}
                                        </h5>
                                    <h6 class="light">тип и модель
                                        {{order.ransportType}} - {{order.transportModel}}
                                        </h6>
                                    <h6 class="light">
                                        {{order.date_from}}
                                        <br> до
                                        {{order.date_to}}
                                        </h6>
                                    </div>
                                </div>
                                <div class="col" style="max-width: 350px;">
                                    <div class="card greyedtotal orderopacity text-light mb-3 rounded"
                                        style="max-width: 300px; --bs-bg-opacity: 0.3; padding-left: 10px">
                                    <h5 class="light"> Владелец </h5>
                                    <h6 class="light">Имя
                                           {{order.transport_owner}}
                                        </h6>
                                    <h6 class="light">Контакты
                                           {{order.transport_owner_phone}} - {{order.transport_owner_email}}
                                        </h6>
                                    </div>
                                </div>
                                <div class="col" style="max-width: 350px;">
                                    <div class="card greyedtotal orderopacity text-light mb-3 rounded"
                                        style="max-width: 300px; --bs-bg-opacity: 0.3; padding-left: 10px">
                                    <h5 class="light"> Заказчик </h5>
                                    <h6 class="light">Имя
                                        {{order.client_name}}
                                        </h6>
                                    <h6 class="light"> Контакты
                                        {{order.clien_phone}} - {{order.client_email}}
                                        </h6>
                                    </div>
                                </div>
                                <div class="col" style="max-width: 150px;">
                                    <div flex>
                                        <!-- <button type="button" class="btn btn-primary" style="margin-bottom: 15px;"> Открыть </button>
                                        <button type="button" class="btn btn-danger"> Отменить </button> -->
                                            <!-- <button v-if="(order.status == 'подтвержден' ? false  : true) && (order.status != 'отменен') && (order.status != 'завершен')" type="button" class="btn btn-primary" style="margin-bottom: 15px;" @click="applyOrderById(order.id)"> Принять </button> -->
                                            <button v-if="(order.status != 'завершен') && (order.status != 'отменен') && (order.status == 'подтвержден')  " type="button" class="btn btn-primary" style="margin-bottom: 15px;" @click="finishOrderFromMeById(order.id)"> Завершить </button>
                                            <button v-if="(order.status != 'отменен') && (order.status != 'завершен') && (order.status != 'подтвержден') " type="button" class="btn btn-danger" @click="cancelOrderById(orderme.id)"> Отклонить </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- <!карточка заказа> -->

                <br></div>
                </div>
            </div>

            <!-- <div v-else="currentTab === 'content-3'"> -->
                <div v-if="visibleTab == 'tab3'" > <!--Пользователи -->
                    <div id="Users" class="container-fluid">
                        <div class="container-sm" >
                                <div class="row">
                                    <div class="col centered">
                                        <i class="fa fa-bullseye" aria-hidden="true"></i>
                                        <h1 class="h3 mb-3 fw-normal" >Пользователи</h1>
                                    <div>
                                        <br>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- <!список пользователей> -->
                    <div class="container-fluid greenedtotal">
                        <br>

                        <!-- <!заголовок> -->
                        <div class="container-sm orderopacity bg-light greyed">
                            <div class="row">
                                <div class="col-sm">
                                            <div class="form-group">
                            <input type="text" class="form-control" style="margin-top: 10px;" id="owner" placeholder="Пользователь" v-model="sortUsername"/>
                                </div>


                                </div>
                                <div class="col-sm"></div>
                            </div>
                            <div class="row">
                                <div class="col-sm">
                                    ПОЛЬЗОВАТЕЛЬ
                                </div>
                                <!-- <div class="col-sm">
                                    ЗАКАЗЫ ПОЛЬЗОВАТЕЛЯ
                                </div>
                                <div class="col-sm">
                                    ЗАКАЗЫ ТРАНСПОРТА
                                </div> -->
                                <div class="col-sm">
                                    ПРАВА
                                </div>
                                 <div class="col-sm">
                                    КОНТАКТНЫЙ ТЕЛЕФОН
                                </div>
                                <div class="col-sm">
                                   E-MAIL
                                </div>
                                <!-- <div class="col-sm">
                                    РЕДАКТИРОВАТЬ
                                </div>  -->
                            </div>
                            <div class="row" v-for="user in sortedUsersname" :key="user.id">
                                <div class="col-sm">
                                    <!-- Иванов Иван -->
                                    <!-- <!{{Имя пользователя}}> -->
                                    {{user.full_name}}


                                </div>
                                <div class="col-sm">
                                    {{ user.is_staff ? 'Admin' : 'User'}}
                                    <!-- <!{{Тип прав пользователя - обычный, ограниченный (бан), модератор, админ}}>  -->
                                </div>
                                <div class="col-sm">
                                    {{user.tel_number}}
                                    <!-- <!{{Количество заказов от пользователя}}> -->
                                </div>
                                <div class="col-sm">
                                  {{user.email}}

                                </div>
                        </div>
                        </div>

                        <div class="container-sm orderopacity bg-light greyed" >

                                <div class="col-sm">
                                    0
                                    <!-- <!{{Количество заказов  транспорта пользователя}}> -->
                                </div>

                                <!-- <div class="col-sm">
                                    <button type="button" class="btn btn-primary usermargin">Вернуть права авторизации</button>


                                </div> -->

                                <!-- <div class="col-sm">
                                    <button type="button" class="btn btn-danger usermargin ">Ограничение авторизации</button>
                                </div>
                                <div class="col-sm">
                                    <! только для обычных или ограниченных>
                                    <button type="button" class="btn btn-outline usermargin">Редактировать данные</button>
                                </div> -->
                            </div>
                            <br>
                        </div>

                    </div>
                    <br>
                </div>
            <!-- </div> -->
        <!-- </div> -->
        <!-- <hr>
            <button @click="visibleTab = 'tab1'">Tab1</button>
            <button @click="visibleTab = 'tab2'">Tab2</button>
            <button @click="visibleTab = 'tab3'">Tab3</button>
            <div v-if="visibleTab == 'tab1'">tab 1</div>
            <div v-if="visibleTab == 'tab2'"> tab 2</div>
            <div v-if="visibleTab == 'tab3'"> tab 3</div>
        <hr> -->

    </div>
</template>

<script>




import axios from 'axios';


  export default {



    data() {
       return {
        sortUsername: '',
      visibleTab: 'tab1',
      currentUser: [],
      transports: [],
      orders: [],


      results: {},
      manufactutrers: [],
      transport_types: [],
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



      sortOrder: '',
      sortOrderForMe:'',
      sortOrderDateFrom: '',
      sortOrderDateTo: '',
      sortOwner: '',
      sortClient: '',

      typeSort:'',
      sortAge: "",
      sortPriceFrom: "",
      sortPriceUpTo: "",

    }
  },







   // ... методы
  methods: {
    getUserData() {
      // const axios = require('axios').default

      axios.get('http://127.0.0.1:8000/moderation/users/',{
        headers:{
          'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
           }}).then((response) => {
            // правильно назвать не currentUser а UserList - список пользвателей
           this.currentUser = [...response.data];
           console.log(this.currentUser)
         }).catch((error) => {
          console.error(error);
        });
        },
    getTransportsData() {
      axios.get(`http://127.0.0.1:8000/moderation/transports/`, {
        headers:{
          'Content-Type': 'applicatios/json',
            Authorization: `token ${localStorage.getItem('token')}`,
           }}).then((response) => {
           this.transports = [...response.data];
            console.log(this.transports);
         }).catch((error) => {
          console.error(error);
        });
        },
    getOrdersData() {
        axios.get(`http://127.0.0.1:8000/moderation/orders/`, {
            headers:{
                'Content-Type': 'applicatios/json',
                Authorization: `token ${localStorage.getItem('token')}`,
                }}).then((response) => {
                    this.orders = [...response.data];
                     console.log(this.orders);
                    }).catch((error) => {
                    console.error(error);
            });
        },
      logout: function() {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
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
            });
        },
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







  computed:{
        sortedUsersname(){
            return [...this.currentUser].filter(user =>{
            return user.full_name.toLowerCase().includes(this.sortUsername.toLowerCase())
        })
        },

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
         sortedOwner(){
            return [...this.sortedOrdersByDateTo].filter(order =>{
                return order.transport_owner.toLowerCase().includes(this.sortOwner.toLowerCase())
            })
         },
        sortedClient(){
            return [...this.sortedOwner].filter(order =>{
                return order.client_name.toLowerCase().includes(this.sortClient.toLowerCase())
            })
        },
         isLoggedIn: function() { return this.$store.getters.isLoggedIn },

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
  this.getUserData();
  this.getTransportsData();
  this.getOrdersData();
  this.getManufacturerData();
  this.getTransportTypesData();



},
  }
</script>

<style scoped>
.tabs {
  display: flex;
  flex-direction: column;
}

.tabs__links {
  display: flex;
  width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 10px;
  order: 0;
  white-space: nowrap;
  background-color: #fff;
  border: 1px solid #e3f2fd;
  box-shadow: 0 2px 4px 0 #e3f2fd;
}

.tabs__links>a {
  display: inline-block;
  text-decoration: none;
  padding: 6px 10px;
  text-align: center;
  color: #1976d2;
}

.tabs__links>a:hover {
  background-color: rgba(227, 242, 253, 0.3);
}

.tabs>#content-1:target~.tabs__links>a[href="#content-1"],
.tabs>#content-2:target~.tabs__links>a[href="#content-2"],
.tabs>#content-3:target~.tabs__links>a[href="#content-3"] {
  background-color: #bbdefb;
  cursor: default;
}

.tabs>div:not(.tabs__links) {
  display: none;
  order: 1;
}

.tabs>div:target {
  display: block;
}

</style>
