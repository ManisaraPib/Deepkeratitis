<template>
  <div class="my-box">
    <div class="text-box">
      <div class="fs-4 fw-bolder text-dark">Deepkeratitis</div>
      <div class="fs-6 fw-bold text-dark mb-2">in version 1</div>
      <div class="fs-6 fw-light text-dark sec-text">
        The Deep Keratitis project builds AI to classify corneal infections
        between fungal keratitis and bacterial keratitis using deep learning
      </div>
    </div>
    <div class="my-box-img">
      <img src="../image/EYE.png" class="my-image" />
    </div>
  </div>
</template>

<script>
export default {
  name: "TextContent",
};
</script>

<style scoped>
.text-box {
  margin-left: 60px;
}

.my-box {
  padding: 20px;
  background: #dddddd;
  border-radius: 10px;
  width: 65%;
  margin: auto;
  margin-bottom: 30px;
  position: relative;
}

.my-box-img {
  position: absolute;
  height: 130px;
  width: 130px;
  top: 8%;
  right: 40px;
  background: #eaf0f1;
  border-radius: 130px;
}

.my-image {
  height: 65px;
  margin-top: 35px;
  margin-left: 7px;
}

.sec-text {
  width: 60%;
}

@media (max-width: 1000px) {
  .my-box-img {
    display: none;
  }
}

@media (max-width: 850px) {
  .sec-text {
    display: none;
  }
}
</style>
