<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="q-pa-md q-gutter-y-sm bg-orange">
      <q-toolbar>
        <q-toolbar-title>
          Cell Tower Signal Tester
        </q-toolbar-title>
        <div style="height=20px; margin: 5px;">
          <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pinclipart.com%2Fpicdir%2Fbig%2F162-1626456_communication-tower-png-pic-cell-phone-tower-clip.png&f=1&nofb=1&ipt=a3f30131c5f719e98560ac9abc2ce6e5a276bd355fdca47f0dadbad6b45c3534&ipo=images"  height="60" alt="Cell Tower Clip Art"/>
        </div>
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
