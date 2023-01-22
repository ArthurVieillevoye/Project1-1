<template>
  <card-layout>
    <div v-if="groundedTree.length !== 0">
      <div v-for="(tree, index) in groundedTree" :key="index">
        <OrganizationChart :datasource="tree" />
      </div>
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
    ...mapGetters({ groundedTree: "getGETree" }),

    transformDataToTree() {
      return {
        id: "1",
        name: "1",
        title: this.groundedTree[0],
      };
    },
  },

  methods: {},
};
</script>

<style></style>
