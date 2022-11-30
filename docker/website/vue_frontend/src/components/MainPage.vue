<template>
  <div style="display:flex; flex-direction: column; align-items: center;">
      <div class="q-pa-md" style="width: 75%">
        <!-- Table which changes its colum color depending on Distance value -->
      <q-table
        title="Cell Tower Signal Data"
        :rows="rows"
        :columns="columns"
        row-key="name"
        dark
        color="amber"
      >
      </q-table>
    </div>
      
    <div style="display:flex; flex-direction: column; align-items: center; width: 40%;">
      <q-input color="orange" standout bottom-slots v-model="lon" label="Longitude">
        <template v-slot:prepend>
          <q-icon name="place" />
        </template>
      </q-input>

      <q-input color="orange" standout bottom-slots v-model="lat" label="Latitude">
        <template v-slot:prepend>
          <q-icon name="place" />
        </template>
      </q-input>

      <div class="q-pa-lg" style="display:flex; flex-direction: column; align-items: center;">
        <q-option-group
          v-model="group"
          :options="options"
          color="orange"
          center-label
          type="toggle"
        />
      </div>

      <q-btn color="primary" label="Get Cell Data" @click="getAPI()" />

    </div>
 
  </div>
</template>

<style>
</style>

<script>
import { ref } from 'vue'

export default {
  name: 'MainPage',
  data() {
    return {
      rows: [],
      test: 0,
      lon: 0.0,
      lat: 0.0,
      group: ref(['UMTS']),
      options: [
        {label : 'UMTS', value: 'UMTS'},
        {label : 'LTE', value: 'LTE'},
        {label : 'GSM', value: 'GSM'},
        {label : 'CDMA', value: 'CDMA'},
      ],
    }
  },

  methods: {
    async getAPI() {
      for (let i in this.group){
        this.rows = this.rows.concat(await fetch("http://"+ self.location.host + "/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
        .then(response => response.json())
        .then(data =>  {
          return data.data
        }));
      }
    }
  },

  setup () {
    const backGroundFunc =  ((row) =>  {return "bg-" + (row.distance < 500 ? "green" : (row.distance < 1000 ? "orange" : "red"))})
    const columns = [
      { name: 'radio', label: 'Radio Type', field: 'radio', sortable: true, classes: backGroundFunc},
      { name: 'distance', label: 'Distance', field: 'distance', sortable: true, classes: backGroundFunc},
    ]
    return {
      columns,
    }
  }
}

</script>