export default {
  fetchData({ commit }) {
    return new Promise((resolve, reject) => {
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

  fetchQuestions({ commit }) {
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
};
