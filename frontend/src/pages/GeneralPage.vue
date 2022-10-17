<template>
  <div class="general-contanier">
    <div class="flex-contanier navbar">
      <div class="flex-item element1">
        Fefu Service
      </div>
      <div class="second-contanier flex-item ">
        <first-button
            class="element2"
            @click="ShowWindow()"
        >
          Регистрация
        </first-button>
      </div>
    </div>
    <form @submit.prevent="submitForm">
      <div class="flex-contanier flex-contanier2">
        <div class="reristration">
          <p class="error m-0" v-if="error">{{ error }}</p>
          <input v-model="phone_number" placeholder="phone_number">
          <input v-model="password" type="password" placeholder="Password"><br>
          <second-button style="width: 200px; margin-left: 17%" @click="setGeneralPage">Войти</second-button>
          <br>
          <div style="font-size: 14px">Если у вас нет аккаунта,<a
              @click="ShowWindow">зарегистрируйся</a></div>
        </div>
        <div class="text">Будь с нами,<br>
          зарегистрируйся!
        </div>
      </div>
    </form>
    <dialog-window
        v-model:show="Window"
    >
      <form @submit.prevent="submitForm">
        <div class="flex-contanier4">
          <div class="registration">
            <div class="form reg_item">
              <h1 style="color: #403D39">Регистрация</h1>
              <input placeholder="UserName" v-model="name">
              <input placeholder="Number" v-model="phone_number">
              <select  class="filter_item">
                <option v-for="bul in buildings" v-bind:key="bul.id" v-bind:value="bul.id"> {{ bul.title }}</option>
              </select>
              <input type="password" placeholder="Password" v-model="password">
              <input type="password" placeholder="Password again" v-model="password2"><br>
              <second-button style="width: 230px;" @click="this.$router.push('/posts')">Зарегистрироваться
              </second-button>
            </div>
            <p v-if="error">{{ error }}</p>
            <div class="aut_item">
              <img style="width: 800px" src="@/assets/ref-img.png">
            </div>

          </div>

        </div>
      </form>

    </dialog-window>
  </div>
  <footer>
    <img style="width: 14px" src="@/assets/f-icon.png"> 2022
  </footer>
</template>

<script>
import FirstButton from "@/components/FirstButton";
import axios from 'axios';
import DialogWindow from "@/components/DialogWindow";
import SecondButton from "@/components/SecondButton";

export default {
  components: {
    SecondButton,
    DialogWindow,
    FirstButton
  },
  name: 'LogIn',
  data() {
    return {
      phone_number: '',
      password: '',
      error: '',
      loginVisible: false,
      signupVisible: false,
      Window: false,
      buildings: [],
    }
  },
  mounted() {
    this.getBuildings()

  },

  methods: {
    ShowWindow() {
      this.Window = true
      console.log(this.Window)
    },
    async submitForm() {
      if (this.phone_number === '' || this.password === '') {
        this.error = 'Введите все данные!'
        return 0;
      }

      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        phone_number: this.phone_number,
        password: this.password
      }
      await axios
          .post("/auth/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = "Token " + token
            localStorage.setItem("token", token)
            const toPath = this.$route.query.to || '/posts'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              this.error = 'Неверный номер телефона или пароль. Попробуйте снова!'
            }
          })
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
select {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  height: 40px;
}
input {
  border-radius: 10px;
  border: 2px solid #403D39;
  padding: 3px;
  margin: 10px;
  height: 30px;
}

.reristration {
  display: flex;
  flex-direction: column;
  width: 300px;
  border: 4px solid #403D39;
  border-radius: 30px;
  padding: 70px;
}

.flex-contanier2 {
  padding-top: 18%;
  background-color: #CCC5B9;
  display: flex;
  padding-bottom: 200px;
  justify-content: space-evenly;
}

.text {
  padding-top: 50px;
  font-size: 70px;
}

.flex-contanier {
  display: flex;
  justify-content: space-around;
  padding: 30px;
  margin-bottom: 80px;
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

footer {
  background-color: #FFFCF2;
  padding: 20px;
  padding-left: 50%;
}


.navbar {
  background: #FFFCF2;
  margin-bottom: 70px;
}

.registration {
  display: flex;
  flex-direction: row;
  justify-content: center;


}

.form {
  display: flex;
  flex-direction: column;
  margin-left: 10%;
  padding: 30px;
  background: #CCC5B9;
  border: 4px solid #FFFCF2;
  border-radius: 30px;

}

.flex-contanier2 {
  padding-top: 2%;
  display: flex;
  padding-bottom: 2%;
  justify-content: space-evenly;
}
</style>