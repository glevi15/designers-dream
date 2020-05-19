<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on }">
        <v-btn color="success" dark v-on="on">Add New Project</v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>Create New Project</v-card-title>

        <v-card-text>
          <v-form class="px-3">
            <v-text-field label="Title" v-model="title" prepend-icon="folder"></v-text-field>
            <v-textarea label="Information" v-model="content" prepend-icon="edit"></v-textarea>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn color="success" text @click="cancel()">Cancel</v-btn>
          <v-spacer></v-spacer>
          <v-btn color="primary" text :to="'/newproject'" @click="submit()">Create</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  data() {
    return {
      dialog: false,
      title: "",
      content: ""
    };
  },
  methods: {
    submit() {
      this.dialog = false;
      //console.log(this.title, this.content);
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
          console.log("from Dashboard - id = ", data.id);
          Vue.prototype.$currentProjectId = data.id;


          this.$emit("projectAdded")

          this.$router.push("/newproject");
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },
    cancel() {
      this.dialog = false;
    }
  }
};
</script>