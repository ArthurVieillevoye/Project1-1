<template>
  <div
    class="flex flex-col w-1/3 h-full bg-gray-200/40 backdrop-blur-md rounded"
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
    <div class="overflow-auto h-full bg-gray-100/40 rounded-t">
      <FactsCard v-if="selectedTab === 'Facts'" />
    </div>
    <MainButton
      dynamicClass="bg-green-400 rounded-b text-white hover:bg-green-600"
      icon="mdi-chevron-triple-right"
      width="w-18"
      placeholder="Submit"
      @click="fetchArgs"
    />
  </div>
</template>

<script>
export default {
  name: "SideBar",

  data() {
    return {
      tabs: [{ name: "Facts" }, { name: "Examples" }],
      selectedTab: "Facts",
    };
  },

  methods: {
    selectTab(selected) {
      this.selectedTab = selected;
    },
    fetchArgs() {
      this.$store.dispatch("fetchData");
    },
  },

  mounted() {
    // this.$axios.get("http://localhost:8000/api/hello");
  },
};
</script>
