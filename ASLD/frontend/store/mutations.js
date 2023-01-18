import { InitialState } from "./state";

export default {
  SET_RULES(state, payload) {
    state.rules = payload;
  },

  SET_FACTS(state, payload) {
    state.facts = payload;
  },

  SET_ARGS(state, payload) {
    state.args = payload;
  },
  SET_CLOSURE(state, payload) {
    state.closure = payload;
  },
  SET_STABLE(state, payload) {
    state.stable = payload;
  },
  SET_GROUNDED(state, payload) {
    state.grounded = payload;
  },

  SET_QUESTIONS(state, payload) {
    state.questions = payload;
  },

  SET_EXAMPLES(state, payload) {
    state.examples = payload;
  },
  SET_EXAMPLES_TWO(state, payload) {
    state.examplesTwo = payload;
  },
  SET_SELECTED_TAB(state, payload) {
    state.selectedTab = payload;
  },

  RESET_STATE(state) {
    Object.assign(state, InitialState());
  },
};
