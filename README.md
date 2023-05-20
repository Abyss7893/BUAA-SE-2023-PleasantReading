# BUAA-SE-2023-PleasantReading

此仓库为 `BUAA` 软工大作业仓库。

除去默认分支 `main` 外新增三个分支：

* `front` : 负责放置前端代码
* `back` ：负责放置后端代码
* `documents` ：负责放置相关文件以及配图

各人员在上传时 **仅允许** 对以上三个分支进行修改提交 `commit` ，不允许直接对 `main` 分支进行修改！在对应分支提交后发起 `merge` 请求后由组长统一审核，通过后同步至 `main` 分支。

每个分支内的 `README.md` 文件可自由发挥。


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

## 后端运行方法

`back`分支下的结构：

```
─BUAA-SE-2023-PleasantReading
│  └─PleasantReading
│      ├─.idea
│      │  ├─dataSources
│      │  └─inspectionProfiles
│      ├─api
│      │  ├─migrations
│      │  │  └─__pycache__
│      │  ├─templates
│      │  └─__pycache__
│      ├─media
│      │  └─UserImg
│      ├─PleasantReading
│      │  └─__pycache__
│      └─__pycache__
└─config.ini
```

我们对于django的各种操作和运行都是基于`manage.py`的，配置文件则位于`PleasantReading/settings.py`

需要注意的是，为了对数据库密码和邮箱密码进行保护，我们将这些信息装到了`config.ini`，注意其目录位置是在所有文件夹的外面，具体文件内容通过微信私发。

需要提前安装的东西：

```
pip install django
pip install django-cors-headers
pip install djangorestframework
pip install djangorestframework-jwt
pip install djangorestframework-simplejwt
```

（这里不一定全，可以根据之后的运行信息额外进行安装）

打开`settings.py`进行修改：第98行开始的部分：

```python
CORS_ALLOWED_ORIGINS = [
    'http://10.193.157.84:8080'
]
# 允许的来源（根据需要进行配置，可以是具体的域名或通配符）
CORS_ORIGIN_WHITELIST = [
    'http://10.193.157.84:8080/'
    # 其他允许的来源
]
```

将以上两个IP地址改成vue运行之后显示的ip地址，例如vue启动之后信息如下：

```
  App running at:
  - Local:   http://localhost:8080/
  - Network: http://10.193.80.44:8080/
```

则将`http://10.193.80.44:8080/`填入。

然后用PyCharm打开`PleasantReading`文件夹，在右上方运行处附近拉出菜单，点击“编辑配置”；左边选择“django服务器”，右边名称填入PleasantReading，规定端口号为8888，下拉菜单选择自己电脑上的、能导入django的python解释器，点击确定即可。

此时点击右上角的运行按钮即可运行。