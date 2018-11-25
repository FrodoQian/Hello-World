"""
下载百度图片页面上的所有图片
"""
"""
登录12306网站
"""
import requests
#cookie处理requests.session 自动的处理
session = requests.Session( )
#伪装成浏览器
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36'
train_png_url = 'https://kyfw.12306.cn/otn/resources/login.html'
session.post(train_png_url)

