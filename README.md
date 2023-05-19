# BUAA-SE-23-PleasantReading

## 前后端交互规范

### 要求

* 要求全部数据采用 `json` 格式传输
* 要求登录等操作使用 `token` 检查

### 具体方法

前端登录认证需要修改的地方：

- `main.js`

  ```js
  import axios from 'axios'
  axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.getItem('token')}`;
  ```

- `LoginComponent.vue`

  ```js
  import axios from 'axios'
  ```

  ```js
  async function usreList() {
      try {
        axios.post('http://127.0.0.1:8888/login/', {
          id: userLoginForm.username,
          pwd: userLoginForm.password
        }, {
        headers: {
          'Content-Type': 'application/json'  // 设置请求头为 JSON 格式
        }
      }).then(response => {
          const token = response.data.access;
          // 将令牌存储在本地存储中
          localStorage.setItem('token', token);
          console.log(token);
          console.log(response.data.message);
          // 更新默认请求头中的令牌
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          // 登录成功后的操作，例如跳转到其他页面
      }).catch(error => {
        // 处理登录错误
        console.error(error);
      });
      } catch (error) {
        // 处理错误
        console.error(error);
      }
    }
  ```

- 对于需要登录认证即需要 `token` 的请求，e.g.：

  ```js
  async function func_name() {
                  axios.post('http://127.0.0.1:8888/xxx/', {}, {
                      headers: {
                          'Content-Type': 'application/json',
                          'Authorization': `Bearer ${localStorage.getItem('token')}` //传 token
                      }
                  }).then(response => {
                      console.log(response);
                  }).catch(error => {
                      console.error(error);
                  });
  }
  ```

- 对于不需要登录认证的请求，以登录为例（跟上一份代码的主要区别在于`headers`里面没有`Authorization`），另外登录需要获取`token`：

  ```js
    async function usreList() {
      try {
        axios.post('http://127.0.0.1:8888/login/', {
          id: userLoginForm.username,
          pwd: userLoginForm.password
        }, {
        headers: {
          'Content-Type': 'application/json'  // 设置请求头为 JSON 格式！！！
        }
      }).then(response => {
          const token = response.data.access;
          // 将令牌存储在本地存储中
          localStorage.setItem('token', token);
          console.log(token);
          console.log(response.data.message);
          // 更新默认请求头中的令牌
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          // 登录成功后的操作，例如跳转到其他页面
      }).catch(error => {
        // 处理登录错误
        console.error(error);
      });
      } catch (error) {
        // 处理错误
        console.error(error);
      }
    }
  ```

  