<template>
  <card-layout>
    <div v-if="undercutting.length !== 0">
      <ul v-for="(undercut, index) in undercutting" :key="index">
        <li class="py-1">{{ undercut }}</li>
      </ul>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "UndercuttingCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ undercutting: "getUndercutting" }),
  },
};
</script>

<style></style>
