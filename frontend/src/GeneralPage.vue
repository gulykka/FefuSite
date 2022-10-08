<template>

  <div class="general-contanier">
    <div class="flex-contanier navbar">
      <div class="flex-item element1">
        Fefu Service
      </div>
      <div class="second-contanier flex-item ">
        <first-button
            class="element2"
            @click="showDialog">
          Регистрация
        </first-button>
        <dialog-window v-model:show="dialogVisible">
          <div class="authorization" id="it1">
            <div class="form aut_item">
              <input placeholder="UserName">
              <input placeholder="Number">
              <input placeholder="Korpus">
              <input placeholder="Password">
              <input placeholder="Password again"><br>
              <second-button style="width: 200px;">Зарегистрироваться</second-button>
            </div>
            <div class="aut_item">
              <img style="width: 700px" src="@/assets/ref-img.png">
            </div>
          </div>
        </dialog-window>
        <first-button
            class="element2"
            href=" http://localhost:8080"
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
    <div class="flex-contanier flex-contanier2">
      <div class="reristration">
        <input placeholder="UserName">
        <input placeholder="Password"><br>
        <second-button style="width: 200px; margin-left: 17%">Войти</second-button>
        <br>
        <div style="font-size: 14px">Если у вас нет аккаунта,<a @click="showDialog">зарегистрируйся</a></div>
      </div>
      <div class="text">Будь с нами,<br>
        зарегистрируйся!
      </div>
    </div>

  </div>


  <footer><img style="width: 14px" src="@/assets/f-icon.png"> 2022</footer>
</template>

<script>
import SecondButton from "@/components/SecondButton";
import FirstButton from "@/components/FirstButton";
import DialogWindow from "@/components/DialogWindow";

export default {
  components: {
    DialogWindow,
    SecondButton,
    FirstButton
  },
  data() {
    return {
      dialogVisible: false,
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true
    },

  }
}
</script>

<style>
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

img {
  width: 600px;
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

.flex-contanier1 {
  background-color: #CCC5B9;
  display: flex;
  padding-bottom: 200px;
  justify-content: space-evenly;
}

.flex-contanier2 {
  padding-top: 280px;
  background-color: #CCC5B9;
  display: flex;
  padding-bottom: 200px;
  justify-content: space-evenly;
}

.text {
  padding-top: 50px;
  font-size: 70px;
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

.form {
  display: flex;
  flex-direction: column;
  margin-top: 6%;
  margin-left: 10%;
  padding: 7px;
  border-radius: 10px;

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

.base_img img:hover {
  width: 250px;
  height: 250px;
  border-radius: 130px;
}

.base_img img {
  width: 230px;
  height: 230px;
  border: 6px solid #403D39;
  border-radius: 120px;
}

.base {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

.base_i {
  width: 50%;
}
</style>
