<template>
  <div class="flex h-full space-x-4">
    <TableauCard />
    <side-bar>
      <template #header>
        <div
          class="w-full flex space-x-4 p-3 justify-center bg-white/80 rounded backdrop-blur-md"
        >
          <span
            v-for="tab in tabs"
            :key="tab.name"
            class="hover:border-b"
            @click="selectTab(tab.name)"
          >
            {{ tab.name }}
          </span>
        </div>
      </template>
      <template #body>
        <FactsCard v-if="tab == 'Facts'" />
        <QuestionsCard v-if="tab == 'Questions'" />
      </template>
    </side-bar>
  </div>
</template>

<script>
import SideBar from "../components/Shared/SideBar.vue";
export default {
  components: { SideBar },
  name: "IndexPage",

  data() {
    return {
      tabs: [{ name: "Facts" }, { name: "Questions" }],
      tab: "",
    };
  },

  methods: {
    selectTab(selected) {
      this.tab = selected;
    },
  },

  mounted() {
    // this.$axios.get("http://localhost:8000/api/hello");
  },
};
</script>
