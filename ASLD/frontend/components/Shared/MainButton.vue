<template>
  <button
    class="py-1 px-2 drop-shadow-md font-light tracking-wide uppercase"
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
      const payload = event;
      this.$emit("click", payload);
    },
  },
};
</script>

<style></style>
