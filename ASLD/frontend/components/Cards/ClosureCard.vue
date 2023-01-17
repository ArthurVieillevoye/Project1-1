<template>
  <card-layout title="Closure Arguments">
    <div v-if="closure.length !== 0">{{ closure }}</div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "ClosureCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ closure: "getClosure" }),
  },
};
</script>

<style></style>
