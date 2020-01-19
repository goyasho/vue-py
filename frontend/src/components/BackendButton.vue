<template>
  <div>
    <input type="text" v-model="msg">
    <button @click="backend">backend</button>
    <p>{{ response }}</p>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  name: "BackendButton",
  data () {
    return {
      msg: "",
      response: "none"
    };
  },
  methods: {
    backend() {
      const path = `http://localhost:5000/api/${this.msg}`
      axios.get(path)
        .then(response => {
          console.log(response)
          this.response = response.data;
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
};
</script>

<style scoped>

</style>
