<template>
  <card-layout>
    <div v-if="args.length !== 0">
      <ul v-for="(arg, index) in args" :key="index">
        <li class="p-2">{{ arg }}</li>
      </ul>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";
import TreeCard from "./TreeCard.vue";
export default {
  components: { TreeCard, CardLayout },
  name: "ArgumentsCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ args: "getArgs" }),
  },
};
</script>

<style></style>
