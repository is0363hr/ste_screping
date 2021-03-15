<template>
  <div>
    <Tabs></Tabs>
    <div class="text-center">
      <v-btn
        class="mx-2"
        fab
        dark
        small
        color="primary"
      >
        <v-icon dark>
          mdi-minus
        </v-icon>
      </v-btn>
      <v-btn
        class="mx-2"
        fab
        dark
        small
        color="indigo"
      >
        <v-icon dark>
          mdi-plus
        </v-icon>
      </v-btn>
    </div>
    <div>
      <v-slider
        v-model="time"
        :max="6"
        :tick-labels="labels"
        class="mx-4"
        ticks
      ></v-slider>
    </div>
  </div>
</template>

<script>
import Tabs from '~/components/Tabs.vue'

export default {
  components: {
    Tabs,
  }
}
</script>