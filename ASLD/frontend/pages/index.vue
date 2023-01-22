<template>
  <div class="flex flex-row space-x-4 w-full">
    <div class="flex flex-col space-y-4 w-full h-full">
      <div
        class="flex flex-col w-full h-1/2 bg-gray-200/40 backdrop-blur-md rounded"
      >
        <div class="flex space-x-4 py-2 justify-center h-12">
          <span
            v-for="tab in tabs"
            :key="tab.name"
            class="hover:border-b border-green-400"
            @click="selectTab(tab.name)"
            :class="
              tab.name === currentTab
                ? 'border-green-400  border-b-4 drop-shadow-md'
                : ''
            "
          >
            {{ tab.name }}
          </span>
        </div>
        <ArgumentsCard v-if="currentTab === 'All Arguments'" />
        <ClosureCard v-if="currentTab === 'Closure Arguments'" />
        <UndercuttingCard v-if="currentTab === 'Undefeated Undercutting Arguments'" />
      </div>

      <div
        class="flex flex-col w-full h-1/2 bg-gray-200/40 backdrop-blur-md rounded rounded"
      >
        <div class="flex space-x-4 py-2 justify-center h-12">
          <span
            v-for="tab in windows"
            :key="tab.name"
            class="hover:border-b border-green-400"
            @click="chooseWindow(tab.name)"
            :class="
              tab.name === currentWindow
                ? 'border-green-400  border-b-4 drop-shadow-md'
                : ''
            "
          >
            {{ tab.name }}
          </span>
        </div>
        <StableCard v-if="currentWindow === 'Stable Extensions (Full)'" />
        <GroundedCard v-if="currentWindow === 'Grounded Extension (Full)'" />
        <StableFilterCard
          v-if="currentWindow === 'Final Arguments (Stable Extensions)'"
        />
        <GroundedTreeCard v-if="currentWindow === 'Final Argument Trees (Grounded Extension)'" />
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
        { name: "All Arguments" },
        { name: "Closure Arguments" },
        { name: "Undefeated Undercutting Arguments" },
      ],
      currentTab: "Arguments",
      windows: [
        { name: "Stable Extensions (Full)" },
        { name: "Grounded Extension (Full)" },
        { name: "Final Arguments (Stable Extensions)" },
        { name: "Final Argument Trees (Grounded Extension)" },
      ],
      currentWindow: "Final Argument Trees (Grounded Extension)",
    };
  },

  methods: {
    selectTab(selected) {
      this.currentTab = selected;
    },
    chooseWindow(selected) {
      this.currentWindow = selected;
    },
  },

  mounted() {},
};
</script>
