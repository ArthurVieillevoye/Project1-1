<template>
  <card-layout title="Stable Semantics" :info="stable">
    <div v-if="stable.length !== 0">
      <ul v-for="stab in stable" :key="stab">
        <li class="p-2">{{ stab }}</li>
      </ul>
    </div>
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
