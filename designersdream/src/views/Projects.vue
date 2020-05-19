<template>
  <div class="PROJECTS">
    <p class="display-2 font-italic pt-8 mx-12 pl-5 yellow--text text--lighten-3">Projects</p>

    <v-container class="my-5">
      <v-layout row class="mb-3 justify-end">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small color="yellow" v-on="on" @click="sortBy('title')">
              <v-icon left small>folder</v-icon>
              <span class="caption yellow--text text-lowercase text--lighten-3">by project name</span>
            </v-btn>
          </template>
          <span>orders projects by project name</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small color="yellow" v-on="on" @click="sortBy('status')" class="mr-4">
              <v-icon left small>offline_pin</v-icon>
              <span class="caption yellow--text text-lowercase text--lighten-3">by status</span>
            </v-btn>
          </template>
          <span>orders projects by project status</span>
        </v-tooltip>
      </v-layout>

      <v-expansion-panels hover >
        <v-expansion-panel 
          v-for="project in displayedProjects"
          :key="project.title"
          @click="setSelected(project.id)"
        >
          <v-layout row wrap :class="`pa-3 project ${project.status}`">
            <v-expansion-panel-header>
              <v-flex xs12 md6>
                <div class="caption grey--text">Project title</div>
                <div>{{project.title}}</div>
              </v-flex>

              <v-flex xs6 sm4 md2></v-flex>
              <v-flex xs6 sm4 md2></v-flex>

              <v-flex xs6 sm4 md2>
                <div class="text-right">
                  <v-chip
                    small
                    :color="`${project.status}`"
                    :class="`v-chip--active white--text caption my-2`"
                    @click="toggleStatus(project.id)"
                  >{{project.status}}</v-chip>
                </div>
              </v-flex>
            </v-expansion-panel-header>
          </v-layout>
          <v-expansion-panel-content>
            <v-card>
              <v-row>
              <v-col>
              <v-card-text class="px-4 dark--text">
                <div class="font-weight-bold">Information</div>
                <div>{{project.description}}</div>
                
                <v-row class="pt-2">
                  <v-card outlined class="ml-6">
                    <img height="256" width="256" v-bind:src="project.sketchImage"/> 
                  </v-card>

                  <v-card outlined class="ml-12">
                    <img height="256" width="256"  v-bind:src="project.resultImage"/>
                  </v-card>
                </v-row>
              </v-card-text>
              </v-col>
              <v-col class="text-right" style="position: absolute; bottom: 1em;">
                    <v-btn color="primary" class="ml-10" @click="openProject()">
                    <span class="caption">Open</span>
                  </v-btn>

                  <v-snackbar v-model="snackbar" :timeout="4000" bottom>
                    <span>Project deleted successfully.</span>
                    <v-btn text color="white" @click="snackbar = false">Close</v-btn>
                  </v-snackbar>

                  <v-btn
                    color="primary"
                    class="ml-10"
                    @click="deleteProject()"
                    :loading="loading"
                  >
                    <v-icon left small>delete</v-icon>
                    <span class="caption">Delete</span>
                  </v-btn>

                  <v-btn color="primary" class="ml-10 text-right" @click="downloadProject()">
                    <v-icon left small>cloud_download</v-icon>
                    <span class="caption">Download</span>
                  </v-btn>
                  </v-col>
                  </v-row>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </div>
</template>

<script>
import Vue from "vue";
import JSZip from "jszip";
import { saveAs } from "file-saver";

export default {
  mounted() {
    fetch("http://localhost:5000/projects", {
      method: "GET"
      // mode: 'no-cors',
    })
      .then(response => response.json())
      .then(data => {
        this.projects = data.projects;
        return data;
      })
      .then(data => {
        Object.keys(data.projects).map(id => {
          if (data.projects[id]) {
            this.displayedProjects.push(data.projects[id]);
          }
        });
      })
      .catch(error => {
        console.error("Error:", error);
      });
  },

  data() {
    return {
      currentSelectedId: -1,
      projects: {},
      displayedProjects: [],
      loading: false,
      snackbar: false
    };
  },

  methods: {
    sortBy(property) {
      this.displayedProjects.sort((a, b) =>
        a[property] < b[property] ? -1 : 1
      );
    },

    setSelected(id) {
      this.currentSelectedId = id;
    },

    toggleStatus(id) {
      console.log(id);
      let newStatus =
        this.projects[id].status == "Ongoing" ? "Done" : "Ongoing";
      fetch("http://localhost:5000/status", {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "text/plain"
        },
        body: JSON.stringify({
          id: id,
          status: newStatus
        })
      })
        .then(response => {
          if (response.status == 200) {
            this.projects[id].status = newStatus;
          }
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },

    openProject() {
      Vue.prototype.$currentProjectId = this.currentSelectedId;

      this.$root.$data.sketchImage = this.projects[
        this.currentSelectedId
      ].sketchImage;
      this.$root.$data.resultImage = this.projects[
        this.currentSelectedId
      ].resultImage;

      this.$router.push("/newproject");
    },

    downloadProject() {
      var zip = new JSZip();
      var img = zip.folder("images");

      let projectName = this.projects[this.currentSelectedId].title;
      let sketchImage = this.projects[this.currentSelectedId]["sketchImage"];
      let sketch = sketchImage.replace("data:image/png;base64,", "");

      let resultImage = this.projects[this.currentSelectedId]["resultImage"];
      let design = resultImage.replace("data:image/png;base64,", "");

      img.file("sketch.png", sketch, { base64: true });
      img.file("design.png", design, { base64: true });

      zip.generateAsync({ type: "blob" }).then(function(content) {
        saveAs(content, projectName + ".zip");
      });
    },

    deleteProject() {
      this.loading = true;

      fetch("http://localhost:5000/delete", {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "text/plain"
        },
        body: JSON.stringify({
          id: this.currentSelectedId
        })
      })
        .then(response => {
          if (response.status == 200) {
            for (let i = 0; i < this.displayedProjects.length; i++) {
              if (this.displayedProjects[i].id == this.currentSelectedId) {
                this.displayedProjects.splice(i, 1);
                this.loading = false;
                this.snackbar = true;
                break;
              }
            }
          }
        })
        .then(() => {
          console.log(this.displayedProjects);
        })
        .catch(error => {
          console.error("Error:", error);
        });
    }
  }
};
</script>

<style>
.project.Done {
  border-left: 12px solid #8bc34a;
}

.project.Ongoing {
  border-left: 12px solid #039be5;
}

.v-chip.Done {
  background: #8bc34a;
}

.v-chip.Ongoing {
  background: #039be5;
}
</style>