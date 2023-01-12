<template>
  <div class="bg-white/80 h-full backdrop-blur-md rounded flex flex-col p-3">
    <div class="flex-col">
      {{ questions }}
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "QuestionsCard",

  computed: {
    ...mapGetters({ questions: "getQuestions" }),
  },

  mounted() {
    this.$store.dispatch("fetchQuestions");
  },
};
</script>

<style></style>
