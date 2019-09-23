<template>
  <div class="container">
    <p>{{ msg }}</p>
    <p>{{ date_created }}</p>
    <div class="button-container">
      <div class="like-container">
        <p class="likes">Likes: {{ likes }}</p>
        <button v-on:click="addLike" type="button">Like</button>
      </div>
      <div class="report-container">
        <p class="likes">Reports: {{ reports }}</p>
        <button v-on:click="addReport" type="button">Report</button>
      </div>
    </div>
  </div>
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