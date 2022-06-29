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
    </div>
    <div class="white-box"></div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style scope>
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
  height: 65px;
}

@media (max-width: 850px) {
  .rama-text {
    display: none;
  }
  .rama-text-short {
    display: inline;
  }
}
</style>
