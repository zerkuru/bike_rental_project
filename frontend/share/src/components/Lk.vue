<template>
  <div>


    <body class="text-center">
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
              <div class="container-sm">
                  <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
                    <div class="col d-flex align-items-start">
                      <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
                        <svg class="bi" width="1em" height="1em"><use xlink:href="#toggles2"></use></svg>
                      </div>
                      <div>
                        <h2>Транспорт</h2>
                        <p>Категория позволяет добавить транспортные средства предназначенные для аренды.</p>
                        <router-link to="/ntransport"  class="btn btn-primary">
                          Добавить
                        </router-link>
                      </div>
                    </div>
                    <div class="col d-flex align-items-start">
                      <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
                        <svg class="bi" width="1em" height="1em"><use xlink:href="#cpu-fill"></use></svg>
                      </div>
                      <div>
                        <h2>Каталог</h2>
                        <p>У нас вы можете подобрать транспорт в аренду на определнные срок.</p>
                        <router-link to="/cat" class="btn btn-primary">
                          Подобрать
                        </router-link>
                        <router-link to="/mt" class="btn btn-primary">
                          Мой транспорт
                        </router-link>
                      </div>
                    </div>
                    <div class="col d-flex align-items-start">
                      <div class="icon-square bg-light text-dark flex-shrink-0 me-3">
                        <svg class="bi" width="1em" height="1em"><use xlink:href="#tools"></use></svg>
                      </div>
                      <div>
                        <h2>Мои заказы</h2>
                        <p>В этой категории вы можете посмотрет ваши заказы.</p>
                        <router-link to="/mo" class="btn btn-primary">
                          Просмотреть
                        </router-link>
                      </div>
                    </div>
                  </div>


          </div>








    </body>
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
