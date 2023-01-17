<template>
  <card-layout title="Closure Arguments" :info="closure">
    <div v-if="closure.length !== 0">
      <ul v-for="close in closure" :key="close">
        <li class="p-2">{{ close }}</li>
      </ul>
    </div>
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
