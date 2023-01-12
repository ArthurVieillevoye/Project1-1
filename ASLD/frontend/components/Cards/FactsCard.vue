<template>
  <div
    class="bg-white/80 backdrop-blur-md rounded h-full flex-col p-3 overflow-auto"
  >
    <!-- <div class="flex justify-between overflow-auto"></div> -->
    {{ questions }}
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "FactsCard",

  computed: {
    ...mapGetters({ questions: "getQuestions" }),
  },

  mounted() {
    this.$store.dispatch("fetchQuestions");
  },
};
</script>

<style></style>
