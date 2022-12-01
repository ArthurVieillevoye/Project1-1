<template>
  <div class="h-screen w-screen flex flex-col">
    <div class="flex flex-row h-full w-full absolute">
      <div class="w-2/3 bg-blue-800"></div>
      <div class="w-1/3"></div>
    </div>

    <Navigation />

    <!-- <wrapper> -->
    <Nuxt />
    <!-- </wrapper> -->
  </div>
</template>
<script>
export default { name: "MainLayout" };
</script>

<style></style>
