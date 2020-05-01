<template>
  <div class="Dashboard">
    <h1>Dashboard</h1>

    <v-container class="my-5">
      <v-layout column wrap>
        <v-flex xs12 sm6 md4 lg3 v-for="infos in info" :key="infos.name">
          <v-card color="primary" text class="text-xs-center ma-3" max-width="600">
            <v-responsive class="pt-4">
              <span class="white--text pa-2">title goes here</span>
            </v-responsive>
            <v-card-text>
              <div class="subheading white--text">{{infos.name}}</div>
              <div class="dark--text">{{infos.image}}</div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>

      <v-card max-width="600" outlined color="primary">
        <v-list-item three-line>
          <v-list-item-content>
            <div class="overline mb-4">Header</div>
            <v-list-item-title class="headline mb-1">Headline</v-list-item-title>
            <v-list-item-subtitle>Hello there!! Why not give our app a try? You will like it</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-avatar tile size="80" color="white"></v-list-item-avatar>
        </v-list-item>

        <v-card-actions>
          <v-btn>Get Started</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      info: [
        { name: "Type Something Here1", image: "Maybe an image here?1" },
        { name: "Type Something Here2", image: "Maybe an image here?2" }
      ]
    };
  }
};
</script>

<style>
body {
  position: initial !important;
}
</style>

 


