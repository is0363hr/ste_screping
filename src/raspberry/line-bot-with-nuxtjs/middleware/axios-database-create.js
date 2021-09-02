import axios from 'axios'

const instance = axios.create({
  baseURL: `${process.env.LOCAL_URL}/api`,
})

export default instance