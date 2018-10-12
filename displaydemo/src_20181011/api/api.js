import axios from 'axios';

// let host = 'http://127.0.0.1:8000';
let host = 'http://128.5.9.20:8015';

export const getPersonList = params => {
    return axios.get(`${host}/getPersonList`, params)
}

export const getDepartmentList = params => {
    return axios.get(`${host}/duty/departmentlist`, params)
}
/**
 *  根据传入的选中时间以及did获取值班人员信息表
 *
 * @param {*} params selected_date,did
 * @returns promise
 */
export const getUserListByDepartment = params => {

    return axios.get(`${host}/duty/schdeulelistshow`, {
        params: params
    })
}

/**
 *  获取左侧的固定显示两个领导信息
 *
 * @param {*} params
 */
export const getStaticUser=params=>{
    return axios.get(`${host}/duty/schdeulestaticlistshow`, {
        params: params
    })
}

// export const getUserImg=paramas=>{
//     return 
// }

/**
 * 根据显示等级的key返回对应的value
 *
 * @param {*} params index level字典的key（1-4）
 * @returns
 */
export const getLevel = params => {
    const dict_level = {
        1: 'urgency', //中心领导
        2: 'minor', //业务处领导
        3: 'import', //室领导
        4: 'norm' //值班员
    }
    var value_level = 'norm'
    if (dict_level.hasOwnProperty(params)) {
        value_level = dict_level[params]
    }
    return value_level;
}