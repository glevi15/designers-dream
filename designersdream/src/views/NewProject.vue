
<template>
  <div class="projects">

    <v-container class="mx-12 pt-12 mt-12">
      <v-row no-gutters>
        <v-col class="px-12" cols="12" xs="12" sm="5">
          <div class="custom-navigation" style="background: none;">
            <!-- Paintable canvas -->
            <paintable style="background: #fff;"
              :active="paintableActive"
              :horizontalNavigation="true"
              :navigation="navigation"
              :factor="x1"
              :lineWidth="3"
              :lineWidthEraser="25"
              :useEraser="useEraser"
              :showLineWidth="false"
              :color="black"
              :colors="false"
              :width="500"
              :height="500"
              class="paint"
              ref="paintable"
              @toggle-paintable="true"
            >
              <div class="control">
                <h3>Paint</h3>
              </div>
            </paintable>
          </div>
          <!--Paintable ends here -->
          <canvas width="128" height="128" id="smallCanvas" style="display: none">></canvas>
          <!-- invisible canvas to scale the image-->
          <img id="smallImg" style="display: none" />
          <!-- invisible image to scale the image inside the invisible canvas-->
        </v-col>

        <v-col class sm="2">
          <!-- GET IMAGE BUTTON -->
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>

          <v-row class="mt-12">
            <v-col class="ml-8" cols="12" sm="8">
              <v-btn
                x-large
                color="primary"
                @click="loadImage();buttonEnabler=false"
                :loading="imageLoading"
              >
                <!-- Our loadImage function is assigned to the onclick of the Get Image Button -->
                GET IMAGE
                <v-icon>mdi-upload</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

        <v-col class="px-12" cols="12" sm="5">
          <v-card class="d-inline-block mx-auto mt-4" width="500" height="500">
            <v-container>
              <v-row justify="space-between">
                <img id="outImg" :src="outImageSrc" width="500" height="500" />

                <!-- SHARE BUTTON ENDS HERE -->
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>

      <v-snackbar v-model="saveSnackbar" :timeout="4000" bottom>
        <span>Project saved successfully.</span>
        <v-btn text color="white" @click="saveSnackbar = false">Close</v-btn>
      </v-snackbar>

      <v-row class="pr-12 mr-12">
        <!-- SAVE IMAGE BUTTON / WORK-IN-PROGRESS / WILL BE USED TO UPLOAD THE PROJECTS TO DATABASE-->
        <v-spacer></v-spacer>
        <v-col sm="3" class="pr-12 mr-12">
          <v-btn x-large shaped text>
            <v-icon
              x-large
              @click="saveImage()"
              color="primary"
              :loading="saveLoading"
            >mdi-content-save</v-icon>
          </v-btn>

          <!-- DOWNLOAD BUTTON -->
          <v-btn
            x-large
            text
            color="primary"
            @click="downloadImage()"
            id="downloadButton"
            :disabled="buttonEnabler"
          >
            <v-icon x-large>cloud_download</v-icon>
          </v-btn>

          <v-menu bottom right offset-x>
            <!--SHARE BUTTON -->
            <template v-slot:activator="{ on }">
              <v-btn x-large text icon v-on="on">
                <v-icon color="primary">mdi-share-variant</v-icon>
              </v-btn>
            </template>

            <v-card class="mx-auto" max-width="300" tile>
              <v-list>
                <v-list-item-group v-model="item" color="primary">
                  <v-list-item v-for="(item, i) in items" :key="i">
                    <v-list-item-icon>
                      <v-icon color="primary" v-text="item.icon"></v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                      <!-- düğme konucaksa on click, buna konacak -->
<ShareNetwork 
    :network="item.title"
    url="https://aavci123.wixsite.com/designers-dream"
    title="Check out Designer's Dream!"
    description="Our capstone design project for COMP 491 turns your clothing designs into reality!"
    quote=""
    hashtags="designersdream"
  > {{item.title}}
</ShareNetwork>

                      <!-- <v-list-item-title v-text="item.title"></v-list-item-title> -->
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-card>
          </v-menu>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import func from '../../vue-temp/vue-editor-bridge';
