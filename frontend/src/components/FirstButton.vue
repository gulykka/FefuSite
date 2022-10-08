<template>
  <a>
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "FirstButton"
}
</script>

<style scoped>
a{
  padding: 10px;

  color: #CCC5B9;

  transition: all 1s ;
}
a:hover{
  opacity: 0.7;
  color: #EB5E28;

}
</style>