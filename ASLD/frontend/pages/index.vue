<template>
  <span>Hello World</span>
</template>

<script>
export default {
  name: "IndexPage",

  mounted() {
    this.$axios.get("http://localhost:8000/api/hello");
  },
};
</script>
