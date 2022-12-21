<template>
  <h2>Life Game</h2>
    <div class="container">
    <div>
      <form>
        <label>length:&emsp;</label>
        <input v-if="!gameInProgress" v-model="field.len" maxlength="2"/>
        <input disabled v-else>
        <label>&emsp;width:&emsp;</label>
        <input v-if="!gameInProgress" v-model="field.width" maxlength="2">
        <input disabled v-else>
      </form>
    </div>
  </div>
<!--  {{ my_data}}-->
  <PlayGround @startGame="startGame"
              @endGame="endOfGame"
              v-bind:groundLen="field.len"
              v-bind:groundHigh="field.width"
              v-bind:aliveAfterEpoch="my_data"/>
</template>

<script>
import PlayGround from "@/components/Playground.vue";
export default {
  data() {
    return {
      my_data: [],
      connection: null,
      field: {
        len: 60,
        width: 30,
      },
      gameInProgress: false
    }
  },
  methods: {
    startGame: function(data, speed, gameInProgress) {
      this.gameInProgress = gameInProgress
      let outer_this = this
      if (!outer_this.connection) {
        outer_this.connection = new WebSocket('ws://localhost:8000/ws')
        outer_this.connection.onmessage = function (event) {
          outer_this.my_data = JSON.parse(event.data).slice(1, -1).split(', ')
        }
        outer_this.connection.onopen = function (event) {
          console.log(event)
          outer_this.sendData(data, speed)
        }
      }
      else {
        outer_this.sendData(data, speed)
      }
    },
    sendData: function(data, speed) {
      let msg = {
        shape: this.field,
        alive_mols: Object.keys(data),
        interrupt: false,
        speed: speed,
      }
      this.connection.send(JSON.stringify(msg))
    },
    endOfGame: function(gameInProgress) {
      this.gameInProgress = gameInProgress
      let msg = {
        shape: this.field,
        alive_mols: [],
        interrupt: true,
        speed: 1
      }
      this.connection.send(JSON.stringify(msg))
      this.connection.close(1000, 'Game over')
      this.connection = null
    },
  },
  components: {
    PlayGround
  },
  name: 'App',
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
input {
  width: 50px;
}
button {
  -webkit-writing-mode: horizontal-tb !important;
  -webkit-appearance: button;
  border-color: rgb(216, 216, 216) rgb(209, 209, 209) rgb(186, 186, 186);
  border-style: solid;
  border-width: 1px;
  padding: 1px 5px 0.5px;
  text-rendering: auto;
  color: #2c3e50;
  display: inline-block;
  text-align: start;
  margin: 0em;
}
button:hover {
  background: #1d49aa;
}

button:focus {
  outline: none;
  box-shadow: 0 0 0 4px #cbd6ee;
}
.container {
  margin: 10px;
}
form {
  margin: 5px;
}
</style>
