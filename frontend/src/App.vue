<template>
  <v-app>
    <title>DP</title>
    <v-main>
      <FileUpload/>
    </v-main>
  </v-app>
</template>

<script>
import FileUpload from './components/FileUpload.vue'

export default {
  name: 'App',

  components: {
    FileUpload,
  },

  data: () => ({
    //
  }),
}
</script>
