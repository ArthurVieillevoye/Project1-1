<template>
  <div class="flex h-full space-x-4">
    <TableauCard />
    <FactsCard />
  </div>
</template>

<script>
export default {
  name: "IndexPage",

  mounted() {
    // this.$axios.get("http://localhost:8000/api/hello");
    this.$store.dispatch("fetchQuestions");
  },
};
</script>
