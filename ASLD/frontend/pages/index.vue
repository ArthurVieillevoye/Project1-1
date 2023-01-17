<template>
  <div class="flex flex-row space-x-4 w-full">
    <div class="grid grid-cols-2 grid-rows-2 gap-4 w-full h-full">
      <ArgumentsCard />
      <ClosureCard />
      <StableCard />
      <GroundedCard />
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
    return {};
  },

  methods: {},

  mounted() {},
};
</script>
