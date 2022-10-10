<template>
<button>
  <slot></slot>
</button>
</template>

<script>
export default {
  name: "SecondButton"
}
</script>

<style scoped>
button {
  border-color: #403D39;
  border-style: solid;
  border-radius: 10px;
  font-size: 17px;
  padding: 4px;
  transition: all 1s;
}
button:hover {
  color: #EB5E28;
  border-color: #EB5E28;
}
</style>