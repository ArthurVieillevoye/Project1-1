<template>
  <card-layout>
    <div v-if="groundedFilter.length !== 0">
      <ul v-for="(grounded, index) in groundedFilter" :key="index">
        <li class="py-1">{{ grounded }}</li>
      </ul>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "GroundedFilterCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ groundedFilter: "getGEFilter" }),
  },
};
</script>

<style></style>
