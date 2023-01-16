<template>
  <div class="flex flex-row space-x-4 w-full">
    <TableauCard />
    <div
      class="flex flex-col w-1/3 h-full bg-gray-200/80 backdrop-blur-md rounded"
    >
      <div class="flex space-x-4 py-2 justify-center h-12">
        <span
          v-for="tab in tabs"
          :key="tab.name"
          class="hover:border-b border-green-400"
          @click="selectTab(tab.name)"
          :class="
            tab.name == selectedTab
              ? 'border-green-400  border-b-4 drop-shadow-md'
              : ''
          "
        >
          {{ tab.name }}
        </span>
      </div>
      <div class="overflow-auto h-full rounded bg-gray-200/80 backdrop-blur-md">
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
      tabs: [{ name: "Facts" }, { name: "Options" }],
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
