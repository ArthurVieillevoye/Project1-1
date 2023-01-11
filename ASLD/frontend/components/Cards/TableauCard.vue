<template>
  <div class="h-full w-2/3 bg-white/80 backdrop-blur-md rounded flex flex-col">
    <div class="flex justify-between p-3">
      <span class="font-semibold text-xl tracking-wide">
        Argumentation Tableau
      </span>
    </div>
    <div class="w-full h-full p-3">
      <div v-if="args.length !== 0" class="h-full bg-gray-100 rounded">
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
};
</script>

<style></style>
