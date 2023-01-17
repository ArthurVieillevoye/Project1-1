export const InitialState = () => {
  return {
    rules: [],
    facts: [],
    args: [],
    closure: [],
    stable: [],
    grounded: [],
    questions: [],
  };
};

const state = InitialState();
export default state;
