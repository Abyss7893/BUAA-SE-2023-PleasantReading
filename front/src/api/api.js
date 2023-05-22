import axios from 'axios'
// import VueAxios from 'vue-axios'
var back = "http://154.8.183.51/";

function getBookDetiles(bookid) {
    var url = back + "/book/info/" + bookid;
    return axios.get(url).then(res => {
        var data = res.data;
        data.cover = back + data.cover;
        console.log(data);
        return data;
    });
}


export {
    getBookDetiles
}