<template>
  <div class="flex-contanier navbar">
    <div class="flex-item element1">
      Fefu Service
    </div>
    <div class="second-contanier flex-item ">
      <first-button
          class="element2"
          @click="$router.push('/myprofile')">
        Мой Профиль
      </first-button>

      <first-button
          class="element2"
          @click="$router.push('/posts')"
      >
        Услуги
      </first-button>
      <first-button
          class="element2"
          @click="showDialog"
      >
        Добавить пост
      </first-button>
      <dialog-window
          v-model:show="dialogVisible"
      >
        <post-form
            v-bind:category="category"
            v-bind:buildings="buildings"
        ></post-form>

      </dialog-window>
    </div>
  </div>
</template>

<script>
import FirstButton from "@/components/FirstButton";
import DialogWindow from "@/components/DialogWindow";
import PostForm from "@/components/PostForm";
export default {
  name: "NavBar",
  components: {
    FirstButton,
    DialogWindow,
    PostForm,

  },
  props: {
    category: {
      type: Array,
      required: true
    },
    buildings:{
      type: Array,
      required: true
    }
  },
  data() {
    return {
      dialogVisible: false
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    }
  }
}
</script>

<style scoped>
.flex-contanier {
  display: flex;
  justify-content: space-around;
  padding: 30px;
}

.element1 {
  font-size: 40px;
  color: #403D39;

}

.element2 {
  font-size: 22px;
  color: #CCC5B9;
}
.second-contanier {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}
a {
  text-decoration: none;
}
.navbar {
  background: #FFFCF2;
}

</style>