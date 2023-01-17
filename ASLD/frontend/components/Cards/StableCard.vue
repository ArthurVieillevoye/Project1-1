<template>
  <card-layout title="Stable Semantics">
    <div v-if="stable.length !== 0">{{ stable }}</div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "StableCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ stable: "getStable" }),
  },
};
</script>

<style></style>
