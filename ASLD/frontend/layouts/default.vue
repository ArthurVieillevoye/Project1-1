<template>
  <div
    class="h-screen w-screen flex flex-col bg-gradient-to-r from-blue-900 to-blue-400"
  >
    <!-- <div class="flex flex-row h-full w-full absolute -z-10">
      <div class="w-2/3 bg-blue-800"></div>
      <div class="w-1/3"></div>
    </div> -->

    <Navigation />

    <div class="p-4 flex flex-row basis-full overflow-auto">
      <Nuxt />
    </div>
  </div>
</template>
<script>
export default { name: "MainLayout" };
</script>

<style></style>
