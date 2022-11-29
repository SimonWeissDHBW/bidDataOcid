import { createApp } from 'vue'
import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import axios from 'axios'
import VueAxios from 'vue-axios'

createApp(App).use(Quasar, quasarUserOptions, axios, VueAxios).mount('#app')
