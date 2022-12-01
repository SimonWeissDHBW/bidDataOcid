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
        >
        <template v-slot:label="options">
        <div class="row items-center">
          <span>{{ options.label }}</span>
          <q-spinner-comment
            color="orange"
            size="3em"
            :thickness="2"
            v-if="options.loading" 
            style="padding: 5px;"
          />
        </div>
      </template>
      </q-option-group>
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
      lon: 0.0,
      lat: 0.0,
      group: ref(['UMTS']),
      options: [
        {label : 'UMTS', value: 'UMTS', loading: false},
        {label : 'LTE', value: 'LTE', loading: false},
        {label : 'GSM', value: 'GSM', loading: false},
        {label : 'CDMA', value: 'CDMA', loading: false},
      ],
    }
  },

  methods: {
    async getAPI() {
      this.rows = [];
      for (let i in this.group){
        
        this.options.find(x => x.value === this.group[i]).loading = true;
        fetch("http://"+ self.location.host + "/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
        .then(response => response.json())
          .then(data =>  {

            this.options.find(x => x.value === this.group[i]).loading = false;
            if (data.data.length != 0){
              console.log("Data found.");
              console.log(data.data);
              console.log(this.rows)
              this.rows = this.rows.concat(data.data);
              console.log(this.rows);
              // return data.data
            }
            else{
              console.log("No data found");
              console.log(data.data);
              console.log(this.rows)
              this.rows = this.rows.concat([{radio: this.options[i].value, distance: NaN}]);
              console.log(this.rows);
              // return [{radio: this.options[i].value, distance: NaN}]
            }
        
          }
        );
      }
    }
  },

  setup () {
    const backGroundFunc =  ((row) =>  {return "bg-" + (isNaN(row.distance) ? "grey" : (row.distance < 500 ? "green" : (row.distance < 1000 ? "orange" : "red")))})
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