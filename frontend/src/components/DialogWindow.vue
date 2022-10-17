<template>
  <div class="dialog" v-if="show" >
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>
    <img @click.stop="hideDialog" src="@/assets/krest.png" style="width: 40px; height: 40px; padding: 10px">

  </div>

</template>

<script>

export default {
  components: {

  },
  props:{
    show:{
      type: Boolean,
      default: false
    }
  },
  // test
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
  background: #403D39;
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
  padding: 50px;
}

</style>