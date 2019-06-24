<template>
  <div class="container">
    <h1>HIVE</h1>
    <p v-if="isConnected">Connected</p>
    <p v-else>Disconnected</p>

    <!-- <button v-on:click="fetchMessage" class="btn">Fetch message</button> -->
    <inputField/>
    <div class="postContainer">
      <post/>
    </div>
  </div>
</template>

<script>
// import Vue from "vue";
import Post from "./Post.vue";
import InputField from "./InputField.vue";

export default {
  data() {
    return {
      isConnected: false
    };
  },
  sockets: {
    connect() {
      this.isConnected = true;
    },
    disconnect() {
      this.isConnected = false;
    }
  },
  components: { Post, InputField },
  methods: {}
};
</script>

<style scoped>
</style>
