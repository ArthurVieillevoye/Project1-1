<template>
  <card-layout>
    <div v-if="grounded.length !== 0">
      <ul v-for="(ground, index) in grounded" :key="index">
        <li class="py-1">{{ ground }}</li>
      </ul>
    </div>
    <div v-if="grounded.length === 0" class="flex justify-center pt-16">
      <h5>No grounded extension was identified.</h5>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "GroundedCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ grounded: "getGrounded" }),
  },
};
</script>

<style></style>
