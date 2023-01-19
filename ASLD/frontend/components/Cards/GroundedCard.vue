<template>
  <card-layout>
    <div v-if="grounded.length !== 0">
      <ul v-for="(ground, index) in grounded" :key="index">
        <li class="p-2">{{ ground }}</li>
      </ul>
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
