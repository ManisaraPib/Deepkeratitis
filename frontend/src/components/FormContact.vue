<template>
  <div class="my-box">
    <div class="fs-3 fw-bolder text-center mb-4">Contact us</div>
    <div><input type="text" placeholder="Name" v-model="form.name" /></div>
    <div>
      <input
        type="email"
        placeholder="Email"
        v-model="form.email"
        :class="{ 'red-border': wrongEmail }"
      />
    </div>
    <div>
      <textarea placeholder="Message" v-model="form.message"></textarea>
    </div>
    <div>
      <button class="submit-button" @click="sendMessage">
        <div v-if="!sending">
          {{ textButton }}
        </div>
        <div v-else>
          <div class="lds-ellipsis">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
          </div>
        </div>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "FromContact",
  data() {
    return {
      form: {
        name: "",
        email: "",
        message: "",
      },
      wrongEmail: false,
      textButton: "Send message",
      sending: false,
    };
  },
  methods: {
    sendMessage() {
      console.log(this.form);
      if (
        this.form.name == "" ||
        this.form.email == "" ||
        this.form.message == ""
      ) {
        alert("Please fill out the form");
        return;
      }
      this.validateEmail();
      if (this.wrongEmail) {
        return;
      }
      this.sending = true;
      // this.textButton = "Sending...";
      axios
        .post("http://127.0.0.1:5000/contact", this.form) //Nest 8000, Flask 5000
        .then((res) => {
          if (res.data.message == "success") {
            alert("Success");
            this.sending = false;
          }
          // this.textButton = "Send message";
        })
        .catch(() => {
          this.sending = false;
          // this.textButton = "Send message";
          alert("server failure");
        });
    },
    validateEmail() {
      if (!/^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/.test(this.form.email)) {
        this.wrongEmail = true;
        alert("Please type correct email");
      } else {
        this.wrongEmail = false;
      }
    },
  },
};
</script>

<style scoped>
input,
textarea {
  width: 350px;
  height: 35px;
  padding: 20px;
  margin-bottom: 15px;
  border: none;
  background-color: rgb(245, 245, 245);
}

textarea {
  padding-top: 10px;
  height: 85px;
}
.my-box {
  width: 350px;
  margin: auto;
}

.submit-button {
  height: 45px;
  width: 350px;
  color: white;
  background-color: #555555;
  border: none;
  border-radius: 8px;
}

.red-border {
  border: 2px solid red;
}

.submit-button:hover {
  background-color: black;
}

.lds-ellipsis {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ellipsis div {
  position: absolute;
  top: 17px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
  animation-timing-function: cubic-bezier(0, 1, 1, 0);
}
.lds-ellipsis div:nth-child(1) {
  left: 8px;
  animation: lds-ellipsis1 0.6s infinite;
}
.lds-ellipsis div:nth-child(2) {
  left: 8px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(3) {
  left: 32px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(4) {
  left: 56px;
  animation: lds-ellipsis3 0.6s infinite;
}
@keyframes lds-ellipsis1 {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes lds-ellipsis3 {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0);
  }
}
@keyframes lds-ellipsis2 {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(24px, 0);
  }
}
</style>
