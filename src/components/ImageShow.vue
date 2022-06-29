<template>
  <div>
    <div class="fs-5 fw-light text-dark text-box mb-4">
      Select image to upload and press Detect :
    </div>
    <div class="my-img-box">
      <div class="row gy-4 gx-1">
        <div class="col-8">
          <input
            type="file"
            class="form-control"
            id="myfile"
            @change="onFileChange"
          />
        </div>
        <div>
          <button class="btn btn-primary me-2" @click="Predict">Predict</button>
          <button class="btn btn-outline-danger" @click="Remove">Remove</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageShow",
  methods: {
    onFileChange(e) {
      var file = e.target.files;
      if (!file.length) {
        return;
      }
      this.createImage(file[0]);
    },
    createImage(file) {
      var reader = new FileReader();
      reader.onload = (e) => {
        this.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    Predict() {
      console.log("Predict");
      console.log(document.getElementById("myfile").value);
      if (document.getElementById("myfile").value != "") {
        this.$emit("myImage", this.image);
      } else {
        alert("Please select your image");
      }
    },
    Remove() {
      console.log("Remove");
      document.getElementById("myfile").value = "";
      //this.$emit("myImage", this.image);
    },
  },
};
</script>

<style scpoe>
.my-img-box {
  padding-left: 18%;
}
.text-box-img {
  margin-left: 190px;
}
</style>
