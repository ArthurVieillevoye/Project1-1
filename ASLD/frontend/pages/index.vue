<template>
  <div class="flex flex-row overflow-auto space-x-4 h-full w-full">
    <TableauCard />
    <div
      class="flex flex-col w-1/3 h-full bg-white/80 backdrop-blur-md rounded"
    >
      <div class="flex space-x-4 p-3 justify-center">
        <span
          v-for="tab in tabs"
          :key="tab.name"
          class="hover:border-b"
          @click="selectTab(tab.name)"
          :class="tab.name == selectedTab ? 'border-green-400  border-b-4' : ''"
        >
          {{ tab.name }}
        </span>
      </div>
      <div class="overflow-auto h-96">
        <FactsCard v-if="selectedTab === 'Facts'" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexPage",

  data() {
    return {
      tabs: [{ name: "Facts" }],
      selectedTab: "Facts",
    };
  },

  methods: {
    selectTab(selected) {
      this.selectedTab = selected;
    },
  },

  mounted() {
    // this.$axios.get("http://localhost:8000/api/hello");
  },
};
</script>
