export default {
  fetchData({ dispatch, commit }) {
    return new Promise((resolve, reject) => {
      dispatch("dispatchFacts").then((res) => {
        if (res.statusCode === 404) {
          resolve(res);
        }
      });
      this.$axios
        .get("http://localhost:8000/api/main")
        .then((res) => {
          commit("SET_ARGS", res.data.args);
          commit("SET_CLOSURE", res.data.closure);
          commit("SET_STABLE", res.data.stable);
          commit("SET_GROUNDED", res.data.grounded);
          resolve(res);
        })
        .catch((error) => {
          reject(error);
        });
    });
  },

  fetchQuestions({ state, commit }) {
    if (state.questions.length !== 0) return;

    return new Promise((resolve, reject) => {
      this.$axios
        .get("http://localhost:8000/api/questions")
        .then((res) => {
          commit("SET_QUESTIONS", res.data.questions);
          resolve(res);
        })
        .catch((error) => {
          reject(error);
        });
    });
  },
  fetchToyExamples({ state, commit }) {
    if (state.examples.length !== 0) return;

    return new Promise((resolve, reject) => {
      this.$axios
        .get("http://localhost:8000/api/examples")
        .then((res) => {
          commit("SET_EXAMPLES", res.data.examples);
          resolve(res);
        })
        .catch((error) => {
          reject(error);
        });
    });
  },

  dispatchFacts({ state }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .post("http://localhost:8000/api/facts", {
          facts: state.facts,
        })
        .then((res) => {
          resolve(res);
        })
        .catch((e) => {
          reject(e);
        });
    });
  },
};