export default {
  data: () => ({
    saveLoading: false,
    saveSnackbar: false,
    imageLoading: false,
    items: [
      { title: "Facebook", icon: "mdi-facebook", route: "/" },
      { title: "Twitter", icon: "mdi-twitter", route: "/" },
      { title: "Reddit", icon: "mdi-reddit", route: "/" },
      // { title: "Instagram", icon: "mdi-instagram", route: "/" }
    ],
    sketchImageSrc: "",
    outImageSrc: "",
    buttonEnabler: true,
    paintableActive: false
    // smallImageSrc: "",
  }),

  beforeRouteLeave(to, from, next) {
    // called when the route that renders this component is about to
    // be navigated away from.
    // has access to `this` component instance.
    console.log(to,from,next)
    this.$refs.paintable.removeItem()

    this.$root.$data.resultImage = "";
    this.$root.$data.sketchImage = "";

    next()
  },

  mounted() {
    console.log("from NewProject.vue");
    //this.$currentProjectId
    this.paintableActive = false;
    this.$refs.paintable.setItem(undefined, this.$root.$data.sketchImage);
    this.$refs.paintable.undoDrawingStep();
    this.paintableActive = true;

    this.outImageSrc = this.$root.$data.resultImage;
  },

  methods: {
    convert(dataUrl) {
      // send data to backend via js fetch API
      const myData = { imageData: dataUrl };
      const myDataJSON = JSON.stringify(myData);

      fetch("http://localhost:5000/convert", {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "application/json"
        },
        body: myDataJSON
      })
        .then(response => response.json())
        .then(convertedData => {
          let convertedImageData = convertedData.imageData;
          // process convertedData sent back from server
          console.log("Successfully converted image");

          // here we are setting Vue data and letting it handle the
          // DOM update. We could also receive the image element
          // and set the src ourselves
          this.outImageSrc = convertedImageData;

          this.imageLoading = false;
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },

    downloadImage() {
      var image = this.outImageSrc.replace("image/png", "image/octet-stream");
      var link = document.createElement("a");
      link.download = "my-design.png";
      link.href = image;
      link.click();
    },

    saveImage() {
      console.log("Save image to database");
      this.saveLoading = true;
      const saveMessage = {
        id: this.$currentProjectId,
        sketchImage: this.sketchImageSrc,
        resultImage: this.outImageSrc
      };
      const saveMessageJson = JSON.stringify(saveMessage);

      fetch("http://localhost:5000/save", {
        method: "POST",
        // mode: 'no-cors',
        headers: {
          "Content-Type": "text/plain"
        },
        body: saveMessageJson
      })
        .then(response => response.json())
        .then(convertedData => {
          // TODO receive id of project here!!
          console.log(convertedData);
          this.saveLoading = false;
          this.saveSnackbar = true;
        })
        .catch(error => {
          console.error("Error:", error);
        });
    },

    loadImage() {
      this.$refs.paintable.saveCurrentCanvasToStorage();
      this.imageLoading = true;
      // let myImg = document.getElementById("outImg");

      let dataUrl = this.$refs.paintable.getItem();
      this.sketchImageSrc = dataUrl;

      let smallCanvas = document.getElementById("smallCanvas");
      let ctx = smallCanvas.getContext("2d");

      let smallImg = document.getElementById("smallImg");
      smallImg.src = dataUrl;

      smallImg.onload = () => {
        // this.smallImageSrc = dataUrl;

        ctx.save();
        ctx.fillStyle = "white";
        ctx.fillRect(0, 0, smallCanvas.width, smallCanvas.height);
        ctx.drawImage(smallImg, 0, 0, smallCanvas.width, smallCanvas.height);
        ctx.restore();

        let d = ctx.getImageData(0, 0, 128, 128); // Get image Data from Canvas context
        const threshold = 128;
        for (var i = 0; i < d.data.length; i += 4) {
          // 4 is for RGBA channels
          d.data[i] = d.data[i + 1] = d.data[i + 2] =
            d.data[i + 1] > threshold ? 255 : 0;
        }

        ctx.putImageData(d, 0, 0);
        let smallDataURL = smallCanvas.toDataURL();

        // Data olarak src yerine koymak yerine, direk id den src sine set edebiliriz. DİPNOT
        this.convert(smallDataURL);
      };
    }
  },

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
</script>

<!-- STYLING FOR THE PAINTABLE CANVAS -->
<style>
.control {
  margin: 10px;
}
.paint {
  border: 5px solid #000;
  border-radius: 5px;
  margin: 20px auto;
  box-sizing: border-box;
  display: block;
  border-radius: 25px;
  width: 510px !important;
  height: 510px !important;
  position: relative !important;
  overflow: hidden;
}

.custom-navigation {
  position: static;
  top: 160px;
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

#outImg[src=""] {
  display: none;
}

#outImg[src="data*"] {
  display: block;
}
</style>
