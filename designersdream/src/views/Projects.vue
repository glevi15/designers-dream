<template>
  <div class="PROJECTS">
    <h1>Projects</h1>

    <v-container class="my-5">
      <v-layout row class="mb-3 justify-end">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small color="grey" v-on="on" @click="sortBy('title')">
              <v-icon left small>folder</v-icon>
              <span class="caption text-lowercase">by project name</span>
            </v-btn>
          </template>
          <span>orders projects by project name</span>
        </v-tooltip>

        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn text small color="grey" v-on="on" @click="sortBy('status')">
              <v-icon left small>offline_pin</v-icon>
              <span class="caption text-lowercase">by status</span>
            </v-btn>
          </template>
          <span>orders projects by project status</span>
        </v-tooltip>
      </v-layout>

      <v-expansion-panels outlined hover popout="true">
        <v-expansion-panel
          v-for="project in projects"
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
              <v-card-text class="px-4 dark--text">
                <div class="font-weight-bold">Information</div>
                <div>{{project.description}}</div>
                <div>
                  <img height="128" width="128" v-bind:src="project.sketchImage" />
                  <img height="128" width="128" v-bind:src="project.resultImage" />
                </div>
              </v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-btn color="primary" class="my-6 ml-10" @click="openProject()">
        <span class="caption">Open</span>
      </v-btn>

      <v-btn color="primary" class="my-6 ml-10">
        <v-icon left small>delete</v-icon>
        <span class="caption">Delete</span>
      </v-btn>

      <v-btn color="primary" class="my-6 ml-10">
        <v-icon left small>cloud_download</v-icon>
        <span class="caption">Download</span>
      </v-btn>
    </v-container>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  mounted() {
    fetch("http://localhost:5000/projects", {
      method: "GET"
      // mode: 'no-cors',
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        this.projects = data.projects;
      })
      .catch(error => {
        console.error("Error:", error);
      });
  },

  data() {
    return {
      currentSelectedId: -1,
      projects: [
        //   {
        //     title: "My project #1",
        //     status: "Done",
        //     src: "/handbag.png",
        //     src2: "/handbag.png",
        //     content:
        //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sollicitudin mauris eu nulla accumsan, vitae luctus nisl egestas."
        //   },
        //   {
        //     title: "My project #2",
        //     status: "Ongoing",
        //     src: "/handbag1.png",
        //     content:
        //       "Aliquam id est diam. Integer viverra placerat porta. Nam eget pellentesque libero. Morbi vestibulum sem iaculis sagittis pulvinar. Donec"
        //   },
        //   {
        //     title: "My project #3",
        //     status: "Done",
        //     src: "/handbag2.png",
        //     content:
        //       "diam mauris, tempus vel finibus sed, consectetur et tellus. Vivamus laoreet justo vitae dui tincidunt, at placerat nibh bibendum. Vivamus"
        //   },
        //   {
        //     title: "My project #4",
        //     status: "Done",
        //     src: "/handbag3.png",
        //     content:
        //       "fringilla diam sed mi semper bibendum. Nulla justo sapien, sollicitudin vitae hendrerit bibendum, tempus nec ex. Aliquam felis quam,"
        //   },
        //   {
        //     title: "My project #5",
        //     status: "Ongoing",
        //     src: "/handbag1.png",
        //     content:
        //       "convallis sed leo sit amet, auctor pharetra ligula. Vestibulum in augue ac ex tristique blandit vitae nec enim. Ut aliquet risus vitae erat"
        //   },
        //   {
        //     title: "My project #6",
        //     status: "Done",
        //     src: "/handbag2.png",
        //     content:
        //       "convallis ornare. Vestibulum eget orci sed quam laoreet fermentum vel sollicitudin arcu. Pellentesque sed metus sem. Vivamus libero nisl, scelerisque sed ultrices eu, posuere sit amet leo."
        //   }
      ]
    };
  },
  methods: {
    sortBy(property) {
      this.projects.sort((a, b) => (a[property] < b[property] ? -1 : 1));
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
      this.$router.push("/newproject");
    }
  }
};
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