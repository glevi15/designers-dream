<template>
  <div class="Dashboard">
    <!-- <p class="display-2 font-italic pt-8 mx-12 pl-5">Dashboard</p> -->

    <v-container >
      <v-layout column wrap class="pt-12">
        <v-row xs12 sm6 md4 lg3>
          <v-col>
            <v-card color="primary" text class="text-xs-center pt-3 mx-4" shaped :elevation="24">
              <v-card-text>
                <!--<div class="header white--text pt-2 ">WELCOME TO DESIGNER'S DREAM APP</div> -->
                <p class="header white--text display-2 pt-2 text-center"> Welcome to Designer's Dream!</p>
              </v-card-text>
            </v-card>

            <v-card color="primary" text class="text-xs-center mt-5 mx-4" shaped>
              <v-responsive class="pt-4">
                <p class="display-1 text-center white--text"> Instructions</p>
              </v-responsive>
              <v-card-text>
                <p class="white--text pa-2 headline">- Open the side bar</p>
                <p
                  class="white--text pa-2 headline" 
                >- Click <span class="font-italic font-weight-bold mr-1">Add New Project </span>  to start working on a Project</p>
                <p
                  class="white--text pa-2 headline"
                >- Click <span class="font-italic font-weight-bold mr-1">My Projects </span> to see and manage your saved projects</p>                
                <p
                  class="white--text pa-2 headline"
                >- Or press <span class="font-italic font-weight-bold mr-1">Get Started</span> below!</p>

                <div class="dark--text">
                  <img src alt />
                </div>
              </v-card-text>
            </v-card>

            <!-- HEADLINE -->

            <v-card  outlined color="primary" class="mt-5 mx-4" shaped>
              <v-list-item three-line>
                <v-list-item-content>
                  <v-list-item-title class="white--text pa-2 headline">Are you ready to make your dreams come true?</v-list-item-title>
                  <!-- <v-list-item-title class="white--text pl-2 title">Click and get started!</v-list-item-title> -->
                </v-list-item-content>
              </v-list-item>

              <v-dialog v-model="dialog" width="500">
                <template v-slot:activator="{ on }">
                  <v-row>
                    <v-col class="mx-6"><p class="white--text  title">Click and get started!</p></v-col>
                    
                    <v-col class="text-right">
                      <v-btn x-large flat v-on="on" class="mr-6" >
                        Get Started
                      <v-icon>mdi-arrow-right</v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </template>

                <v-card>
                  <v-card-title class="headline grey lighten-2" primary-title>Save Project</v-card-title>

                  <v-card-text>
                    <v-form class="px-3">
                      <v-text-field
                        label="Title"
                        v-model="title"
                        prepend-icon="folder"
                      >Please type a title</v-text-field>
                      <v-textarea label="Information" v-model="content" prepend-icon="edit"></v-textarea>
                    </v-form>
                  </v-card-text>

                  <v-divider></v-divider>

                  <v-card-actions>
                    <v-btn color="success" text @click="cancel()">Cancel</v-btn>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="submit()">Create</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>

              <!-- <v-card-actions>
                  <v-spacer></v-spacer>
                <v-btn :to="'/newproject'">Get Started</v-btn>
              </v-card-actions>-->
            </v-card>
          </v-col>

          <v-col class="pt-12 mt-12" >
            <v-row class="pt-8 pb-8 ">
              <!-- first row of images -->
              <v-card class="d-inline-block mx-auto">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img height="200" width="200" src="/pants-sk.png"></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>

              <!-- <v-btn icon disabled style="align-self: center;"> -->
                <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
              <!-- </v-btn> -->

              <v-card class="d-inline-block mx-auto">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img height="200" width="200" src="/pants.png"></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-row>

            <v-row></v-row>

            <v-row>
              <!-- second row -->
              <v-card class="d-inline-block mx-auto mt-8">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img height="200" width="200" src="/poster-sketch.png"></v-img>
                    </v-col>

                    <v-col cols="auto" class="text-center pl-0">
                      <v-row class="flex-column ma-0 fill-height" justify="center"></v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>

              <!-- <v-btn icon style="align-self: center;"> -->
                <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
              <!-- </v-btn> -->

              <v-card class="d-inline-block mx-auto mt-8">
                <v-container>
                  <v-row justify="space-between">
                    <v-col cols="auto">
                      <v-img height="200" width="200" src="/poster-img.png"></v-img>
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
import Vue from 'vue'

export default {
  data() {
    return {
      dialog: false,
      title: "",
      content: "",
      info: [
        { name: "Type Something Here1", image: "Maybe an image here?1" },
        { name: "Type Something Here2", image: "Maybe an image here?2" }
      ]
    };
  },

  methods: {
    // TODO copy to Popup component
    submit() {
      this.dialog = false;
      console.log(this.title, this.content);
      //this.$emit("projectAdded"); //will be used to close snackbar in navbar component.

      const createMessage = {
        title: this.title,
        description: this.content,
        status: "Ongoing"
      };
      const createMessageJSON = JSON.stringify(createMessage);

      fetch("http://localhost:5000/create", {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "text/plain"
        },
        body: createMessageJSON
      })
        .then(response => response.json())
        .then(data => {
          // TODO receive id of project here!!
          console.log("from Dashboard - id = ", data.id)
          Vue.prototype.$currentProjectId = data.id

          this.$router.push("/newproject");
        })
        .catch(error => {
          console.error("Error:", error);
        });

    },

    cancel() {
      this.dialog = false;
      console.log("Cancel");
    }
  }
};
</script>

<style>
body {
  position: initial !important;
}
</style>

 


