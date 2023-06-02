
import axios from 'axios'
// import VueAxios from 'vue-axios'
var back = "http://154.8.183.51/";



function getBookDetiles(bookid) {
  var token = localStorage.getItem("token")
  var axios = require('axios');

  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/info/' + bookid,
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  };
  return axios(config)
    .then(function (response) {
      // console.log(JSON.stringify(response.data));
      return response.data;
    })
    .catch(function () {
      // alert("书籍信息不存在！")
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
    .catch(function (error) {
      return error;
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
  if ('sub' in options) {
    options['category'] = options['sub']
  }
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

function submitBookComment(bookid, chapter, comment) {
  var token = localStorage.getItem("token")
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  return axios({
    method: 'post',
    url: 'http://154.8.183.51/book/comments/' + bookid + '/' + chapter,
    data: { "text": comment },
  }).catch(function (data) {
    return data;
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
  return axios({
    method: 'delete',
    url: 'http://154.8.183.51/book/mark/' + bookid + '/' + chapter,
  }).catch(function (data) {
    return data;
  });
}

function addBookToFavor(bookid) {
  var token = localStorage.getItem("token")
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  return axios({
    method: 'put',
    url: 'http://154.8.183.51/book/favor/' + bookid
  }).catch(function (data) {
    return data;
  });
}
function addColection(bookid) {
  var axios = require('axios');
  var token = localStorage.getItem("token")
  var config = {
    method: 'put',
    url: 'http://154.8.183.51/book/favor/' + bookid,
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  };
  // console.log(config);

  return axios(config)
    .then(function () {
      // console.log(JSON.stringify(response.data));
      return true;
    })
    .catch(function (error) {
      console.log(error);
    });
}


function submitRating(bookid, rate) {
  // var token = localStorage.getItem("token")
  var axios = require('axios');

  var config = {
    method: 'post',
    url: `http://154.8.183.51/book/score/${bookid}/${rate}`,
    headers: {
      // 'Authorization':`Bearer ${token}`, 
      // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)', 
      'Content-Type': 'application/json'
    }
  };

  return axios(config)
    .then(function (response) {
      console.log(JSON.stringify(response.data));
      return true;
    })
    .catch(function (error) {
      console.log(error);
    });
}
function getMyRating(bookid) {
  var axios = require('axios');
  var token = localStorage.getItem("token");
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/score/' + bookid,

    headers: {
      // 'Authorization': 'Bearer {{ACCESS_TOKEN}}',

      'Content-Type': 'application/json'
    }
  };

  return axios(config)
    // .then(function (response) {
    //   // console.log(JSON.stringify(response.data));
    //   return response;
    // })
    .catch(function (response) {
      return response;
    });
}
function getSearchBookIds(keywords, page) {
  var token = localStorage.getItem("token")
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  return axios({
    method: 'get',
    url: `http://154.8.183.51/book/search/?keyword=${keywords}&page=${page}`,
  }).catch(function (data) {
    return data;
  });
}
function deleteColection(bookid) {
  var axios = require('axios');
  var token = localStorage.getItem("token")
  var config = {
    method: 'delete',
    url: `http://154.8.183.51/book/favor/${bookid}`,
    headers: {
      'Authorization': `Bearer ${token}`,
      // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Content-Type': 'application/json'
    }
  }
  return axios(config)
    .then(function () {
      return true;
    })
    .catch(function (error) {
      console.log(error);
    });
}
function getRecent() {
  var axios = require('axios');
  var token = localStorage.getItem("token")
  var config = {
    method: 'get',
    url: 'http://154.8.183.51/book/recent',
    headers: {
      'Authorization': `Bearer ${token}`,
      // 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Content-Type': 'application/json'
    }
  };

  return axios(config)
    .catch(function (response) {
      return response;
    });
}

function getAuthor(author) {
  return axios({
    method: 'get',
    url: 'http://154.8.183.51/book/author/' + author,
  }).catch(function (data) {
    return data;
  });
}

function getNotes(bookid, chapter, page) {
  return axios({
    method: 'get',
    url: `http://154.8.183.51/book/notes/${bookid}/${chapter}/${page}`,
  }).catch(function (data) {
    return data;
  });
}

function submitNote(bookid, chapter, note) {
  return axios({
    method: 'post',
    url: `http://154.8.183.51/book/notes/${bookid}/${chapter}`,
    data: { "text": note },
  }).catch(function (data) {
    return data;
  });
}
function getBriefInfo() {
  var token = localStorage.getItem("token")
  return axios({
    method: 'get',
    url: `http://154.8.183.51/book/briefinfo`,
    headers: {
      'Authorization': `Bearer ${token}`,
    }
  }).catch(function (data) {
    return data;
  });

}

export {
  getBookDetiles,
  getBookContent,
  getBookList,
  getBookCharpter,
  getBookComments,
  addBookmark,
  getMyBook,
  deletBookmark, addColection,
  submitBookComment,
  addBookToFavor,
  getSearchBookIds,
  deleteColection, submitRating, getMyRating, getRecent,
  getAuthor,
  getNotes, submitNote,
  getBriefInfo
}
// 使用示例

