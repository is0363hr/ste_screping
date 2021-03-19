<template>
  <v-row justify="center" align="center" width=100%>
    <HomeHeader></HomeHeader>
    <div class="home-body">
      <v-img width=100%
        src='zoom2/202102231025.png'
      >
      </v-img>
      <div class="img-bar">
        <HomeBody></HomeBody>
      </div>
    </div>
  </v-row>
</template>

<script>
import HomeHeader from '~/components/HomeHeader.vue'
import HomeBody from '~/components/HomeBody.vue'

export default {
  components: {
    HomeHeader,
    HomeBody,
  }
}
</script>

<style scoped>
.home-body {
  position: relative;
}
.img-bar {
  position: absolute;
  top: 15%;
  left: 3%;
}
</style>
