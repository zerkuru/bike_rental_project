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
                        <router-link to="/cat" class="btn btn-outline-primary me-2"> <i class="fa  fa-folder-open" aria-hidden="true"></i> </router-link>
                        <router-link to="/mo" class="btn btn-outline-primary me-2"> <i class="fa fa-cart-plus" aria-hidden="true"></i> </router-link>
          </div>

          </div>
        </nav>
            <div class="container-sm">
                <div class="row">
                    <div class="col centered">
            <i class="fa fa-bullseye" aria-hidden="true"></i>
            <h1 class="h3 mb-3 fw-normal">Мой транспорт</h1>
                      <div>
                        <br>
                        <br>
                      </div>


                    </div>
                </div>
            </div>


            <div class="container-fluid transportback_dark">
              <br>
              <br>
              <div class="container-sm">
                <div class="row">
                    <div class="col centered">
            <h3 class="h4 mb-3 fw-normal light">Вы уверены, что хотите удалить эту карточку транспорта?</h3>
                      <br>
                      <div class="btn-group">
                          <button type="button" class="btn btn-primary" @click="$router.push('/mt')">Оставить</button>
                          <button type="button" class="btn btn-danger" @click="$router.push('/mt')">Удалить</button>
                        </div>
                    </div>

                </div>
              </div>
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



  </div>

</template>