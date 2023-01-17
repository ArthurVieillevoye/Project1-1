<template>
  <div class="bg-gray-200/40 backdrop-blur-md rounded flex flex-col">
    <span class="text-lg tracking-wide p-3"> {{ title }}</span>
    <div class="px-3 pb-3 h-full w-full overflow-auto bg-gray-100/40 rounded">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardLayout",
  props: {
    title: {
      required: true,
      type: String,
      default: "Arguments",
    },
  },

  data() {
    return {};
  },

  computed: {},

  methods: {},
};
</script>

<style></style>
