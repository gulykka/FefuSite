<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios'
import API from "@/mixins/API";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
      isAuthenticated: false,
      profile: {}
    }
  },
  mixins: [API],
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    if (this.$store.state.isAuthenticated) {
      this.getProfile()
      this.isAuthenticated = this.$store.state.isAuthenticated
    }
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.length
    }
  },
  watch: {
    '$store.state.isAuthenticated'(to) {
      if (to === false) {
        this.isAuthenticated = false
        this.profile = {}
      } else {
        this.getProfile()
        this.isAuthenticated = this.$store.state.isAuthenticated
      }
    },
    '$store.state.cart.items'() {
      this.cart = this.$store.state.cart
    }
  }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
  font-family: "Century Gothic";
}
#app {
  background: #CCC5B9;
}
</style>