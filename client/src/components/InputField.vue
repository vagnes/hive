<template>
  <div>
    <div class="form-group">
      <textarea v-model="msg" v-on:keyup.enter.ctrl.exact="sendMsg" class="form-control"></textarea>
    </div>
    <button v-on:click="sendMsg" class="btn">Send</button>
  </div>
</template>

<script>
export default {
  name: "InputField",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    sendMsg: function() {
      this.$socket.emit("send_message", { msg: this.msg });
    }
  }
};
</script>

<style scoped>
textarea {
  width: 40vw;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
