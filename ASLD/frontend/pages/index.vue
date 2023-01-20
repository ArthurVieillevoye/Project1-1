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
        <ArgumentsCard v-if="currentTab === 'Arguments'" />
        <ClosureCard v-if="currentTab === 'Closure Arguments'" />
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
        <StableCard v-if="currentWindow === 'Stable Extensions'" />
        <GroundedCard v-if="currentWindow === 'Grounded Extension'" />
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
      tabs: [{ name: "Arguments" }, { name: "Closure Arguments" }],
      currentTab: "Arguments",
      windows: [{ name: "Stable Extensions" }, { name: "Grounded Extension" }],
      currentWindow: "Stable Semantics",
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
