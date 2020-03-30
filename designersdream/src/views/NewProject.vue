<template>
  <div class ="projects">
    <h1>Projects</h1>

    <v-container class = "my-5">
      <v-layout row wrap justify-space-between>
        <v-flex xs12 md3>
          <v-btn outline block class="primary">test</v-btn>
        </v-flex>
        <v-flex xs12 md3>
          <v-btn outline block class="success">henlo</v-btn>
        </v-flex>
        <v-flex xs12 md3>
          <v-btn outline block class="primary">test</v-btn>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-space-around>
        <v-flex xs12 md4>
          <v-btn outline block class="success">henlo</v-btn>
        </v-flex>

        <v-flex xs12 md4>
          <v-btn outline block class="success">henlo</v-btn>
        </v-flex>
      </v-layout>

    </v-container>

    <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-row :align="alignment" :justify="justify" class="grey lighten-5" style="height: 300px;">
          <v-card class="ma-3 pa-6" outlined tile>
            Column
          </v-card>

          <v-card class="ma-3 pa-6" outlined tile>
            Column
          </v-card>

        </v-row>
      </v-col>
      <v-col cols="12">
        <v-row justify="center">
          <v-col cols="6" d="2">
            <v-select v-model="alignment" :items="alignmentsAvailable" label="Align"></v-select>
          </v-col>

          <v-col cols="6" md="2">
            <v-select v-model="justify" :items="justifyAvailable"  label="Justify" ></v-select>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>

<script>
export default {
  
}
</script>