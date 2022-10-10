<template>
  vgbhnjmk,l
  <template v-for="ser in services" v-bind:key="ser.id">
    <div v-if="ser.category === ChosenCategory">
      <div class="serves">
        <h3>{{ ser.content }}</h3>
      </div>
    </div>
  </template>
</template>

<script>
export default {
  name: "FilterList"
}
</script>

<style scoped>

</style>