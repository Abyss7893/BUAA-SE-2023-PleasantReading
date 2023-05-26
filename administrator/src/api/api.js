import axios from 'axios'
// import VueAxios from 'vue-axios'
var back = "http://154.8.183.51/";

function submitRating(bookid, rate) {
  var token = localStorage.getItem("token")
  var axios = require('axios');

  var config = {
    method: 'post',
    url: `http://154.8.183.51/book/score/${bookid}/${rate}`,
    headers: {
      'Authorization': `Bearer ${token}`,
      // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Content-Type': 'application/json'
    }
  };

  return axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
    })
    .catch(function (error) {
      console.log(error);
    });
}

function getBookDetiles(bookid) {
  var axios = require('axios');

  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/info/' + bookid,
    headers: {
      'Content-Type': 'application/json'
    }
  };
  return axios(config)
    .then(function (response) {
      // console.log(JSON.stringify(response.data));
      return response.data;
    })
    .catch(function (error) {
      console.log(error);
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
  var token = localStorage.getItem("token")
  var axios = require('axios');

  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/content/' + bookid + '/' + chapter,
    headers: {
      'Authorization': `Bearer ${token}`,
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
  var url = back + 'manager/filter?category=' + mergedOptions.category +
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
  console.log(config)
  return axios(config)
    .then(function (response) {
      // console.log(response.data);
      console.log("请求books成功", response.data)
      return response.data;
    })
    .catch(function (error) {
      console.log("fail", error)
      throw error;
    });
}
function getMyBook() {
  var token = localStorage.getItem("token")
  var axios = require('axios');

  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/favor',
    headers: {
      'Authorization': `Bearer ${token}`,
      // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Content-Type': 'application/json',
    }
  };

  return axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
      return response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
}

// 使用示例

function getBookComments(bookid, chapter, page) {
  var axios = require('axios');
  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/comments/' + bookid + '/' + chapter + '/' + page,
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

function addBookmark(bookid, chapter) {
  var token = localStorage.getItem("token")
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  // console.log(axios.defaults.headers.common['Authorization'])
  return axios({
    method: 'post',
    url: 'http://154.8.183.51/book/mark/' + bookid + '/' + chapter,
  }).catch(function (data) {
    return data;
  });
}

function deletBookmark(bookid, chapter) {
  var token = localStorage.getItem("token")
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  // console.log(axios.defaults.headers.common['Authorization'])
  return axios({
    method: 'delete',
    url: 'http://154.8.183.51/book/mark/' + bookid + '/' + chapter,
  }).catch(function (data) {
    return data;
  });
}



export {
  getBookDetiles, getBookContent, getBookList, getBookCharpter, getBookComments, addBookmark, getMyBook, deletBookmark, submitRating
}