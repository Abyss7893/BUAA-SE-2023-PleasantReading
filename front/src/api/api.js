import axios from 'axios'
// import VueAxios from 'vue-axios'
var back = "http://154.8.183.51/";

function getBookDetiles(bookid) {
    var url = back + "/book/info/" + bookid;
    return axios.get(url).then(res => {
        var data = res.data;
        // data.cover = back + data.cover;
        console.log(data);
        return data;
    });
}
function getBookContent(bookid) {
    var url = back + "/book/outline/" + bookid;
    return axios.get(url).then(res => {
        var data = res.data;
        // console.log(data);
        return data;
    });
}
function getBookCharpter(bookid, chapter) {
    var axios = require('axios');

    var config = {
        method: 'get',
        url: 'http://154.8.183.51/book/content/' + bookid + '/' + chapter,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    return axios(config)
        .then(function (response) {
            // console.log(response.data);
            return response.data;
        })
        .catch(function (error) {
            throw error;
        });
}
function getBookList(options) {
    // 设置默认参数
    var defaultOptions = {
        category: '',
        vip: '',
        range: '',
        order: '',
        status: '',
        page: ''
    };

    // 合并默认参数和传入的参数
    var mergedOptions = { ...defaultOptions, ...options };

    // 构建 URL
    var url = back + '/book/filter/?category=' + mergedOptions.category +
        '&vip=' + mergedOptions.vip +
        '&range=' + mergedOptions.range +
        '&order=' + mergedOptions.order +
        '&status=' + mergedOptions.status +
        '&page=' + mergedOptions.page;

    var config = {
        method: 'get',
        url: url,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    return axios(config)
        .then(function (response) {
            // console.log(response.data);
            return response.data;
        })
        .catch(function (error) {
            throw error;
        });
}

// 使用示例


export {
    getBookDetiles, getBookContent, getBookList, getBookCharpter
}