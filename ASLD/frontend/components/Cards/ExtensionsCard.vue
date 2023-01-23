<template>
  <card-layout>
    <div v-if="grounded.length !== 0">
      <h3 class="font-bold">Grounded Extension</h3>
      <ul v-for="(ground, index) in grounded" :key="index">
        <li class="py-1">{{ ground }}</li>
      </ul>
    </div>
    <div v-if="grounded.length === 0">
      <div v-if="stable.length !== 0">
        <h3 class="font-bold">Stable Extensions</h3>
        <ul v-for="(stab, index) in stable" :key="index" class="pb-3">
          Extension
          {{
            index + 1
          }}
          <ul v-for="(semantic, index) in stab" :key="index">
            <li class="py-1 pl-2">{{ semantic }}</li>
          </ul>
        </ul>
      </div>
    </div>
  </card-layout>
</template>

<script>
import { mapGetters } from "vuex";
import CardLayout from "../Shared/CardLayout.vue";

export default {
  components: { CardLayout },
  name: "ExtensionsCard",

  data() {
    return {
      parsedArgs: [],
    };
  },

  computed: {
    ...mapGetters({ stable: "getStable", grounded: "getGrounded" }),
  },
};
</script>

<style></style>
