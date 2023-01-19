<template>
  <card-layout>
    <div v-if="stable.length !== 0">
      <ul v-for="(stab, index) in stable" :key="index" class="pb-3">
        <ul v-for="(semantic, index) in stab" :key="index">
          <li class="py-1">{{ semantic }}</li>
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
