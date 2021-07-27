import axios from 'axios'

const url = 'http://localhost:5000/api'
const origin = 'http://localhost:3000'
const instance = axios.create({
  baseURL: 'https://comicvine.gamespot.com/api',
})
export default instance
