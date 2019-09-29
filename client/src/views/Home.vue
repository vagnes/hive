<template>
  <div class="ion-page">
    <ion-header>
      <ion-toolbar>
        <ion-title>Hive</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <Main />
    </ion-content>
  </div>
</template>

<script>
// @ is an alias to /src

import Main from "@/components/Main.vue";

export default {
  name: "home",
  components: {
    Main
  }
};
</script>
