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

  SET_QUESTIONS(state, payload) {
    state.questions = payload;
  },

  RESET_STATE(state) {
    Object.assign(state, InitialState());
  },
};
