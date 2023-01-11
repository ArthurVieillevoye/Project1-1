export default {
  fetchArgs({ commit }) {
    return new Promise((resolve, reject) => {
      this.$axios
        .get("http://localhost:8000/api/main")
        .then((res) => {
          commit("SET_ARGS", res.data.closure);
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
