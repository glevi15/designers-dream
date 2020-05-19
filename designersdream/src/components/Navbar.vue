<template>
  <nav>
    <!--Snackbar is the pop-up that tells the project is succesfully created-->
      <v-snackbar v-model="snackbar" :timeout="4000" top >
          <span>Project created successfully.</span>
          <v-btn text color="white" @click="snackbar = false">Close</v-btn>
      </v-snackbar>

    <!--This is the bar on top of our screen -->
    <v-app-bar color="black" flat app>
      <v-app-bar-nav-icon class="white --text" @click="drawer = !drawer"></v-app-bar-nav-icon>
      
      <v-toolbar-title>
        <router-link class="font-weight-dark white--text" style="text-decoration:none;" :to="'/'">
        <span class="font-weight-light display-1">Designer's</span>
        <span class="display-1">Dream</span>
        </router-link>
        </v-toolbar-title>
    </v-app-bar>
    
    <!-- Side Panel -->
    <v-navigation-drawer app v-model="drawer" class="secondary">
      <v-layout column align-center>
        <v-flex class="mt-5">
          <v-avatar size="120">
            <img src="/ourlogo2.png" alt />
          </v-avatar>
          <p class="white--text subheading mt-4">Designer's Dream </p>
        </v-flex>

        <v-flex class="mt-4 mb-3">
          <Popup @projectAdded="snackbar = true"/>
        </v-flex>
      </v-layout>
      <v-list-shaped>
        <v-subheader class="white--text">MENU</v-subheader>
        <v-list-item-group v-model="item" color="primary">
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-item-action>
              <v-icon color="white">{{link.icon}}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="white--text">{{link.text}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list-shaped>
    </v-navigation-drawer>
    
  </nav>
</template>


<script>
import Popup from "./Popup";

export default {
  components: { Popup },

  data() {
    return {
      drawer: false,
      links: [
        { icon: "dashboard", text: "Dashboard", route: "/" },

       // { icon: "edit", text: "New Project", route: "/newproject" },
        { icon: "create_new_folder", text: "My Projects", route: "/projects" },
        //Added test for testing purposes
       // { icon: "folder", text: "Test Area", route: "/test" }
      ],
      snackbar: false
    };
    
  }
};
</script>



      