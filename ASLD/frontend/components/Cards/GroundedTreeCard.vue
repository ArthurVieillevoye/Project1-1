<template>
  <card-layout>
    <div v-if="groundedFilter.length !== 0">
      <OrganizationChart :datasource="groundedFilter" />
    </div>
  </card-layout>
</template>

<script>
import OrganizationChart from "vue-organization-chart";
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "GroundedTreeCard",

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
