import axios from '~/middleware/axios-auth'

// export const namespaced = true

export const state = () => ({
  idToken: null,
})

export const mutations = {
  updateIdToken(state, idToken) {
    state.idToken = idToken
  },
}

export const actions = {
  signIn({ commit }, authData) {
    axios
      .post(
        `/accounts:signInWithPassword?key=${process.env.FIRE_AUTH_API_KEY}`,
        {
          password: authData.password,
          email: authData.email,
          returnSecureToken: true,
        }
      )
      .then((response) => {
        commit('updateIdToken', response.data.idToken)
        console.log(response)
      })
  },
  signOut({ commit }) {
    commit('updateIdToken', null)
  },
}

export const getters = {
  idToken(state) {
    return state.idToken
  },
}
