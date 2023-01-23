<template>
  <card-layout>
    <div v-if="stableFilter.length !== 0">
      <ul v-for="(stable, index) in stableFilter" :key="index" class="pb-3">
        <ul v-for="(argument, index) in stable" :key="index">
          <li class="py-1">{{ argument }}</li>
        </ul>
      </ul>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "StableFilterCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ stableFilter: "getSEFilter" }),
  },
};
</script>

<style></style>
