<template>
  <div>
    <OrganizationChart :datasource="ds" />
  </div>
</template>

<script>
import OrganizationChart from "vue-organization-chart";
export default {
  name: "TreeCard",

  components: {
    OrganizationChart,
  },

  data() {
    return {
      ds: {
        id: "1",
        name: "Lao dsfasdfdas",
        title: "ksdakfasdfs ",
        // children: [
        //   { id: "2", name: "Bo Miao", title: "department manager" },
        //   {
        //     id: "3",
        //     name: "Su Miao",
        //     title: "department manager",
        //     children: [
        //       {
        //         id: "4",
        //         name: "Tie Hua",
        //         title: "senior engineer",
        //         relationship: "111",
        //       },
        //       {
        //         id: "5",
        //         name: "Hei Hei",
        //         title: "senior engineer",
        //       },
        //     ],
        //   },
        //   { id: "8", name: "Hong Miao", title: "department manager" },
        //   {
        //     id: "9",
        //     name: "Chun Miao",
        //     title: "department manager",
        //     children: [
        //       { id: "6", name: "Pang Pang", title: "engineer" },
        //       { id: "7", name: "Xiang Xiang", title: "UE engineer" },
        //     ],
        //   },
        // ],
      },
    };
  },
};
</script>

<style></style>
