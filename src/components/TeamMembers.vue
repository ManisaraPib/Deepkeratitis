<template>
  <div>
    <div class="my-box">
      <hr class="line-team solid" />
      <div class="line-team text fs-5 fw-bold text-dark mb-2">Team Members</div>
      <div class="btn-group" role="group">
        <button class="btn" :class="{ 'btnd': developer, 'btnw': contributor }" @click="Developer()">Developer</button>
        <button class="btn" :class="{ 'btnd': contributor, 'btnw': developer }"
          @click="Contributor()">Contributor</button>
      </div>
    </div>
    <div v-if="developer">
      <div class="my-box row mb-5">
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white ">
          <img src="../image/fern.jpg" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">Manisara Piboon</h5>
            <p class="mb-4 text-muted fw-light fs-6">
              UX/UI Designer and Front-end Developer
            </p>
          </div>
        </div>
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white">
          <img src="../image/gj.jpg" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">
              Prince Paris Jackson Wongsaroj
            </h5>
            <p class="mb-4 text-muted fw-light fs-6">Back-end Developer</p>
          </div>
        </div>
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white">
          <img src="../image/tt.png" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">Chanakarn Rungnisakorn</h5>
            <p class="mb-4 text-muted fw-light fs-6">Data Modeling Analyst</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="my-box row mb-5">
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white ">
          <img src="../image/Amit.jpeg" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">Amit Kumar Goash</h5>
            <p class="mb-4 text-muted fw-light fs-6">Master Student</p>
          </div>
        </div>
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white ">
          <img src="../image/Ratchainant_2019.jpeg" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">
              Ratchainant Thammasudjarit, Ph.D.
            </h5>
            <p class="mb-4 text-muted fw-light fs-6">Data Scientist</p>
          </div>
        </div>
        <div class="members col-lg-4 col-md-6 p-3 mb-3 bg-white ">
          <img src="../image/p.jpg" class="image rounded img-fluid rounded-circle mt-2" />
          <div class="name-team">
            <h5 class="mb-2 mt-3 fw-bold fs-5">Passara Jongkhajornpong, M.D.</h5>
            <p class="mb-4 text-muted fw-light fs-6">
              Cornea and Refractive Surgery
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeamMembers",
  data() {
    return {
      developer: true,
      contributor: false,
    };
  },
  methods: {
    Developer() {
      this.developer = true
      this.contributor = false
    },
    Contributor() {
      this.developer = false
      this.contributor = true
    }
  }
};
</script>

<style scoped>
.my-box {
  margin-left: 100px;
  margin-top: 30px;
}

.name-team {
  text-align: center;
}

.members {
  width: 400px;
  margin-right: 24px;
  border-radius: 20px;
  box-shadow: 6px 6px 20px 2px rgba(0, 0, 0, 0.1);

}

.image {
  position: relative;
  margin: auto;
  margin-left: 115px;
  height: 140px;
  width: 140px;
}

.btnd {
  height: 45px;
  width: 160px;
  color: white;
  background-color: #555555;
  border: none;
  border-radius: 8px;
}

.btnw {
  height: 45px;
  width: 160px;
  color: #555555;
  background-color: #dddddd;
  border: none;
  border-radius: 8px;
}

.line-team {
  width: 1260px;
  margin: center;
  margin-top: 120px;
}

.text {
  margin-top: 55px;
}

.btn-check:focus+.btn,
.btn:focus {
  outline: 0;
  box-shadow: none
}
</style>
