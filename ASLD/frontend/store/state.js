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
  };
};

const state = InitialState();
export default state;
