import axios from 'axios';

let host='http://127.0.0.1:8000';

export const getPersonList=params=>{
    return axios.get(`${host}/getPersonList`,params)
}