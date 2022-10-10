<template>
  <div class="general-contanier">
    <div class="flex-contanier navbar">
      <div class="flex-item element1">
        Fefu Service
      </div>
      <div class="second-contanier flex-item ">
        <first-button
            class="element2"
            @click="$router.push('/registration')">

          Регистрация
        </first-button>

        <first-button
            class="element2"
            @click="$router.push('/')"
        >
          Авторизация
        </first-button>
      </div>
    </div>
    <form @submit.prevent="submitForm">
    <div class="flex-contanier flex-contanier2">
      <div class="authorization" id="it1">
        <div class="form aut_item">
          <input placeholder="UserName" v-model="name">
          <input placeholder="Number" v-model="phone_number">
          <select class="building" @change="setBuilding($event)">
          <option selected disabled>Выберите корпус</option>
            <option v-for="building in buildings"
                    :key="building.id"
                    :value="building.name"
            >{{ building.name }}
            </option>
            </select>
          <input type="password" placeholder="Password" v-model="password">
          <input type="password" placeholder="Password again" v-model="password2"><br>
          <second-button style="width: 230px;"  @click="this.$router.push('/posts')">Зарегистрироваться</second-button>
        </div>
        <p v-if="error">{{ error }}</p>
        <div class="aut_item">
          <img style="width: 800px" src="@/assets/ref-img.png">
        </div>
      </div>

    </div>
    </form>
  </div>
  <footer>
    <img style="width: 14px" src="@/assets/f-icon.png"> 2022
  </footer>
</template>

<script>
import SecondButton from "@/components/SecondButton";
import FirstButton from "@/components/FirstButton";
import axios from 'axios'

export default {
  components: {
    SecondButton,
    FirstButton
  },
  data() {
    return {
      buildings: [],
      phone_number: '',
      name: '',
      building: '',
      password: '',
      password2: '',
      error: '',
      singUpContent: true
    }
  },
  methods: {
    setBuilding(e) {
      this.building = e.target.value
    },
    async submitForm() {
      this.errors = []
      if (this.phone_number === '' || this.name === '' || this.building === '' || this.password === '') {
        this.error = 'Введите все данные!'
        return 0;
      }

      if (!this.errors.length) {
        const formData = {
          phone_number: this.phone_number,
          name: this.name,
          building: this.building,
          password: this.password
        }
        await axios
            .post("/api/users/", formData)
            .catch(error => {
              if (error.response) {
                this.error = ('Что-то пошло не так.\nПопробуйте снова!')
              }
            })
        await axios
            .post('/auth/token/login/', {
              phone_number: formData['phone_number'],
              password: formData['password']
            })
            .then(response => {
              const token = response.data.auth_token
              this.$store.commit('setToken', token)

              axios.defaults.headers.common["Authorization"] = "Token " + token
              localStorage.setItem("token", token)
            })
        this.singUpContent = false
      }
    }
  }
}
</script>

<style scoped>
* {
  font-family: "Century Gothic";
  margin: 0;
  padding: 0;

}
body {
  background-color: #FFFCF2;
}

.flex-contanier {
  display: flex;
  justify-content: space-around;
  padding: 30px;


}

.second-contanier {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

.element1 {
  font-size: 40px;
  color: #403D39;

}

.element2 {
  font-size: 22px;
  color: #CCC5B9;
}

.general-contanier {
  display: flex;
  flex-direction: column;
}

input {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  height: 40px;
  width: 200px;
}

.flex-contanier2 {

  padding-top: 12%;
  background-color: #CCC5B9;
  display: flex;
  padding-bottom: 200px;
  justify-content: space-evenly;
}

.navbar {
  background-color: #FFFCF2;
  height: 80px;
  width: 100%;
  position: fixed;
}

a {
  color: #FFFCF2;
  transition: all 1s;
  text-decoration: none;
}

a:hover {
  color: #EB5E28;
}

img {
  border-radius: 120px;
}

.form {
  display: flex;
  flex-direction: column;

  margin-left: 10%;
  padding: 50px;
  border: 4px solid #403D39;
  border-radius: 30px;

}

footer {
  background-color: #FFFCF2;
  padding: 20px;
  padding-left: 50%;
}

.authorization {
  display: flex;
  flex-direction: row;
  justify-content: center;

}

.block_2_5 p {
  padding: 110px 10px;
  text-align: center;
}

.block_1_5:hover .block_2_5 {
  visibility: visible;
  transition: 3s;
  height: 335px;
  width: 500px;
  background: rgba(0, 0, 0, 0.6);
  border-radius: 120px;
  -webkit-transition: 1s;
  transform: translatey(-160px);
  -webkit-transform: translatey(-160px);

}

.block_1_5 :hover {
  transition: 1s;
  -webkit-transition: 0.6s;
}

.block_1 {
  overflow: hidden;
  position: relative;
  background-size: cover
}

.block_2 {
  position: absolute;
  visibility: hidden;
  left: 1px;
  font-size: 20px;
  color: #CCC5B9;
  top: 160px;
  transition: all 1s;
  width: 600px;
  height: 400px;
}

.block_2 p {
  padding: 110px 10px;
  text-align: center;
}

.block_1:hover .block_2 {
  visibility: visible;
  transition: 3s;
  width: 600px;
  height: 400px;
  background: rgba(0, 0, 0, 0.6);
  border-radius: 120px;
  -webkit-transition: 1s;
  transform: translatey(-160px);
  -webkit-transform: translatey(-160px);

}

.block_1:hover {
  transition: 1s;
  -webkit-transition: 0.6s;
}

</style>