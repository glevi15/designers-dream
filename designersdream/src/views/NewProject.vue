
<template>
  <div class="projects">
    <h1>Projects</h1>

    <v-row>
      <v-col xs6 sm4 md2 class></v-col>
      <v-col xs6 sm4 md2 class></v-col>
      <v-col xs6 sm4 md4 class>
        <v-tooltip>
          <template v-slot:activator="{ on }">
            <v-switch v-model="gridswitch" label="Grid" v-on="on"></v-switch>
          </template>
          <span>Changes the image preview</span>
        </v-tooltip>
      </v-col>
    </v-row>

    <v-container>
      <v-row no-gutters>
        <v-col class="px-12" cols="12" xs="12" sm="5">
          <div class="custom-navigation">
            <paintable
              :active="isActive"
              :horizontalNavigation="false"
              :navigation="navigation"
              :factor="x1"
              :lineWidth="3"
              :lineWidthEraser="25"
              :showLineWidth="false"
              :color="color"
              :width="500"
              :height="500"
              class="paint"
              ref="paintable"
              @toggle-paintable="toggledPaintable"
            >
              <div class="control">
                <h3>Paint</h3>
              </div>
            </paintable>
          </div>
          <canvas width="128" height="128" id="smallCanvas" style="display: none"> ></canvas>
          <img id="smallImg" style="display: none">
        </v-col>

        <v-col class sm="2">
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>
          <v-row class="mt-12"></v-row>

          <v-row class="mt-12">
            <v-col class="ml-8" cols="12" sm="8">
              <v-btn x-large color="primary" @click="loadImage()">
                GET IMAGE
                <v-icon>mdi-upload</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-col>

        <v-col class="px-12" cols="12" sm="5">
          <v-card class="d-inline-block mx-auto" outlined max-height="520" max-width="550">
            <v-container class="mt-6">
              <v-row justify="space-between">
                <img id="outImg" :src=outImageSrc>

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
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>

      <v-row class="ml-12">
        <v-col sm="4"></v-col>
        <v-col sm="4"></v-col>
        <v-col class="ml-5">
          <v-btn fab class="ml-12" icon>
            <v-icon x-large color="primary">mdi-arrow-left-bold</v-icon>
          </v-btn>

          <v-btn fab class="ml-12" icon>
            <v-icon x-large color="primary">mdi-arrow-right-bold</v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <v-row class="pr-6">
        <v-spacer></v-spacer>
        <v-col sm="3" class="pr-12 mr-12">
          <v-btn x-large shaped>
            SAVE IMAGE
            <v-icon x-large color="primary">mdi-content-save</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: [
      { title: "Facebook", icon: "mdi-facebook", route: "/" },
      { title: "Twitter", icon: "mdi-twitter", route: "/" },
      { title: "Instagram", icon: "mdi-instagram", route: "/" }
    ],
    outImageSrc: "",
    // smallImageSrc: "",
  }),

  methods: {
    convert(dataUrl) {
      // send data to backend via js fetch API
      const myData = { imageData: dataUrl };
      const myDataJSON = JSON.stringify(myData) 

      fetch('http://localhost:5000/convert', {
        method: 'POST',
        // mode: 'no-cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: myDataJSON,
      })
      .then((response) =>  response.json())
      .then((convertedData) => {
        let convertedImageData = convertedData.imageData
        // process convertedData sent back from server
        console.log('Success:', convertedData);

        // here we are setting Vue data and letting it handle the
        // DOM update. We could also receive the image element
        // and set the src ourselves
        this.outImageSrc = convertedImageData; 
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    },

    loadImage() {
      this.$refs.paintable.saveCurrentCanvasToStorage();

      // let myImg = document.getElementById("outImg");

      let dataUrl = this.$refs.paintable.getItem();
      
      let smallCanvas = document.getElementById("smallCanvas");
      let ctx = smallCanvas.getContext('2d');
      
      let smallImg = document.getElementById("smallImg");
      smallImg.src = dataUrl;

      smallImg.onload = () => {
        // this.smallImageSrc = dataUrl;

        ctx.save();
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, smallCanvas.width, smallCanvas.height);
        ctx.drawImage(smallImg, 0, 0, smallCanvas.width, smallCanvas.height);
        ctx.restore();

        let d = ctx.getImageData(0, 0, 128, 128);  // Get image Data from Canvas context
        const threshold = 128
        for (var i=0; i<d.data.length; i+=4) { // 4 is for RGBA channels
          d.data[i] = d.data[i+1] = d.data[i+2] = d.data[i+1] > threshold ? 255 : 0;
        }
  
        ctx.putImageData(d, 0, 0);  
        let smallDataURL = smallCanvas.toDataURL() 
  
      // Data olarak src yerine koymak yerine, direk id den src sine set edebiliriz. DİPNOT
        this.convert(smallDataURL);
      }      
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
</style>
