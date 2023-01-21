<template>
  <card-layout>
    <div v-if="groundedFilter.length !== 0">
      <OrganizationChart :datasource="transformDataToTree" />
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

  components: {
    OrganizationChart,
  },

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ groundedFilter: "getGEFilter" }),

    transformDataToTree() {
      return {
        id: "1",
        name: "1",
        title: this.groundedFilter[0],
      };
    },
  },

  methods: {},
};
</script>

<style></style>
