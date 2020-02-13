

## 直播课程实战步骤参考

部署 Flask 框架
https://github.com/serverless-components/tencent-flask
注意：该框架需要在本地安装Python环境，并且保持pip可用。

基于 Flask 模板，为页面增加情人节Demo

## 下载目录和教程文档：
https://github.com/canmengfly/Serverless-2.13demo

## 具体改动说明：

在使用之前，需要先初始化一个 Flask 项目，然后将 Flask 和 werkzeug 添加到依赖文件 requirements.txt 中，如下：
```bash
Flask==1.0.2
werkzeug==0.16.0
```

## 同时新增服务 app.py，在 app.py 中返回需要的页面：
```bash
from flask import Flask, abort, render_template  //引入 render_template

app = Flask(__name__,  static_folder='static')

@app.route('/') //首页路由
def index():
    return render_template('index.html')

@app.route('/love') //生成页路由
def love():
    return render_template('love.html')

if __name__ == '__main__':
    app.run()
```

## 相关修改参加 Github 代码，最后运行 sls --debug 即可

Demo预览地址： https://service-lidgnqo9-1251746107.sh.apigw.tencentcs.com/release/
