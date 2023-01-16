<template>
  <div
    class="h-full w-2/3 bg-gray-200/80 backdrop-blur-md rounded flex flex-col"
  >
    <div class="flex justify-between p-3">
      <span class="font-semibold text-xl tracking-wide">
        Argumentation Tableau
      </span>
      <MainButton
        dynamicClass="shadow bg-blue-500 rounded text-white hover:bg-blue-400"
        icon="mdi-plus"
        width="w-18"
        @click="fetchArgs"
      />
    </div>
    <div class="p-3 h-full w-full overflow-auto">
      <div
        v-if="args.length !== 0"
        class="bg-gray-100 rounded h-full w-full overflow-auto"
      >
        {{ args }}
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "TableauCard",

  computed: {
    ...mapGetters({ args: "getArgs" }),
  },

  methods: {
    fetchArgs() {
      this.$store.dispatch("fetchArgs");
    },
  },
};
</script>

<style></style>
