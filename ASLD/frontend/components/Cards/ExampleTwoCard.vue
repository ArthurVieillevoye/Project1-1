<template>
  <div>
    <template v-for="example in examples">
      <div
        v-if="example.question"
        :key="example.id"
        class="flex p-3 justify-between"
      >
        {{ example.question }}
        <input
          type="checkbox"
          :id="example.id"
          v-model="checked"
          :value="example.id"
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
  name: "ExampleTwoCard",

  data() {
    return {
      checked: [],
    };
  },

  methods: {},

  watch: {
    checked(newFact) {
      this.$store.commit("SET_FACTS", newFact);
    },
  },

  computed: {
    ...mapGetters({ examples: "getExamplesTwo" }),
  },

  mounted() {
    this.$store.dispatch("fetchToyExamplesTwo");
  },
};
</script>

<style></style>
