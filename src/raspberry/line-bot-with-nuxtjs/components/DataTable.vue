<template>
  <div id="app">
    <v-app id="inspire">
      <div>
        <v-data-table
          :headers="headers"
          :items="items"
          item-key="id"
          class="elevation-1"
          :search="search"
          :custom-filter="filterOnlyCapsText"
        >
          <template v-slot:top>
            <v-text-field
              v-model="search"
              label="Search (UPPER CASE ONLY)"
              class="mx-4"
            ></v-text-field>
          </template>
          <!-- ウェブサイトの項目をリンクにします。 -->
          <template #item.name="{ item }">
            <!-- <nuxt-link :to="`Image?imagePath=${item.path}`" @click.native="updatePath(item.path)">{{ item.name }}</nuxt-link> -->
            <nuxt-link to="Image" @click.native="updatePath(item.path)">{{ item.name }}</nuxt-link>
          </template>
        </v-data-table>
      </div>
    </v-app>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex'
export default {
  data () {
    return {
      items: [],
      search: '',
      calories: '',
    }
  },
  computed: {
    headers () {
      return [
        {
          text: 'Id',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        {
          text: 'ImageName',
          value: 'name',
        },
        {
          text: 'CreatedAt',
          value: 'createdAt',
        },
        {
          text: 'ZoomLevel',
          value: 'zoomLevel',
        },
      ]
    },
  },
  methods: {
    ...mapMutations('image', ['updateImagePath']),
    ...mapActions('image', ['requestImg']),
    filterOnlyCapsText (value, search, item) {
      return value != null &&
        search != null &&
        typeof value === 'string' &&
        value.toString().toLocaleUpperCase().indexOf(search) !== -1
    },
    updatePath (path){
      this.updateImagePath(path)
      this.requestImg()
    },
  },
  mounted: function() {
    this.$axios
      .$get('/api/database')
      .then(response => {
        this.items = response
      })
      .catch(error => {
        console.log(error)
      })
  },
}
</script>