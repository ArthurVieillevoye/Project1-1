export default {
  getRules: (state) => state.rules,
  getArgs: (state) => state.args,
  getClosure: (state) => state.closure,
  getStable: (state) => state.stable,
  getGrounded: (state) => state.grounded,
  getFacts: (state) => state.facts,
  getQuestions: (state) => state.questions,
  getExamples: (state) => state.examples,
  getExamplesTwo: (state) => state.examplesTwo,
  getSelectedTab: (state) => state.selectedTab,
  getGEFilter: (state) => state.groundedExtensionFilter,
  getUndercutting: (state) => state.undercuttingArgs,
};
