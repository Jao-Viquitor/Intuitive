import axios from 'axios'

const api = axios.create({
    baseURL: 'https://intuitive-backend.onrender.com/api',
})


export default api
