<template>
  <div class="general-contanier">
    <div class="flex-contanier navbar">
      <div class="flex-item element1">
        Fefu Service
      </div>
      <div class="second-contanier flex-item ">
        <first-button
            class="element2"


            @click="$router.push('/registration')"
        >
          Регистрация
        </first-button>
        <first-button
            v-if="!this.$store.state.isAuthenticated"
            class="element2"
            @click="showloginDialog"
        >
          Авторизация
        </first-button>
        <first-button
            class="element2"
            href="#about"
        >
          О нас
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
        <div style="font-size: 14px">Если у вас нет аккаунта,<a @click="showsignupDialog" v-if="!this.$store.state.isAuthenticated">зарегистрируйся</a></div>
      </div>
      <div class="text">Будь с нами,<br>
        зарегистрируйся!
      </div>
    </div>
    <div class="base" id="about">
      <div class="base_item" style="font-size: 25px; padding-left: 20px">Платформа создана для студентов<br>
        Дальневосточного Федерального
        Университета<br>
        <div class="block_1_5"><br><img class="base_item" style="width: 500px" src="@/assets/2.jpg">
          <div class="block_2_5"><p>Мастер предоставляет услуги<br>Клиент нуждается в услуге</p></div>
        </div>
      </div>
      <div class=" base_item block_1">
        <img class="base_item info" style="width: 600px" src="@/assets/1.jpg">
        <div class="block_2">
          <p>Сайт предназначен для быстрого и комфортного доступа ко многим услугам на кампусе ДВФУ</p>
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

  name: 'LogIn',
  data() {
    return {
        phone_number: '',
        password: '',
        error: '',
        loginVisible: false,
        signupVisible: false,
    }
  },
  methods: {
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
        showloginDialog() {
          this.loginVisible = true;
          document.querySelector('body').style.overflow = 'hidden'
        },
        showsignupDialog() {
          this.signupVisible = true;
          document.querySelector('body').style.overflow = 'hidden'
        },
        closeDialog() {
          this.loginVisible = false;
          this.signupVisible = false;
          document.querySelector('body').removeAttribute('style')
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
  height: 30px;
}

/*input:hover {*/
/*  box-shadow: 1px 1px 5px #EB5E28;*/
/*}*/

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
  margin-bottom: 160px;
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

.base {
  background-color: #CCC5B9;
  padding-bottom: 100px;
  display: flex;
  flex-direction: row;
  margin-bottom: 50px;
  justify-content: space-evenly;
}

.block_1_5 {
  overflow: hidden;
  position: relative;
  background-size: cover
}

.block_2_5 {
  position: absolute;
  visibility: hidden;
  left: 1px;
  font-size: 20px;
  color: #CCC5B9;
  top: 190px;
  transition: all 1s;
  height: 335px;
  width: 500px;

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
.navbar {
  background: #FFFCF2;
  margin-bottom: 100px;
}
</style>