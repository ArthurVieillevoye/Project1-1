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

  RESET_STATE(state) {
    Object.assign(state, InitialState());
  },
};
