<template>
  <v-container class>
    <!-- ROW #1 -->
    <v-row no-gutters>
      <v-col order="last">
        <v-card class="pa-2" outlined tile>First, but last</v-card>
      </v-col>
      <v-col>
        <v-card class="pa-2" outlined tile>Second, but unordered</v-card>
      </v-col>
      <v-col order="first">
        <v-card class="pa-2" outlined tile>Third, but first</v-card>
      </v-col>
    </v-row>

    <!-- ROW #2 -->

    <v-row class="pt-12">
      <v-col order="last">
        <v-card class="pa-2" outlined tile>First, but last</v-card>
      </v-col>
      <v-col>
        <v-card class="pa-2" outlined tile>Second, but unordered</v-card>
      </v-col>
      <v-col order="first">
        <v-card class="pa-2" outlined tile>Third, but first</v-card>
      </v-col>
    </v-row>

    <!-- TEST ROW -->

    <v-row>
      <v-col cols="12" class>
        <v-row :align="alignment" :justify="justify" class="lighten-5" style="height: 500px;">
          <div class="custom-navigation">
            <paintable
              :active="isActive"
              :horizontalNavigation="false"
              :navigation="navigation"
              :factor="x1"
              :lineWidth="dynamicLineWidth"
              :lineWidthEraser="5"
              :showLineWidth="false"
              :color="color"
              class="paint"
              ref="paintable"
              @toggle-paintable="toggledPaintable"
            >
              <div class="control">
                <h3>Paint</h3>
              </div>
            </paintable>
          </div>

          <v-col class="ma-5" sm="2" align="center">
            <v-btn x-large color="primary">
              GET IMAGE
              <v-icon>mdi-upload</v-icon>
            </v-btn>
          </v-col>

          <v-card class="ma-3 pa-6" outlined tile xs6 sm4 md2>
            <v-img
              class="ml-12"
              height="480"
              width="480"
              src="https://rukminim1.flixcart.com/image/832/832/jjylw280/bag/y/3/f/trendy-designer-luxury-handbag-italian-design-with-sling-bag-original-imaf7fynf3mmhhav.jpeg?q=70"
            ></v-img>
          </v-card>
        </v-row>
      </v-col>
    </v-row>

    <v-row>
      <v-col class="pt-12 mt-12" sm="3"></v-col>
      <v-col class="pt-12 mt-12" sm="4"></v-col>
      <v-col order="last" class="pt-2 mt-12" sm="4" align="center">
        <v-btn fab class="ml-6" icon>
          <v-icon x-large color="primary">mdi-arrow-left-bold</v-icon>
        </v-btn>

        <v-menu bottom right offset-x>
          <template v-slot:activator="{ on }">
            <v-btn x-large class icon v-on="on">
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>
          </template>

          <v-card class="mx-auto" max-width="300" tile>
            <v-list>
              <v-list-item-group v-model="item" color="primary">
                <v-list-item v-for="(item, i) in items" :key="i">
                  <v-list-item-icon>
                    <v-icon v-text="item.icon"></v-icon>
                  </v-list-item-icon>

                  <v-list-item-content>
                    <v-list-item-title v-text="item.title"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card>
        </v-menu>

        <v-btn fab icon class="mr-12">
          <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
        </v-btn>

        <v-dialog v-model="dialog" width="500">
          <template v-slot:activator="{ on }">
            <v-btn color="success" dark v-on="on">AYÇA</v-btn>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2" primary-title>Save Project</v-card-title>

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
              <v-btn color="primary" text @click="submit()">Create</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>

    
<script>
export default {
  data() {
    return {
      alignment: "center",
      justify: "center",
      dialog: false,
      title: "",
      content:"",
      items: [
        { title: "Facebook", icon: "mdi-facebook", route: "/" },
        { title: "Twitter", icon: "mdi-twitter", route: "/" },
        { title: "Instagram", icon: "mdi-instagram", route: "/" }
      ],

      computed: {
        navigation() {
          return {
            "draw-save": {
              body: "TOOLS!",
              activeBody: "<strong>save</strong>"
            },
            color: {
              body: "color"
            },
            redo: {
              activeBody: false
            }
          };
        }
      }
    };
  },

  methods: {
    submit() {
      (this.dialog = false), console.log(this.title, this.content); 
      this.$emit("projectAdded"); //will be used to close snackbar in navbar component.
    },
    cancel() {
      (this.dialog = false);
    }
  }
};
</script>


<style>
.control {
  margin: 20px;
}
.paint {
  border: 5px solid #000;
  border-radius: 5px;
  margin: 10px auto;
  box-sizing: content-box;
  display: block;
  border-radius: 25px;
  width: 510px !important;
  height: 510px !important;
  position: relative !important;
  overflow: hidden;
}

.custom-navigation {
  position: static;
  top: 180px;
  left: 240px;
  z-index: 1;
  background-color: #fff;
}

.get-images {
  border: 2px solid #000;
  background-color: #30f;
  border-radius: 1px;
  position: fixed;
  height: 50px;
  width: 100px;
  top: 300px;
  left: 630px;
}

.share {
  position: fixed;
  top: -100px;
  left: 960px;
}
</style>
