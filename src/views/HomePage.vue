<template>
  <div>
    <nav-bar></nav-bar>
    <text-content></text-content>
    <div v-if="!imageBefore">
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
            Image with grad cam analysis
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
      <div class="d-grid gap-2 col-1 mx-auto">
        <button class="btn btn-primary" @click="back">Back</button>
      </div>
    </div>
  </div>
</template>

<script>
import TextContent from "@/components/TextContent.vue";
import NavBar from "../components/NavBar.vue";
import ImageShow from "@/components/ImageShow.vue";

export default {
  components: { NavBar, TextContent, ImageShow },
  name: "HomePage",
  data() {
    return {
      imageBefore: "",
      imageAfter: "",
      result: "Test",
    };
  },
  methods: {
    setImage(image) {
      this.imageBefore = image;
      this.imageAfter = image;
    },
    back() {
      this.imageBefore = "";
      this.imageAfter = "";
    },
  },
};
</script>

<style>
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
