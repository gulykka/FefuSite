<template>
  <div class="forma">
    <h2 style="">Добавление поста</h2>
    <form @submit.prevent="submitForm" class="forma">
      <input v-model="poster.content" placeholder="Текст публикации">
      <p>Категоря услуги</p>
      <select v-model="poster.categoryi" class="filter_item">
        <option v-for="cat in category" v-bind:key="cat.id" v-bind:value="cat.id"> {{ cat.title }}</option>
      </select>
      <p>Корпус</p>
      <select v-model="poster.building" class="filter_item">
        <option v-for="bul in buildings" v-bind:key="bul.id" v-bind:value="bul.id"> {{ bul.title }}</option>
      </select>
      <p>Мастер/Клиент</p>
      <select v-model="poster.character">
        <option>Мастер</option>
        <option>Клиент</option>
      </select><br>
      <second-button style="width: 200px; padding: 10px; color: #403D39; margin-left: 60px"
      >Добавить пост
      </second-button>
    </form>
  </div>

</template>

<script>
import SecondButton from "@/components/SecondButton";
import axios from "axios";
import router from "@/router/router";

export default {
  name: "PostForm",
  components: {
    SecondButton
  },
  data() {
    return {
      poster: {
        content: '',
        categoryi: '',
        building: '',
        character: ''

      },
      posts: []
    }
  },
  props: {
    category: {
      type: Array,
      required: true
    },
    buildings: {
      type: Array,
      required: true
    }
  },
  methods: {
    async submitForm() {
      const formData = new FormData()
      formData.append('author', this.$root.profile.id)
      formData.append('building', this.poster.building)
      formData.append('category', this.poster.categoryi)
      formData.append('character', this.poster.character)
      formData.append('content', this.poster.content)

      await axios
          .post('api/publications/', formData)
          .then(response => {
            this.$router.push({name: 'Posts', params: {slug: response.data.slug}})
          })
          .catch(error => {
            console.log(error)
          })
      this.poster.building = ''
      this.poster.categoryi = ''
      this.poster.character = ''
      this.poster.content = ''
      router.push('/myprofile')
    }
  }
}
</script>

<style scoped>
* {
  color: #CCC5B9;
}

input {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  color: #403D39;
  height: 30px;
  width: 300px;
}

option {
  color: #403D39;
}

select {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  color: #403D39;
  height: 40px;
  width: 310px;
}

h2 {
  text-align: center;
  margin-bottom: 10px;
}

.forma {
  margin: 20px;
  display: flex;
  flex-direction: column;

}

p {
  margin-left: 12px;
}
</style>