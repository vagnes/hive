<template>
  <ion-card>
    <ion-card-subtitle>{{ date_created }}</ion-card-subtitle>
    <ion-card-content>
      <ion-text color="dark">{{ msg }}</ion-text>
      <ion-grid>
        <ion-row class="ion-float-right">
          <ion-button fill="clear" v-on:click="addLike">
            <ion-icon slot="icon-only" name="heart" size="small"></ion-icon>
            {{ likes }}
          </ion-button>
          <ion-button fill="clear" v-on:click="addReport">
            <ion-icon slot="icon-only" name="alert" size="small"></ion-icon>
            {{ reports }}
          </ion-button>
        </ion-row>
      </ion-grid>
    </ion-card-content>
  </ion-card>
</template>

<script>
export default {
  name: "Post",
  props: [],
  data() {
    return {
      id: "",
      msg: "",
      likes: "",
      reports: "",
      date_created: ""
    };
  },
  methods: {
    addLike: function() {
      this.$socket.emit("add_like", {
        id: this.id
      });
    },
    addReport: function() {
      this.$socket.emit("add_report", {
        id: this.id
      });
    },
    updateStats: function() {
      this.$socket.emit(
        "update_stats",
        {
          id: this.id
        },
        data => {
          this.likes = data.likes;
          this.reports = data.reports;
        }
      );
    }
  },
  mounted: function() {
    // this.sockets.subscribe("msg_to_client", data => {
    //   this.id = data.id;
    //   this.msg = data.message;
    //   this.likes = data.likes;
    //   this.reports = data.reports;
    //   this.date_created = data.date_created;
    // });
    this.$socket.emit("fetch_new_msg", data => {
      this.id = data.id;
      this.msg = data.message;
      this.likes = data.likes;
      this.reports = data.reports;
      this.date_created = data.date_created;
    });
  },
  created: function() {
    setInterval(() => {
      this.updateStats();
    }, 1000);
  }
};
</script>

<style scoped>
.container {
  margin-top: 50px;
  background-color: aqua;
  display: flex;
  justify-content: space-around;
  align-items: baseline;
}
.button-container {
  display: flex;
}
.like-container {
  display: flex;
  flex-direction: row;
  align-items: baseline;
  padding-right: 10px;
}

.like-container p {
  padding-right: 10px;
}
.report-container {
  display: flex;
  flex-direction: row;
  align-items: baseline;
  padding-right: 10px;
}

.report-container p {
  padding-right: 10px;
}
</style>