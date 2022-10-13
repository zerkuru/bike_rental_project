<template>
  <div id="app">
      <div id="nav">

      </div>
      <router-view/>


      <div>




                  <footer class="footer mt-auto py-3 bg-light">
                              <div class="container-fluid greenedtotal">
                              <div class="container-md greenedtotal">
                                <p> <h4 class="footerheader whitened">
                                      Контакты
                                    </h4> </p>
                                <p>
                                      <h5 class="footertext whitened">
                                  свяжитесь с нами по телефону или оставив сообщение
                                      </h5>
                                  </p>
                                <hr class="footervector">
                                <div class="row align-items-center">
                                <div class="col-sm">
                                        <h4 class="footerlisttext whitened">
                                            +7-812-0101010101
                                        </h4>
                                    </div>
                                  <div class="col-sm">
                                        <h4 class="footerlisttext whitened">
                                            scooterbikeshare@gmail.com
                                        </h4>
                                    </div>

                                    <div class="col-sm">
                                        <h4 class="footerlisttext whitened">
                                            &copy; 2022 Bike&Scooter
                                        </h4>
                                    </div>

                                </div>
                              </div>
                            </div>

                  </footer>





  </div>
</div>
</template>


<script>
  export default {
    created: function() {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(logout)
        }
        throw err;
      });
    });
  },
    computed: {
      isLoggedIn: function() { return this.$store.getters.isLoggedIn }
    },
    methods: {
      logout: function() {
        this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
      },
    },
  }
</script>


<style>
@import './assets/bootstrap/css/main.css';

</style>
