<template>
  <nav-bar></nav-bar>
  <div class="info">
    <!--informatiom about profile-->
    <first-button style="font-size: 25px">Выйти</first-button>
  </div>
  <div class="servises">

  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import FirstButton from "@/components/FirstButton";
export default {
  name: "UserPage",
  components: {
    NavBar,
    FirstButton
  },
}
</script>

<style scoped>
.info{
  background: #FFFCF2;
}
</style>