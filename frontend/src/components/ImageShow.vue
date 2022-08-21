<template>
  <div>
    <div class="fs-5 fw-light text-dark text-box mb-2">
      Select image to upload and press predict :
    </div>
    <div class="dropzone" :class="{ 'drop-active': drag }" @dragenter.prevent="active" @dragleave.prevent="active"
      @dragover.prevent @drop.prevent="onFileDrop">
      <div v-if="!this.haveImg">
        <div class="browse-img">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="60" fill="currentColor" class="bi bi-image"
            viewBox="0 0 16 16">
            <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z" />
            <path
              d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2h-12zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1h12z" />
          </svg>
        </div>
        <div>
          <span>Drop your image here, or </span>
          <label for="dropzonefile">browse</label>
          <input type="file" id="dropzonefile" @change="onFileChange" />
        </div>
      </div>
      <div v-else>
        <img class="img-show" :src="image" />
        <button class="button-remove" @click="Remove">X</button>
      </div>
    </div>
    <div class="button-center">
      <div>
        <button class="predict-button" @click="Predict">
          <div v-if="!predicting">
            Predict
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="white" class="bi bi-arrow-right-short"
              viewBox="0 0.5 16 16">
              <path fill-rule="evenodd"
                d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z" />
            </svg>
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
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ImageShow",
  data() {
    return {
      image: null,
      fileUpload: null,
      haveImg: false,
      drag: false,
      predicting: false,
    };
  },
  components: {},
  methods: {
    active() {
      this.drag = !this.drag;
    },
    onFileChange(e) {
      var file = e.target.files;
      console.log(file);
      if (!file.length) {
        return;
      }
      this.createImage(file[0]);
      this.fileUpLoad = file[0];
    },
    onFileDrop(e) {
      this.active();
      var file = e.dataTransfer.files;
      console.log(file);
      if (!file.length) {
        return;
      }
      this.createImage(file[0]);
      this.fileUpLoad = file[0];
    },
    createImage(file) {
      if (!file.type.match('image.*')) {
        alert('Select an image');
        return;
      }
      this.haveImg = true;
      var reader = new FileReader();
      reader.onload = (e) => {
        this.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    Predict() {
      console.log("Predict");
      console.log(this.fileUpLoad);
      if (this.haveImg) {
        console.log(this.fileUpload);
        const fd = new FormData();
        fd.append("image", this.fileUpLoad, this.fileUpLoad.name);
        this.predicting = true;
        axios
          .post("http://127.0.0.1:5000/upload", fd, { //Nest 8000, Flask 5000
            // http://localhost:5000/upload
            PredictProgress: (uploadEvent) => {
              console.log(
                "Predict Progress: " +
                Math.round((uploadEvent.loaded / uploadEvent.total) * 100) +
                "%"
              );
            },
          })
          .then((res) => {
            console.log(res);
            this.predicting = false;
            this.$emit("myImage", this.image, res.data.file, res.data.myResult);
          })
          .catch(() => {
            this.predicting = false;
            alert("server failure");
          });
      } else {
        alert("Please select your image");
      }
    },
    Remove() {
      console.log("Remove");
      this.haveImg = false;
      this.predicting = false;
      //this.$emit("myImage", this.image);
    },
  },
};
</script>

<style scoped>
/* .text-box-img {
  margin-left: 190px;
} */
.text-box {
  margin-left: 18%;
}

.dropzone {
  border: 1px dashed black;
  width: 65%;
  height: 250px;
  margin: auto;
  margin-bottom: 25px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 16px;
  transition: 0.1s ease all;
  position: relative;
}

.dropzone label {
  padding-left: 5px;
  text-decoration-line: underline;
  /* color: aliceblue;
  background-color: green; */
  transition: 0.1s ease all;
}

.dropzone label:hover {
  cursor: pointer;
}

.dropzone input {
  display: none;
}

.drop-active {
  border: 2px dashed #22707c;
}

.button-center {
  height: 60px;
  width: 150px;
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

.button-remove {
  width: 30px;
  height: 30px;
  border-radius: 30px;
  font-weight: 600;
  color: red;
  background-color: white;
  border: 2px solid red;
  position: absolute;
  top: 10px;
  right: 10px;
}

.browse-img {
  width: 40px;
  margin: auto;
}

.img-show {
  height: 220px;
}

.lds-ellipsis {
  margin-left: 5px;
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
