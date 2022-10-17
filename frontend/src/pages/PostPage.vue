<template>
  <nav-bar
      v-bind:category="category"
      v-bind:buildings="buildings"
  ></nav-bar>
  <div class="forma">
    <h2>Добавление поста</h2>
    <form @submit.prevent="submitForm">
      <input v-model="poster.content" placeholder="Текст публикации">
      <p>Категория услуги</p>
      <select v-model="poster.categoryi" class="filter_item">
        <option v-for="cat in category" v-bind:key="cat.id" v-bind:value="cat.id"> {{ cat.title }}</option>
      </select>
      <p>Корпус</p>
      <select v-model="poster.building" class="filter_item">
        <option v-for="bul in buildings" v-bind:key="bul.id" v-bind:value="bul.id"> {{ bul.title }}</option>
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
  <div class="content">
    <div class="filter">
      <div>
        <second-button class="filter_item" style="margin: 10px; width: 150px" @click="ShowCategory()"> Фильтрация
        </second-button>
        <second-button class="filter_item" style="margin: 5px; width: 150px" @click="ShowAll()">Все услуги
        </second-button>
      </div>
      <input v-if="ThisFind"
             v-model="search"
             placeholder="Поиск">
      <div v-if="ThisCategory">
        <p>Категоря услуги</p>
        <select v-model.number="ChosenCategory" class="filter_item">
          <option v-for="cat in category" v-bind:key="cat.title" v-bind:value="cat.id"> {{ cat.title }}</option>
        </select>
        <p>Корпус</p>
        <select v-model.number="ChosenBuilding" class="filter_item">
          <option v-for="bul in buildings" v-bind:key="bul.title" v-bind:value="bul.id"> {{ bul.title }}</option>
        </select>
        <second-button @click="NoFilter" class="nofilter"> Сбросить фильтрацию</second-button>
      </div>

    </div>


    <div v-if="ThisAll">
      <div v-if="search === ''" class="sersis">
        <div v-for="ser in services" v-bind:key="ser.id">
          <div class="serves">
            <h3 class="servise_content">{{ ser.content }}</h3>
            <div v-if="ser.photo === null">
              <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
            </div>
            <div v-else>
              <img :src="ser.photo">
            </div>
            <strong>{{ ser.character }}</strong>
            <div v-for="bul in buildings" :key="bul.id">
              <div v-if="bul.id === ser.building">
                Корпус: {{ bul.title }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="sersis">

        <div v-for="ser in sortedAndSearchedPosts" v-bind:key="ser.id">

          <div class="serves">
            <h3 class="servise_content">{{ ser.content }}</h3>
            <div v-if="ser.photo === null">
              <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
            </div>
            <div v-else>
              <img :src="ser.photo">
            </div>
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

    <div v-else-if="ChosenCategory === 0">
      <div v-if="ChosenBuilding === 0" class="sersis">
        <template v-for="ser in services" v-bind:key="ser.id">
          <div class="serves">
            <h3 class="servise_content">{{ ser.content }}</h3>
            <div v-if="ser.photo === null">
              <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
            </div>
            <div v-else>
              <img :src="ser.photo">
            </div>
            <strong>{{ ser.character }}</strong>
            <div v-for="bul in buildings" :key="bul.id">
              <div v-if="bul.id === ser.building">
                Корпус: {{ bul.title }}

              </div>
            </div>
          </div>
        </template>
      </div>
      <div v-else-if="ChosenBuilding !== 0" class="sersis">
        <div v-for="ser in services" :key="ser.id">
          <template v-if="ser.building === ChosenBuilding">
            <div class="serves">
              <h3 class="servise_content">{{ ser.content }}</h3>
              <div v-if="ser.photo === null">
                <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
              </div>
              <div v-else>
                <img :src="ser.photo">
              </div>
              <strong>{{ ser.character }}</strong>
              <div v-for="bul in buildings" :key="bul.id">
                <div v-if="bul.id === ser.building">
                  Корпус: {{ bul.title }}
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </div>

    <div v-else>
      <div v-if="ChosenBuilding === 0" class="sersis">
        <div v-for="ser in services" :key="ser.id">
          <div v-if="ser.category === ChosenCategory">
            <div class="serves">
              <h3 class="servise_content">{{ ser.content }}</h3>
              <div v-if="ser.photo === null">
                <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
              </div>
              <div v-else>
                <img :src="ser.photo">
              </div>
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
      <div v-else>
        <template v-for="ser in services" :key="ser.id">
          <div v-if="ser.building === ChosenBuilding">
            <div v-if="ser.category === ChosenCategory" class="sersis">
              <div class="serves">
                <h3 class="servise_content">{{ ser.content }}</h3>
                <div v-if="ser.photo === null">
                  <img style="width: 190px; margin: 10px;margin-left: 50px" src="@/assets/serves.png">
                </div>
                <div v-else>
                  <img :src="ser.photo">
                </div>
                <strong>{{ ser.character }}</strong>
                <div v-for="bul in buildings" :key="bul.id">
                  <div v-if="bul.id === ser.building">
                    Корпус: {{ bul.title }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
  <footer>
    <img style="width: 15px; padding: 0; margin: 0" src="@/assets/f-icon.png"> 2022
  </footer>
</template>

<script>
import axios from 'axios';
import API from "@/mixins/API";
import NavBar from "@/components/NavBar";
import SecondButton from "@/components/SecondButton";


export default {
  name: "PostPage",
  components: {
    NavBar,
    SecondButton
  },
  mixins: [API],
  data() {
    return {
      services: [],
      profiles: [],
      category: [],
      buildings: [],
      ChosenCategory: 0,
      ChosenBuilding: 0,
      ThisAll: true,
      ThisCategory: false,
      ThisBuilding: false,
      ThisFind: true,
      search: '',
      poster: {
        content: '',
        categoryi: '',
        building: '',
        character: '',


      },
      posts: []

    }
  },
  mounted() {
    this.getServices()
    this.getProfiles()
    this.getCategory()
    this.getBuildings()

  },
  methods: {
    NoFilter() {
      this.ChosenCategory = 0
      this.ChosenBuilding = 0
    },
    ShowAll() {
      this.ThisAll = true
      this.ThisFind = true
      this.ThisCategory = false
      this.ChosenCategory = 0
      this.ChosenBuilding = 0
    },
    ShowCategory() {
      this.search = ''
      this.ThisAll = false
      this.ThisCategory = true
      this.ThisFind = false
    },
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
    getProfiles() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/profiles/',
        auth: {
          username: '0000',
          password: '0000'
        }
      }).then(responce => this.profiles = responce.data)
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
            this.$router.push({name: 'myprifile', params: {slug: response.data.slug}})
          })
          .catch(error => {
            console.log(error)
          })
    }

  },
  computed: {
    sortedAndSearchedPosts() {
      return this.services.filter(post => post.content.toLowerCase().includes(this.search.toLowerCase()))
    }
  }


}
</script>

<style scoped>

footer {
  background-color: #FFFCF2;
  padding: 30px;
  margin-top: 150px;
  padding-left: 50%;
}

input {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  height: 30px;
  width: 300px;
}

select {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  height: 40px;
  width: 310px;
}

.content {
  display: flex;
  flex-direction: row;
}

.filter {
  max-width: 350px;
  flex-grow: 1;
  padding: 30px;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

.services {
  flex-grow: 3;
  padding: 30px;

}

.serves {
  padding: 10px;
  border-radius: 20px;
  border: 4px solid #403D39;
  width: 300px;
  height: 300px;
  margin: 10px;
  display: flex;
  flex-direction: column;
}

.sersis {
  margin-top: 50px;
  width: 1050px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
}

p {
  margin-left: 12px;
}

.nofilter {
  margin-left: 12px;
}

img {
  margin: 10px;
  margin-left: 50px;
  width: 200px;
}
.servise_content {
  height: 45px;
  text-align: center;
}
</style>