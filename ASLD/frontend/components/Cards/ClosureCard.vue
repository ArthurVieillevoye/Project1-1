<template>
  <card-layout>
    <div v-if="closure.length !== 0">
      <ul v-for="(close, index) in closure" :key="index">
        <li class="py-1">{{ close }}</li>
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
