<template>
  <ion-grid>
    <form @submit="sendMsg">
      <ion-col>
        <ion-item>
          <ion-label>Msg:</ion-label>
          <ion-input
            :value="msg"
            @input="msg = $event.target.value"
            name="msg"
            placeholder="Enter your message"
          ></ion-input>
        </ion-item>
      </ion-col>
      <ion-col>
        <ion-button type="submit" color="primary" expand="block">Send</ion-button>
      </ion-col>
    </form>
  </ion-grid>
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
    sendMsg(e) {
      e.preventDefault();
      this.$socket.emit("send_msg", { msg: this.msg });
      this.msg = "";
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
