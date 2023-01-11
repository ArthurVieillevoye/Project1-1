<template>
  <div class="flex h-full space-x-4">
    <TableauCard />
    <side-bar>
      <template #body>
        <FactsCard />
      </template>
    </side-bar>
  </div>
</template>

<script>
import SideBar from "../components/Shared/SideBar.vue";
export default {
  components: { SideBar },
  name: "IndexPage",

  mounted() {
    // this.$axios.get("http://localhost:8000/api/hello");
    this.$store.dispatch("fetchQuestions");
  },
};
</script>
