<template>
  <div>
    <div class="top-box"></div>
    <div class="main-box">
      <img src="../image/rama-logo.png" class="rama-logo" />
      <span class="fs-4 fw-light text-white rama-text">
        Mahidol University Faculty of Medicine Ramathibodi Hospital
      </span>
      <span class="fs-4 fw-light text-white rama-text-short">
        Mahidol University
      </span>
    </div>
    <div class="buttom-box">
      <div class="fs-5 fw-light text-white rama-text-bottom">Deepkeratitis</div>
      <div class="fs-6 fw-lighter text-white text-link">
        <router-link to="/home"><span class="my-img">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-house"
              viewBox="-5 -1 22 22">
              <path fill-rule="evenodd"
                d="M2 13.5V7h1v6.5a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5V7h1v6.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5zm11-11V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z" />
              <path fill-rule="evenodd"
                d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z" />
            </svg>
          </span>
          Home
        </router-link>
        |
        <a href="https://pubmed.ncbi.nlm.nih.gov/34581296/" target="_blank"><svg xmlns="http://www.w3.org/2000/svg"
            width="20" height="20" fill="currentColor" class="bi bi-file-earmark-text" viewBox="-5 -1 22 22">
            <path
              d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5zm0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5z" />
            <path
              d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5L9.5 0zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5z" />
          </svg>
          Full text</a>
        |
        <router-link to="/contact"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
            class="bi bi-envelope" viewBox="-5 -1 22 22">
            <path
              d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" />
          </svg>
          Contact</router-link>
        |
      </div>
    </div>
    <div class="white-box"></div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scoped>
.top-box {
  background-color: #0134ad;
  height: 8px;
  width: 100%;
}

.main-box {
  background-color: #0a3d5d;
  height: 80px;
  width: 100%;
  position: relative;
}

.buttom-box {
  background-color: #22707c;
  height: 44px;
  width: 100%;
  position: relative;
}

.rama-logo {
  width: 73px;
  height: 60px;
  position: relative;
  top: 8px;
  left: 18%;
}

.rama-text {
  position: relative;
  top: 15px;
  left: 20%;
}

.rama-text-short {
  position: relative;
  top: 15px;
  left: 20%;
  display: none;
}

.rama-text-bottom {
  position: absolute;
  top: 6px;
  left: 18%;
}

.white-box {
  height: 35px;
}

.text-link {
  position: absolute;
  top: 9px;
  right: 18%;
}

a {
  color: white;
  text-decoration: none;
}

a:hover {
  font-weight: 400;
}

@media (max-width: 850px) {
  .rama-text {
    display: none;
  }

  .rama-text-short {
    display: inline;
  }

  .text-link {
    display: none;
  }
}
</style>
