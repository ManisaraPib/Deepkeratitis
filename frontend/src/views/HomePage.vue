<template>
  <div>
    <nav-bar></nav-bar>
    <div v-if="!imageBefore">
      <text-content></text-content>
      <image-show @myImage="setImage"></image-show>
    </div>
    <div v-else>
      <span class="fs-5 fw-light text-dark text-box mb-5">
        Result :
        <span class="my-result">{{ result }}</span>
      </span>
      <div class="row justify-content-center mt-3">
        <div class="col-4 pe-4 my-img-l">
          <div class="text-center fs-5 fw-light">Original image</div>
          <img :src="imageBefore" class="my-3 my-img" />
        </div>
        <div class="col-4 ps-4">
          <div class="text-center fs-5 fw-light grap-cam">
            Image with Grad-Cam Analysis
          </div>
          <div class="text-center fs-5 fw-light grap-cam-short">
            Grad cam analysis
          </div>
          <div class="text-center fs-5 fw-light grap-cam-very-short">
            Grad cam
          </div>
          <img :src="imageAfter" class="my-3 my-img" />
        </div>
      </div>
      <div class="left18"></div>
      <div class="left64">
        <div class="button-center">
          <button class="predict-button" @click="back">
            Back
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
              class="bi bi-arrow-left-short" viewBox="0 0.5 16 16">
              <path fill-rule="evenodd"
                d="M12 8a.5.5 0 0 1-.5.5H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5a.5.5 0 0 1 .5.5z" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TextContent from "../components/TextContent.vue";
import NavBar from "../components/NavBar.vue";
import ImageShow from "../components/ImageShow.vue";

export default {
  components: { NavBar, TextContent, ImageShow },
  name: "HomePage",
  data() {
    return {
      imageBefore: "",
      imageAfter: "",
      result: "",
    };
  },
  methods: {
    setImage(image, image2, result) {
      this.imageBefore = image;
      this.imageAfter = image2;
      this.result = result;
    },
    back() {
      this.imageBefore = "";
      this.imageAfter = "";
      this.result = "";
    },
  },
};
</script>

<style scoped>
.left18 {
  height: 20px;
  width: 18%;
  display: inline-block;
}

.left64 {
  width: 60%;
  display: inline-block;
}

.my-content {
  border: 1px solid black;
}

.my-result {
  color: red;
}

.my-img {
  max-height: 400px;
  width: 100%;
}

.my-img-l {
  float: right;
}

.grap-cam {
  display: block;
}

.grap-cam-short {
  display: none;
}

.grap-cam-very-short {
  display: none;
}

.text-box {
  margin-left: 18%;
}

.button-center {
  width: 120px;
  margin: auto;
}

.predict-button {
  height: 45px;
  width: 120px;
  margin: auto;
  margin-left: 20px;
  color: white;
  background-color: #555555;
  border: none;
  border-radius: 8px;
}

.predict-button:hover {
  background-color: rgb(0, 0, 0);
}

@media (max-width: 850px) {
  .grap-cam {
    display: none;
  }

  .grap-cam-short {
    display: block;
  }

  .grap-cam-very-short {
    display: none;
  }
}

@media (max-width: 560px) {
  .grap-cam {
    display: none;
  }

  .grap-cam-short {
    display: none;
  }

  .grap-cam-very-short {
    display: block;
  }
}
</style>
