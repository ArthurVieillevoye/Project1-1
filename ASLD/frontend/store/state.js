export const InitialState = () => {
  return {
    rules: [],
    facts: [],
    args: [],
    closure: [],
    stable: [],
    grounded: [],
    questions: [],
    examples: [],
    selectedTab: "Facts",
    examplesTwo: [],
    groundedExtensionFilter: [],
    undercuttingArgs: [],
  };
};

const state = InitialState();
export default state;
