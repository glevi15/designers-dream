<template>
  <div class="Dashboard">
    <h1>Dashboard</h1>

    <v-container class="my-5 pt-12">
      <v-layout column wrap>
        <v-row xs12 sm6 md4 lg3>
          <v-col>
            <v-card color="primary" text class="text-xs-center pt-3 mx-4" max-width="600">
              <v-card-text>
                <div class="header white--text pt-2"> WELCOME TO DESIGNER'S DREAM APP</div>
              </v-card-text>
            </v-card>

            <v-card color="primary" text class="text-xs-center mt-5 mx-8" max-width="600">
              <v-responsive class="pt-4">
                <span class="white--text pa-2 .display-2" >INSTRUCTIONS</span>
              </v-responsive>
              <v-card-text>
                <span class="white--text pa-2 " >- Open the side bar</span>
                <span class="white--text pa-2" >- By clicking "Add New Project" button you can start working on a Project</span>
                <span class="white--text pa-2 " >-By clicking "My Projects" option, you can see and manage your saved projects</span>
                         
                <div class="dark--text">
                  <img src alt />
                </div>
              </v-card-text>
            </v-card>

            <!-- HEADLİNE -->

            <v-card max-width="600" outlined color="primary" class="mt-5 mx-12">
              <v-list-item three-line>
                <v-list-item-content>
                  <v-list-item-title class="headline mb-1">Let's Get Started!</v-list-item-title>
                  <v-list-item-title class="white--text">Click and get started!</v-list-item-title>
                </v-list-item-content>
              </v-list-item>

              <v-card-actions>
                  <v-spacer></v-spacer>
                <v-btn :to="'/newproject'">Get Started</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>

          <v-col> 
            <v-row>  <!-- first row of images -->
              <v-card class="d-inline-block mx-auto">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img
                        height="200"
                        width="200"
                        src="/pants-sk.png"
                      ></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
              
              <v-btn icon style="align-self: center;">
                <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
              </v-btn>
              

              <v-card class="d-inline-block mx-auto">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img
                        height="200"
                        width="200"
                        src="/pants.png"
                      ></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-row>

            <v-row></v-row>

            <v-row>    <!-- second row -->
              <v-card class="d-inline-block mx-auto mt-8">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img
                        height="200"
                        width="200"
                        src="/poster-sketch.png"
                      ></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>


              <v-btn icon style="align-self: center;">
                <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
              </v-btn>

              <v-card class="d-inline-block mx-auto mt-8">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img
                        height="200"
                        width="200"
                        src="/poster-img.png"
                      ></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-row>
          </v-col>
        </v-row>
      </v-layout>
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

 


