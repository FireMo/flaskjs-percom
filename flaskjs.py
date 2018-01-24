#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


# url规则和视图函数中，2.注册路由
@app.route('/url')
def reg_url():
    return """
        <ur>
            <li><a href="/test">test</a></li>
            <li><a href="/friend">friend</a></li>
        </ur>    
    """


@app.route('/test')
def test():
    return 'this is response'


@app.route('/friend')
def friend():
    return '<h1>My Friend List</h1>'


# url规则和视图函数中，3.为路由指定HTTP方法
@app.route('/method')
def test_method():
    return """
        <form action="/auth" method="POST">
            <input type="text" name="uid">
            <input type="password" name="pwd">
            <input type="submit" value="submit">
        </form>    
    """


@app.route('/auth', methods=["POST"])
def v_auth():
    return '<h1>在这里做验证工作</h1>'


# url规则和视图函数中,4.匹配动态URL
@app.route('/dynamicurl')
def dynamic_url():
    return """
       <ur>
           <li><a href="/user/Mary/friend/Linda">here</a></li>
       </ur>
    """


@app.route('/user/<uname>/friend/<fname>')
def u_f(uname, fname):
    return '%s\'s friend - %s\' s profile' % (uname, fname)


# app.run(port='5000')
if __name__ == '__main__':
    # app.debug=True
    app.run()
