<template>
  <v-row justify="center" align="center" width=100%>
    <HomeHeader></HomeHeader>
    <div class="home-body">
      <v-img width=100%
        :src="imgSrc()"
        alt="/static/4/20210401101500.png"
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
import { mapGetters } from 'vuex'

export default {
  components: {
    HomeHeader,
    HomeBody,
  },
  data() {
    return{
      weatherImgData: "/static/4/20210401101500.png"
    }
  },
  computed: {
    ...mapGetters('weather', ['imgPath']),
    getImgPath() {
      this.imgPath({
        imgPath: this.imgPath,
      })
      this.imgPath = null
    }
  },
  methods: {
    ...mapGetters('weather', ['imgData']),
    imgSrc(){
      this.imgData({
        weatherImgData: this.imgData,
      })
      this.weatherImgData = "/static/4/20210401101500.png"
    }
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
