<template>
  <div>
    <form @submit.prevent>
      <label>random seed:&emsp;</label>
      <input v-model="randomSeed"
             @submit="setRandomSeed"
             placeholder="number"/>
      <button class="game-btn" @click="setRandomSeed">submit</button>
    </form>
    <button v-if="!gameInProgress"
        class="game-btn"
        @click="startGame"><span>start</span></button>
    <button disabled v-else>start</button>

    <button v-if="!gameInProgress"
        class="game-btn"
        @click="clearAllMolecules">refresh</button>
    <button disabled v-else>refresh</button>

    <button v-if="gameInProgress" class="game-btn"
        @click="stopGame">stop</button>
    <button disabled v-else>stop</button>
    <span>&emsp;</span>

    <button v-if="this.speed > 0" @click="speedUp"><span>+</span></button>
    <button disabled v-else>+</button>
    <span>&ensp;speed&ensp;</span>
    <button v-if="this.speed < 2" @click="speedDown">-</button>
    <button disabled v-else>-</button>
    <p></p>
    <hr>
  </div>
  <div class="playground canvas-for-weak">
    <th v-for="(row, row_idx) in playground" :key="row.id">
      <tr v-for="(mol, col_idx) in row" :key="mol.id">
        <button class="molecule"
            :class="{'clicked': mol.is_clicked}"
            @click="pickMolecule(row_idx, col_idx)"
            @mouseover.shift="pickMolecule(row_idx, col_idx)">&ensp;</button>
      </tr>
    </th>
  </div>
</template>

<script>
export default {
  mounted() {
    this.buildEmptyPlayground(this.groundLen, this.groundHigh)
  },
  data() {
    return {
      playground: [],
      molecule: {},
      pickedMolecules: {},
      randomSeed: null,
      speed: 1,
      gameInProgress: false
    }
  },
  methods: {
    refreshGround(aliveAfterEpoch) {
      this.clearPickedMolecules()
      if (aliveAfterEpoch.length === 1) {
        this.$emit('endGame')
        return
      }
      for (let alive_molecule of aliveAfterEpoch) {
        let key = alive_molecule.slice(1, -1)
        this.molecule[key].is_clicked = true
        this.pickedMolecules[key] = true
      }
    },
    buildEmptyPlayground(groundLen, groundWidth) {
      this.playground = []
      for (let i = 0; i < groundLen; i++) {
        let row = []
        for (let j = 0; j < groundWidth; j++) {
          row.push(
            this.molecule[String(j)+ '-' +String(i)] = {
            is_clicked: false,
            }
          )
        }
        this.playground.push(row)
      }
    },
    pickMolecule (i, j) {
      let key = String(j)+'-'+String(i)
      this.molecule[key].is_clicked = !this.molecule[key].is_clicked

      if (!(key in this.pickedMolecules)) {
        this.pickedMolecules[key] = true
        }
      else {
        delete this.pickedMolecules[key]
      }
    },
    clearPickedMolecules () {
      for ( let key in this.pickedMolecules) {
        this.molecule[key].is_clicked = false
      }
      this.pickedMolecules = {}
    },
    clearAllMolecules () {
      for (let i = 0; i < this.groundLen; i++) {
        for (let j = 0; j < this.groundHigh; j++) {
          this.molecule[String(j) + '-' + String(i)].is_clicked = false
        }
      this.pickedMolecules = {}
      this.speed = 1
      }
    },
    setRandomSeed () {
      if (!(/^(0|-?[1-9]\d{0,5})$/.test(this.randomSeed))) {
        alert('Random seed must be positive integer')
        this.randomSeed = null
      }
      this.clearPickedMolecules()
      for (let i = 0; i < this.randomSeed; i++) {
        let col = Math.floor(Math.random() * this.groundLen)
        let row = Math.floor(Math.random() * this.groundHigh)
        let key = String(row)+'-'+String(col)
        this.molecule[key].is_clicked = true
        this.pickedMolecules[key] = true
      }
      this.randomSeed = null
    },
    speedUp () {
      this.speed -= 0.2
      this.gameInProgress = true
      this.$emit('startGame', this.pickedMolecules, this.speed, this.gameInProgress)

    },
    speedDown () {
      this.speed += 0.2
      this.gameInProgress = true
      this.$emit('startGame', this.pickedMolecules, this.speed, this.gameInProgress)

    },
    startGame () {
      if (!(Object.keys(this.pickedMolecules).length === 0)) {
        this.gameInProgress = !this.gameInProgress
        this.$emit('startGame', this.pickedMolecules, this.speed, this.gameInProgress)
      }
    },
    stopGame() {
      this.gameInProgress = !this.gameInProgress
      this.$emit('endGame', this.gameInProgress)
    },


  },
  name: "PlayGround",
  props: ['groundLen', 'groundHigh', 'aliveAfterEpoch'],
  emits: ['startGame', 'endGame'],
  watch: {
    groundLen: function (newVal) {
      this.buildEmptyPlayground(newVal, this.groundHigh)
    },
    groundHigh: function (newVal) {
      this.buildEmptyPlayground(this.groundLen, newVal)
    },
    aliveAfterEpoch: function (newval) {
      this.refreshGround(newval)
    },
  },
}
</script>

<style scoped>
.clicked {
  background-color: brown;
}
.playground {
  margin:0 0 0 20px;
  width:50%;
}
input {
  width:50px;
}
.game-btn {
  font: 400 16px Avenir, Helvetica, Arial, sans-serif;
  margin: 2px;
}
button:disabled,
button[disabled]{
  border: 1px solid #999999;
  background-color: #cccccc;
  color: #666666;
}
</style>