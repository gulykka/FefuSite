<template>
  <nav-bar
      v-bind:category="category"
      v-bind:buildings="buildings"
  ></nav-bar>
  <div class="myprofile">
    <div class="info prof ">
      <h1>{{ this.$root.profile.name }}</h1>
      <div class="info_detail">
        Номер телефона: {{ this.$root.profile.phone_number }}<br>
        Корпус: {{ this.$root.profile.building }}
      </div>
      <br>
      <button style="font-size: 25px;">Выйти</button>
    </div>
    <div class="myservise prof">
      <h2>Мои услуги</h2>
      <div class="my__servises">
        <div v-for="ser in services" :key="ser.id">
          <div v-if="ser.author === this.$root.profile.id">
            <div class="serves">
              <div class="my__servises_content">
                {{ ser.content }}
              </div>
              <img v-if="ser.photo === null"
                   src="@/assets/serves.png">
              <img v-else :src="ser.photo">
              <strong>{{ ser.character }}</strong>
              <div v-for="bul in buildings" :key="bul.id">
                <div v-if="bul.id === ser.building">
                  Корпус: {{ bul.title }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="mymessenge prof">
      <h2>Заказ услуг</h2>
    </div>
  </div>
  <footer>
    <img style="width: 15px; padding: 0; margin: 0" src="@/assets/f-icon.png"> 2022
  </footer>
</template>

<script>
import NavBar from "@/components/NavBar";
import axios from "axios";

export default {
  name: "UserPage",
  components: {
    NavBar,

  },
  data() {
    return {
      services: [],
      buildings: [],
      category: []
    }
  },
  mounted() {
    this.getServices()
    this.getBuildings()
    this.getCategory()
  },
  methods: {
    getServices() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/publications/',
        auth: {
          username: '0000',
          password: '0000'
        }
      }).then(responce => this.services = responce.data)
    },
    getBuildings() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/buildings/',
        auth: {
          username: '0000',
          password: '0000'
        }
      }).then(responce => this.buildings = responce.data)
    },
    getCategory() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/categories/',
        auth: {
          username: '0000',
          password: '0000'
        }
      }).then(responce => this.category = responce.data)
    },
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
    }
  },

}
</script>

<style scoped>

.info {
  background: #CCC5B9;
  flex-grow: 1;
  height: 267px;
  padding: 30px;
  border-radius: 20px;
  border: 5px solid #403D39;
  margin: 10px;
}

.myprofile {
  display: flex;
  flex-direction: row;
}

.myservise {
  flex-grow: 2;
}

.my__servises {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 500px;
}

.mymessenge {
  flex-grow: 2;
}

.serves {
  padding: 10px;
  border-radius: 20px;
  border: 4px solid #403D39;
  width: 210px;
  height: 210px;
  margin: 5px;
}

img {
  padding: 0;
  margin-left: 40px;
  width: 130px;
}

.my__servises_content {
  text-align: center;
  height: 40px;
}

.info_detail {
  font-size: 20px;
}

footer {
  background-color: #FFFCF2;
  padding: 30px;
  margin-top: 150px;
  padding-left: 50%;
}

h2 {
  padding-left: 180px;
  padding-bottom: 35px;
}

button {
  background: none;
  border: 3px solid #403D39;
  color: #403D39;
  border-radius: 10px;
  transition: all 1s;
  padding: 2px;
}

button:hover {
  color: #EB5E28;
  box-shadow: 1px 1px 5px #EB5E28;
}

.prof {
  padding: 20px;
}
</style>