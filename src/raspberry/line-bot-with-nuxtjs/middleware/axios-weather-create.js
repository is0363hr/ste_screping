import axios from 'axios'

const instance = axios.create({
  baseURL: `${process.env.LOCAL_URL}/api`,
  // baseURL: `${process.env.BASE_LOCAL_TEST_URL}/api`,
})

export default instance
