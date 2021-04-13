// export const namespaced = true
import axios from '~/middleware/axios-weather-create'
// import fs from 'fs'
// import axios from 'axios'

export const state = () => ({
  imgYear: new Date().getFullYear(),
  imgMonth: new Date().getMonth()+1,
  imgDay: new Date().getDate(),
  imgHour: new Date().getHours(),
  imgMinute: Math.floor(new Date().getMinutes() / 5)*5,
  zoom: 4,
  lon: 135.000,
  lat: 34.000,
  imgPath: null,
  imgData: null,
})

export const mutations = {
  updateDateTime(state, dateTime) {
    state.imgYear = dateTime.imgYear,
    state.imgMonth = dateTime.imgMonth,
    state.imgDay = dateTime.imgDay,
    state.imgHour = dateTime.imgHour,
    state.imgMinute = dateTime.imgMinute
  },
  updateZoom(state, zoom) {
    state.zoom = zoom
  },
  updateCenterCoordinate(state, centerCoordinate) {
    state.lon = centerCoordinate.lon,
    state.lat = centerCoordinate.lat
  },
  updateImagePath(state, imgPath) {
    state.imgPath = imgPath
  },
  updateImageData(state, imgData) {
    state.imgData = imgData
  },
}

export const actions = {
  weatherImg({ commit, state }, requestData) {
    // commit('updateDateTime', requestData),
    axios
      .get(
        `/weather`,
        {
          params: {
            imgYear: requestData.imgYear,
            imgMonth: requestData.imgMonth,
            imgDay: requestData.imgDay,
            imgHour: requestData.imgHour,
            imgMinute: requestData.imgMinute,
            lon: requestData.lon,
            lat: requestData.lat,
            zoom: state.zoom,
          }
        })
      .then((response) => {
        commit('updateImageData', response.data)
        console.log(response)
      })
  },
}

export const getters = {
  zoom(state) {
    return state.zoom
  },
  dateTime(state) {
    return [state.imgYear, state.imgMonth, state.imgDay, state.imgHour, state.imgMinute]
  },
  centerCoordinate(state) {
    return [state.lon, state.lat]
  },
  imgPath(state) {
    return state.imgPath
  },
  imgData(state) {
    return state.imgData
  },
}
