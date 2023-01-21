export default {
  fetchData({ state, commit }) {
    return new Promise((resolve, reject) => {
      const payload = { facts: state.facts, identifier: state.selectedTab };
      this.$axios
        .post("http://localhost:8000/api/main", payload)
        .then((res) => {
          commit("SET_ARGS", res.data.allArgs);
          commit("SET_CLOSURE", res.data.closure);
          commit("SET_STABLE", res.data.stableExtensions);
          commit("SET_GROUNDED", res.data.groundedExtension);
          commit("SET_GE_FILTER", res.data.groundedExtensionFilter);
          commit("SET_UNDERCUTTING", res.data.undercuttingArgs);
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

  fetchToyExamplesTwo({ state, commit }) {
    if (state.examplesTwo.length !== 0) return;

    return new Promise((resolve, reject) => {
      this.$axios
        .get("http://localhost:8000/api/examplestwo")
        .then((res) => {
          commit("SET_EXAMPLES_TWO", res.data.examples);
          resolve(res);
        })
        .catch((error) => {
          reject(error);
        });
    });
  },
};
