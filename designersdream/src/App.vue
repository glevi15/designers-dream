<template>
  <v-app>
  <Navbar />
    <v-content class="mx-4 mb-4">
      <router-view></router-view>
    </v-content>
  </v-app>
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
