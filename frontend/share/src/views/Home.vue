<template>
  <div class="home">
                <nav class="navbar navbar-light bg-light">
                  <div class="container">      
                    <a class="navbar-brand" href="/">
                      <span class="logotext greened"><i class="fa fa-bullseye" aria-hidden="true"></i>Bike&Scooter</span>
                    </a>
                    <div class="col-md-3 text-end">
                      <router-link to="/lk" class="btn btn-outline-primary me-2"><i class="fa fa-user-circle" aria-hidden="true"></i> </router-link>
                      <span v-if="isLoggedIn">  <a href="#"  class="btn btn-primary" @click="logout">Выйти</a></span>
                      <router-link v-else to="/register" class="btn btn-primary"><i class="fa fa-user-circle-o" aria-hidden="true"></i>Регистрация</router-link>
                    </div>     
                  </div>
                </nav>

      <div class="container-fluid greened-gradient" >
        <div class="headerpart">

                <div class="container-md">
                    <span class="titlename">
                        <h1 class="display-1">Аренда велосипедов и самокатов</h1>
                    </span>
                  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-inner">
                      <div class="carousel-item active">
                        <img src="../assets/bootstrap/img/bikes.png" class="d-block w-100" alt="photo1">
                      </div>
                      <div class="carousel-item">
                        <img src="../assets/bootstrap/img/bike2.jpg" class="d-block w-100" alt="photo2">
                      </div>
                      <div class="carousel-item">
                        <img src="../assets/bootstrap/img/bike3.jpg" class="d-block w-100" alt="photo3">
                      </div>
                  </div>
                  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Предыдущий</span>
                  </button>
                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"  data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Следующий</span>
                  </button>
                </div>
        </div>

        </div>
      </div>


                      <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
                          <div class="feature col centered">
                          
                              <p>
                                <i class="fa fa-bicycle fa-4x greened" aria-hidden="true"></i>
                              </p>

                         
                            <h2>Велосипед на выходные</h2>
                            <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                            <a href="#" class="icon-link">
                              ...
                           
                            </a>
                          </div>
                          <div class="feature col centered">
                          
                              <p><i class="fa fa-bicycle fa-4x greened" aria-hidden="true"></i> </p>
                           
                            <h2>Наш каталог</h2>
                            <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                            <a href="#" class="icon-link">
                              ...
                           
                            </a>
                          </div>
                          <div class="feature col centered">
                           
                                <p><i class="fa fa-bicycle fa-4x greened" aria-hidden="true"></i> </p>
                         
                            <h2>Лучшие маршруты</h2>
                            <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                            <a href="#" class="icon-link">
                              ...
                              <svg class="bi" width="1em" height="1em"><use xlink:href="#chevron-right"></use></svg>
                            </a>
                          </div>
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

