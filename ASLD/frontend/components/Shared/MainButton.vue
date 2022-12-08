<template>
  <button
    class="p-2 drop-shadow-md font-semibold uppercase"
    :class="[
      width,
      dynamicClass,
      isDisabled ? 'cursor-not-allowed opacity-30' : '',
    ]"
    :disabled="isDisabled"
    @click="actionHandler"
  >
    {{ placeholder }}
    <i class="mdi" :class="icon" />
  </button>
</template>

<script>
export default {
  name: "MainButton",

  props: {
    placeholder: {
      default: "Fact",
      type: String,
    },
    handler: {
      type: String,
      default: "",
    },

    width: {
      default: "w-1/2",
      type: String,
    },

    icon: {
      default: "mdi-arrow-right",
      type: String,
    },
    isDisabled: {
      default: false,
      type: Boolean,
    },
    dynamicClass: {
      default: "",
      type: String,
    },
  },

  methods: {
    actionHandler(event) {
      if (!this.handler) return;

      const payload = event;
      this.$emit(this.handler, payload);
    },
  },
};
</script>

<style></style>
