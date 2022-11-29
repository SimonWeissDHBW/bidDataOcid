<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="glossy">
      <q-toolbar>
        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>
        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <MainPage />
    </q-page-container>
  </q-layout>
</template>

<script>
import MainPage from './components/MainPage.vue'

export default {
  name: 'LayoutDefault',

  components: {
    MainPage
  },
}
</script>
