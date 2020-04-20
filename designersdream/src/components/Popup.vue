<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on }">
        <v-btn color="success" dark v-on="on"> Add New Project </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>
          Create New Project
        </v-card-title>

        <v-card-text>
          <v-form class="px-3">
            <v-text-field label="Title" v-model="title" prepend-icon="folder"></v-text-field>
            <v-textarea label="Information" v-model="content" prepend-icon="edit"></v-textarea>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            :to="'/newproject'"
            @click="submit()"
          >
            Create
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
     data () {
      return {
        dialog: false,
        title: '',
        content: '',
      }
    },
      methods: {
        submit() {
          this.dialog = false,
          console.log(this.title,this.content)
        }
      }
}
</script>