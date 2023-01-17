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

  RESET_STATE(state) {
    Object.assign(state, InitialState());
  },
};
