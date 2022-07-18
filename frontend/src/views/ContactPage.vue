<template>
  <div>
    <nav-bar></nav-bar>
    <form-contact></form-contact>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import FormContact from "@/components/FormContact.vue";
export default {
  components: { NavBar, FormContact },
};
</script>

<style scoped></style>
