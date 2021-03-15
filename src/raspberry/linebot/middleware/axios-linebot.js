import axios from 'axios'
import line from '@line/bot-sdk'

const PORT = process.env.PORT || 3000;
const config = {
  channelSecret: process.env.CHANNEL_SECRET,
  channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN
};

const client = new line.Client(config);

const instance = axios.create({
  baseURL: 'https://identitytoolkit.googleapis.com/v1',
})

export default instance