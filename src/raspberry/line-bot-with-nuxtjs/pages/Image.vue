<template>
  <div>
    <div>
      <v-img width=100%
        :src="'data:image/png;base64,'+imgBase64"
      >
      </v-img>
      <!-- {{ $route.query.imagePath }} -->
      <!-- {{ imgBase64 }} -->
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'
export default {
  data () {
    return {
      // path: $route.query.imagePath,
    }
  },
  computed: {
    ...mapState('image', ['imgBase64'])
  },
  mounted() {

  },
  methods: {
  },
}
</script>