<template>
    <div>
              <nav class="navbar navbar-light bg-light">
                  <div class="container">

                      <a class="navbar-brand" href="#">
                          <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
                      </a>



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
                            <!-- <form> -->
                                      <div class="container-md centered whitened">
                                          <br>
                                            <p class="centered"><i class="fa fa-bullseye centered" aria-hidden="true"></i><h1 class="h3 mb-3 fw-normal whitened centered">Заказ создан!</h1> </p>
                                            <p>
                                                <br>
                                            </p>
                                      </div>
                                      <div class="container-sm centered whitened">
                                                <p class="centered">
                                              <h3 class="h5 mb-3 fw-normal whitened">
                                              Ваш транспорт добавлен.
                                              </h3>
                                              <h4 class="h5 mb-3 fw-normal whitened">
                                              Отслеживайте статус заказа в личном кабинете.
                                                  <br>
                                              </h4>
                                              <h4 class="h5 mb-3 fw-normal whitened">
                                              Удачной поездки!
                                              </h4>
                                                </p>
                                            <router-link to="/ntransport" class="btn btn-outline-primary me-2">Добавить еще </router-link>
                                            <router-link to="/mt" class="btn btn-outline-primary me-2">Вернуться в Мой транспорт</router-link>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                              <br>
                                      </div>


                                            </p>
                                          </div>
                            <!-- </form> -->
                        </div>
                    </div>
              </div>


    </div>
</template>

<script>

  export default {



    data() {

  },
   // ... методы
  methods: {
    // функция автоматичского редиректа
      // goBack() {
      // setTimeout(()=>this.$router.push('/cat'), 2000)
    // },
  },





mounted() {
    // this.goBack();
},
}

</script>