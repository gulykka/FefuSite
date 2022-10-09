<template>
  <div class="dialog" v-if="show" @click.stop="hideDialog">
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>

  </div>
</template>

<script>

export default {

  props:{
    show:{
      type: Boolean,
      default: false
    }
  },
  methods:{
    hideDialog(){
      this.$emit('update:show', false)
    }
  }
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0,0,0,0.7);
  position: fixed;
  display: flex;
}
.dialog__content{
  margin: auto;
  border: 6px solid #FFFCF2;
  background: rgba(204, 197,185, 0.7);
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
  padding: 50px;
}

</style>