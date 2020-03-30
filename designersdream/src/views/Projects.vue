<template>
  <div class ="projects">
    <h1>Projects</h1>

    <v-container class = "my-5">

      <v-layout row class="mb-3 justify-end">

        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small flat color="grey" v-on ="on" @click="sortBy('title')">
              <v-icon left small>folder</v-icon>
              <span class="caption text-lowercase">by project name</span>
            </v-btn>
        </template>
        <span>orders projects by project name</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small flat color="grey" v-on ="on" @click="sortBy('status')">
              <v-icon left small>offline_pin</v-icon>
              <span class="caption text-lowercase">by status</span>
            </v-btn>
        </template>
        <span>orders projects by project status</span>
        </v-tooltip>
           
      </v-layout>

      <v-card outlined hover v-for="project in projects" :key="project.title">
        <v-layout row wrap :class="`pa-3 project ${project.status}`">
          <v-flex xs12 md6>
            <div class="caption grey--text">Project title</div>
            <div>{{project.title}}</div>
          </v-flex>

          <v-flex xs6 sm4 md2>
             <div class="caption grey--text">Person</div>
             <div>{{project.person}}</div>
          </v-flex>

          <v-flex xs6 sm4 md2>
             <div class="caption grey--text">Last Changed</div>
             <div>{{project.lastchanged}}</div>
          </v-flex>
          <v-flex xs6 sm4 md2>
             <div class="text-right">
               <v-chip small :color="`${project.status}`" :class="`v-chip--active white--text caption my-2`">{{project.status}}</v-chip>
             </div>
          </v-flex>

        </v-layout>
      </v-card>

      

        <v-btn small flat color="primary"  class="my-6 ml-10">
          <span class="caption">Select</span>
        </v-btn>

        <v-btn small flat color="primary"  class="my-6 ml-10">
          <v-icon left small>delete</v-icon>
          <span class="caption">Delete</span>
        </v-btn>

        <v-btn small flat color="primary" class="my-6 ml-10">
          <v-icon left small>cloud_download</v-icon>
          <span class="caption">Download</span>
        </v-btn>

      

    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      projects: [
        { title: 'My project #1', person: 'İhsan Yazıcı', lastchanged: '28.03.2020', status: 'Done',content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin mauris eu nulla accumsan, vitae luctus nisl egestas.'},
        { title: 'My project #2', person: 'Dursun Bekci', lastchanged: '20.03.2020', status: 'Ongoing',content : 'Aliquam id est diam. Integer viverra placerat porta. Nam eget pellentesque libero. Morbi vestibulum sem iaculis sagittis pulvinar. Donec'},
        { title: 'My project #3', person: 'Ayça Avcı'   , lastchanged: '22.03.2020', status: 'Done',content : 'diam mauris, tempus vel finibus sed, consectetur et tellus. Vivamus laoreet justo vitae dui tincidunt, at placerat nibh bibendum. Vivamus'},
        { title: 'My project #4', person: 'İhsan Yazıcı', lastchanged: '21.02.2020', status: 'Done',content : 'fringilla diam sed mi semper bibendum. Nulla justo sapien, sollicitudin vitae hendrerit bibendum, tempus nec ex. Aliquam felis quam,'},
        { title: 'My project #5', person: 'Genco Levi'  , lastchanged: '12.01.2020', status: 'Ongoing',content : 'convallis sed leo sit amet, auctor pharetra ligula. Vestibulum in augue ac ex tristique blandit vitae nec enim. Ut aliquet risus vitae erat'},
        { title: 'My project #6', person: 'Genco Levi'  , lastchanged: '23.03.2020', status: 'Done',content : 'convallis ornare. Vestibulum eget orci sed quam laoreet fermentum vel sollicitudin arcu. Pellentesque sed metus sem. Vivamus libero nisl, scelerisque sed ultrices eu, posuere sit amet leo.'}
      ]
    }
  },
  methods: {
    sortBy(property){
      this.projects.sort((a,b) => a[property] < b[property] ? -1 : 1)
    }
  }  
}
</script>

<style>
.project.Done {
  border-left: 12px solid #20dd0f;
}

.project.Ongoing {
  border-left: 12px solid #311b92;
}

.v-chip.Done {
  background: #20dd0f;
}

.v-chip.Ongoing {
  background: #311b92;
}
</style>