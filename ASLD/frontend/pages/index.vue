<template>
  <div class="flex flex-row space-x-4 w-full">
    <div class="flex flex-col space-y-4 w-full h-full">
      <div
        class="flex flex-col w-full h-1/3 bg-gray-200/40 backdrop-blur-md rounded"
      >
        <div class="flex space-x-4 py-2 justify-center h-12">
          <span
            v-for="tab in tabs"
            :key="tab.name"
            class="hover:border-b border-green-400"
            @click="selectTab(tab)"
            :class="
              tab.tab === currentTab
                ? 'border-green-400  border-b-4 drop-shadow-md'
                : ''
            "
          >
            {{ tab.name }}
          </span>
        </div>
        <ArgumentsCard v-if="currentTab === 'all'" />
        <ClosureCard v-if="currentTab === 'closure'" />
        <UndercuttingCard v-if="currentTab === 'undercutting'" />
      </div>

      <div
        class="flex flex-col w-full h-2/3 bg-gray-200/40 backdrop-blur-md rounded rounded"
      >
        <div class="flex space-x-4 py-2 justify-center h-12">
          <span
            v-for="tab in windows"
            :key="tab.name"
            class="hover:border-b border-green-400"
            @click="chooseWindow(tab)"
            :class="
              tab.tab === currentWindow
                ? 'border-green-400  border-b-4 drop-shadow-md'
                : ''
            "
          >
            {{ tab.name }}
          </span>
        </div>
        <ExtensionsCard v-if="currentWindow === 'extensions'" />
        <StableFilterCard v-if="currentWindow === 'filtered'" />
        <GroundedTreeCard v-if="currentWindow === 'tree'" />
      </div>
    </div>

    <SideBar />
  </div>
</template>

<script>
import ClosureCard from "../components/Cards/ClosureCard.vue";
import CardLayout from "../components/Shared/CardLayout.vue";
export default {
  components: { CardLayout, ClosureCard },
  name: "IndexPage",

  data() {
    return {
      tabs: [
        { name: "All Arguments", tab: "all" },
        { name: "Closure Arguments", tab: "closure" },
        { name: "Undercutting Arguments", tab: "undercutting" },
      ],
      currentTab: "all",
      windows: [
        { name: "Conclusion", tab: "tree" },
        { name: "Extensions", tab: "extensions" },
        { name: "Final Stable Arguments", tab: "filtered" },
      ],
      currentWindow: "tree",
    };
  },

  methods: {
    selectTab(selected) {
      this.currentTab = selected.tab;
    },
    chooseWindow(selected) {
      this.currentWindow = selected.tab;
    },
  },

  mounted() {},
};
</script>
