<template>
  <div class="bg-white/80 backdrop-blur-md rounded flex flex-col p-3">
    <div class="flex justify-between">
      <span class="font-semibold text-xl tracking-wide"> Facts </span>
      <MainButton
        dynamicClass="shadow bg-blue-500 rounded text-white hover:bg-blue-400"
        icon="mdi-plus"
        width="w-18"
        @click="fetchArgs"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "FactsCard",

  methods: {
    fetchArgs() {
      this.$store.dispatch("fetchArgs");
    },
  },
};
</script>

<style></style>
