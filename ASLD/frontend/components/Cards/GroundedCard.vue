<template>
  <card-layout title="Grounded Semantics">
    <div v-if="grounded.length !== 0">{{ grounded }}</div>
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
