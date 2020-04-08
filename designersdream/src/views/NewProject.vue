<template>
  <div class ="projects">
    <h1>Projects</h1>
  <v-container fill-height>
    <v-row no-gutters>
      <v-col class= "pt-12 px-12" cols="12" xs="12" sm="5">
          <div class="custom-navigation"> 
            <paintable id="Genco"
              :active="isActive"
              :width="500"
              :height="500"
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
                <h3>
                  Paint
                </h3>
              </div> 
            </paintable>
          </div>
      </v-col>

      <v-col class="pt-12" sm="2">
        <v-card height = "100" width = "1200" class="pa-2 white" flat tile>
                 
          <v-flex class="mt-12 pt-12 pl-2 ml-12" >

            <v-btn x-large color="success" dark>
              Get Image
              <v-icon center>play_arrow</v-icon>
            </v-btn>

          </v-flex>

          <v-flex class="mt-12 pt-12 pl-2 ml-12" >

             <v-btn class="ml-12 mb-3" small color="success" dark>
              Twitter
            </v-btn>

            <v-layout row wrap>
              <v-btn class="mr-2" small color="success" dark>
              Facebook
            </v-btn>

            <v-btn small color="success" dark>
              Instagram
            </v-btn>

            </v-layout>           
          </v-flex>

        </v-card>
      </v-col>

      <v-col class="pt-12 px-12" cols="12" sm="5">
        <v-card class="d-inline-block mx-auto" shaped>
          <v-container>
            <v-row justify="space-between">
              <v-col cols="auto">
                <v-img
                  height="510"
                  width="510"
                  src="https://rukminim1.flixcart.com/image/832/832/jjylw280/bag/y/3/f/trendy-designer-luxury-handbag-italian-design-with-sling-bag-original-imaf7fynf3mmhhav.jpeg?q=70"
                ></v-img>
              </v-col>
              <v-col cols="auto" class="text-center pl-0">

              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>

    </v-row>
  </v-container>

  </div>
</template>

<script>
export default {
    computed: {
    navigation() {
      return {
        'draw-save': {
          body: 'TOOLS!',
          activeBody: '<strong>save</strong>'
        },
        color: {
          body: 'color'
        },
        redo: {
          activeBody : false
        }
      };
    }
  },
  
}
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
  position: fixed;
  top: 160px;
  left: 100px;
  z-index: 1;
  background-color: #fff;
}

.get-images{
  border: 2px solid #000;
  background-color:#30f;
  border-radius: 1px;
  position: fixed;
  height: 50px;
  width: 100px;
  top: 300px;
  left: 630px;
}

.share{
  position: fixed;
  top: -100px;
  left: 960px;
}

</style>
