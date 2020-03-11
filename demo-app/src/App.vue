<template>
<div>
    <div class="custom-navigation">
      <div class="controls" v-if="isActive">
        {{ dynamicLineWidth }}px<br />
        <input
          type="range"
          @input="dynamicLineWidth = +$event.target.value"
          min="1"
          max="100"
        />
        <input type="color" v-model="color" /><br /><br />
        
        <button @click="$refs.paintable.undoDrawingStep">undo</button>
        <button @click="$refs.paintable.redoDrawingStep">redo</button>
        <button @click="$refs.paintable.clearCanvas">clear</button>
        <button @click="$refs.paintable.saveCurrentCanvasToStorage">
          save
        </button>
        <button @click="$refs.paintable.cancelDrawing">cancel</button>
        <button @click="useEraser = !useEraser">
          {{ !useEraser ? 'eraser' : 'pencil' }}
        </button>
      </div>
      
    <paintable
      :active="isActive"
      :width="800"
      :height="800"
      :hide="hidePaintable"
      :horizontalNavigation="true"
      :navigation="navigation"
      :factor="1"
      :lineWidth="dynamicLineWidth"
      :lineWidthEraser="20"
      :useEraser="useEraser"
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
  <v-card
    class="mx-auto overflow-hidden"
    height="600"
  >
    <v-app-bar
      color="deep-purple"
      dark
    >
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title>Designer's Dream</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>New Project</v-list-item-title>
            <v-list-item-icon>
              <v-icon>mdi-pencil</v-icon>
            </v-list-item-icon>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>My Projects</v-list-item-title>
            <v-list-item-icon>
              <v-icon>mdi-folder</v-icon>
            </v-list-item-icon>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</div>
</template>


<script>
export default {
  data() {
    return {
      isActive: false,
      useEraser: false,
      drawer: false,
      color: '#000',
      links: [
        {text:'New Project', icon: 'pencil', route: '/'},
        {text:'My Projects', icon: 'folder', route: '/MyProjects'}
      ]
    };
  },
  computed: {
    navigation() {
      return {
        'draw-save': {
          body: 'click here!',
          activeBody: '<strong>save</strong>'
        },
        color: {
          body: 'color'
        }
      };
    }
  },

};
</script>

<style>
body {
  font-family: Helvetica, Arial, sans-serif;
  position: initial !important;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.control {
  margin: 20px;
}
.paint {
  border: 5px solid #000;
  border-radius: 5px;
  margin: 20px auto;
  box-sizing: border-box;
  display: block;
  width: 810px !important;
  height: 510px !important;
  position: relative !important;
  overflow: hidden;
}
footer {
  text-align: center;
}
footer a {
  color: #777;
  text-transform: uppercase;
  text-decoration: none;
}
button {
  border: 0;
  margin: 0 10px 0 0;
  font-size: 14px;
  padding: 10px 15px;
  opacity: 0.8;
  background-color: rgb(19, 102, 141);
  border-radius: 3px;
  color: #fff;
  cursor: pointer;
}
button:hover {
  opacity: 1;
}
.custom-navigation {
  position: fixed;
  top: 70px;
  left: 260px;
  z-index: 1001;
  background-color: #fff;
}
.custom-navigation .controls {
  margin: 10px 0 0 0;
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 5px;
}
</style>

