<template>
  <div>
    <template v-for="question in questions">
      <div
        v-if="question.question"
        :key="question.id"
        class="flex p-3 justify-between"
      >
        {{ question.question }}
        <input
          type="checkbox"
          :id="question.id"
          v-model="checked"
          :value="question.id"
          true-value="True"
          false-value="False"
        />
      </div>
    </template>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "FactsCard",

  data() {
    return {
      checked: [],
    };
  },

  methods: {},

  computed: {
    ...mapGetters({ questions: "getQuestions" }),
  },

  mounted() {
    this.$store.dispatch("fetchQuestions");
  },
};
</script>

<style></style>
