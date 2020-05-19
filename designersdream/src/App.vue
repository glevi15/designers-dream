<template>
 <div id="app">
  <span class="bg"></span>

  <v-app>
  <Navbar />
    <v-content class="mx-4 mb-4 ">
      <router-view></router-view>
    </v-content>  
  </v-app>
</div>
  
</template>

<!-- ADDED THE NAVBAR COMPONENT TO THE APP.VUE IN ORDER TO DISPLAY IT IN ALL ROUTES -->
<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: {Navbar},
  data: () => ({
    state: {}
  }),
};
</script>

<style>
.bg {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0; 
    /* background: url( '/background.jpg') no-repeat center center; */
    background: url( 'https://images.unsplash.com/photo-1498075702571-ecb018f3752d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1357&q=80') no-repeat center center;
    filter: saturate(0.5) ;
    background-size: cover;
    /* background-color: red; */
    transform: scale(1.1);
  }
</style>>