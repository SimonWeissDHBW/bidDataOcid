<template>
  <div style="display:flex; flex-direction: column;">
      <div class="q-pa-md">
      <q-table
        title="Treats"
        :rows="rows"
        :columns="columns"
        row-key="name"
        dark
        color="amber"
      />
    </div>

      
    <div width="25%" style="width: 50%;">
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

      <div class="q-pa-lg">
        <q-option-group
          v-model="group"
          :options="options"
          color="red"
          left-label
          type="checkbox"
        />
      </div>

      <q-btn color="primary" label="Calculate" @click="getAPI()" />

    </div>
 
  </div>
</template>

<style>
</style>

<script>
import { ref } from 'vue'


export default {
  name: 'HelloWorld',
  data() {
    return {
      rows: [],
      lon: 0.0,
      lat: 0.0,
      group: ref(['UMTS']),
      options: [
        {label : 'UMTS', value: 'UMTS'},
        {label : 'LTE', value: 'LTE'},
        {label : 'GSM', value: 'GSM'},
        {label : 'CDMA', value: 'CDMA'},
      ]
    }
  },
  methods: {
    async getAPI() {
      this.rows = [];
      for (let i in this.group){
        console.log(this.group[i])
        // console.log("http://localhost:3000/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
        this.rows = this.rows.concat(await fetch("http://localhost:3000/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
        // this.rows = await fetch("http://localhost:3000/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
        .then(response => response.json())
        .then(data =>  {
          console.log(data.data)
          return data.data
        }));
      }
    }
  },
setup () {
  const columns = [
    { name: 'radio', label: 'Radio Type', field: 'radio', sortable: true },
    { name: 'mcc', label: 'MCC (Mobile Country Code)', field: 'mcc', sortable: true },
    { name: 'net', label: 'Net', field: 'net' },
    { name: 'area', label: 'Area', field: 'area' },
    { name: 'cell', label: 'Cell', field: 'cell' },
    { name: 'unit', label: 'Unit', field: 'unit' },
    { name: 'lon', label: 'Longitude', field: 'lon' },
    { name: 'lat', label: 'Latitude', field: 'lat' },
    { name: 'range', label: 'Range', field: 'range' },
    { name: 'samples', label: 'Samples', field: 'samples', sortable: true},
    { name: 'changeable', label: 'Changeable', field: 'changeable'},
    { name: 'created', label: 'Created', field: 'created'},
    { name: 'updated', label: 'Updated', field: 'updated'},
    { name: 'averageSignal', label: 'Average Signal', field: 'averageSignal'},
  ]



  return {
    columns,

  }
  }
}

</script>