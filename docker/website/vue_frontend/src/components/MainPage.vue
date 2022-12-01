<template>
  <div style="display:flex; flex-direction: column; align-items: center;">
      <div class="q-pa-md" style="width: 75%">
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
      <form 
        style="display:flex; flex-direction: column; align-items: center; width: 100%;"
        @submit.prevent.stop="getAPI" class="q-gutter-md"
      >
        <q-input 
          ref="lonRef"
          color="orange" 
          standout 
          bottom-slots 
          v-model="lon" 
          label="Longitude"
          :rules="[val => (val > -180 && val < 180) || 'Longitude must be between -180 and 180']"
        >
          <template v-slot:prepend>
            <q-icon name="place" />
          </template>
        </q-input>
        <q-input 
          ref="latRef"
          color="orange" 
          standout 
          bottom-slots 
          v-model="lat" 
          label="Latitude"
          :rules="[val => (val > -90 && val < 90) || 'Latitude must be between -90 and 90']"
        >
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
        <q-btn type="submit" color="primary" label="Get Cell Data"/>
      </form>
    </div>
  </div>
</template>

<style>
</style>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const backGroundFunc =  ((row) =>  {return "bg-" + (isNaN(row.distance) ? "grey" : (row.distance < 250 ? "green" : (row.distance < 500 ? "orange" : "red")))})
    const columns = [
      { name: 'radio', label: 'Radio Type', field: 'radio', sortable: true, classes: backGroundFunc},
      { name: 'distance', label: 'Distance (in meters)', field: 'distance', sortable: true, classes: backGroundFunc},
    ]
    return {
      columns,
    }
  },
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

      //Check if the user has entered valid coordinates
      if (!( this.lon <= -180 || this.lon >= 180 || this.lat <= -90 || this.lat >= 90)) {

        this.rows = [];
        for (let i in this.group){
          
          this.options.find(x => x.value === this.group[i]).loading = true;
          fetch("http://"+ self.location.host + "/cellTowers/" + this.group[i] + "/" + this.lon + "/" + this.lat)
          .then(response => response.json())
            .then(data =>  {

              this.options.find(x => x.value === this.group[i]).loading = false;
              let tempDistance = (data.data[0][0].distance != null) ? Math.round(data.data[0][0].distance) : "N/A";
              this.rows = this.rows.concat([{radio: this.group[i], distance: tempDistance}]);

            }
          );
        }

      }
    }
  }
}
</script>