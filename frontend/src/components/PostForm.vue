<template>
  <div class="forma">
    <h2>Добавление поста</h2>
    <form @submit.prevent="createPost">
      <input v-model="poster.content" placeholder="Текст публикации">
      <p>Категоря услуги</p>
      <select v-model="poster.categoryi" class="filter_item">
        <option v-for="cat in category" v-bind:key="cat.id" v-bind:value="cat.title"> {{ cat.title }}</option>
      </select>
      <p>Корпус</p>
      <select v-model="poster.building" class="filter_item">

        <option v-for="bul in buildings" v-bind:key="bul.id" v-bind:value="bul.title"> {{ bul.title }}</option>
      </select>

      <select v-model="poster.character">
        <option>Мастер</option>
        <option>Клиент</option>
      </select>
      <second-button style="width: 200px; padding: 10px; color: #403D39; margin-left: 60px"


      >Добавить пост
      </second-button>
    </form>
  </div>

</template>

<script>
import SecondButton from "@/components/SecondButton";

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
    async createPost() {
      var responce = await fetch('http://127.0.0.1:8000/api/publications/', {
        method: 'post',
        headers: {
          'Content-Type': 'aplication/json'
        },
        body: JSON.stringify(this.poster)
      });
      this.posts.push(await responce.json());
      console.log(this.posts)
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
  margin-left: 50px;
  margin-bottom: 10px;
}

.forma {
  margin: 30px;
  display: flex;
  flex-direction: column;
}

p {
  margin-left: 12px;
}
</style>