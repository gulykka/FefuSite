<template>
  <div class="forma">
    <h2>Добавление поста</h2>
    <input placeholder="Текст публикации">
    <p>Категоря услуги</p>
    <select v-model.number="ChosenCategory" class="filter_item">
      <option v-for="cat in category" v-bind:key="cat.title" v-bind:value="cat.id"> {{ cat.title }}</option>
    </select>
    <p>Корпус</p>
    <select v-model.number="ChosenBuilding" class="filter_item">

      <option v-for="bul in buildings" v-bind:key="bul.title" v-bind:value="bul.id"> {{ bul.title }}</option>
    </select>
    <select>
      <option>Мастер</option>
      <option>Клиент</option>
    </select>
    <second-button style="width: 200px; padding: 10px; color: #403D39; margin-left: 60px">Добавить пост</second-button>
  </div>

</template>

<script>
import SecondButton from "@/components/SecondButton";
export default {
  name: "PostForm",
  components:{
    SecondButton
  },
  data() {
    return {
      ChosenCategory: 0,
      ChosenBuilding: 0
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