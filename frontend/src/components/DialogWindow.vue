<template>
  <div class="dialog" v-if="show" >
    <div @click.stop class="dialog__content">
      <slot></slot>
    </div>
    <second-button @click.stop="hideDialog" style="height: 30px; width: 30px; margin: 20px; padding: 0">x</second-button>
  </div>

</template>

<script>
import SecondButton from "@/components/SecondButton";
export default {
  components: {
    SecondButton
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