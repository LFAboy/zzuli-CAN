# socket 库 这里的作用是动态的获取本机ip
import socket
# 引入 requests 请求库
import requests
import time

import wifi
# 寻找 zzuli-student 网络，并连接（相当于我们点击连接，接下来会跳转认证这一步）
wifi.wifi_connect()
time.sleep(1)

# 获取本机在局域网中的动态IP
def get_ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('8.8.8.8', 80))
  ip = s.getsockname()[0]
  s.close()
  return ip
ip = get_ip()

# 校园网登录页的 url  和f12 network 中的 http请求 url 一致，把URL中的本机IP参数替换一下
post_url = 'http://10.168.6.10:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.168.6.10&iTermType=1&wlanuserip={0}&wlanacip=10.168.6.9&mac=00-00-00-00-00-00&ip={0}&enAdvert=0&queryACIP=0&loginMethod=1'.format(ip)


# http post请求的 参数
post_data = {
  "DDDDD": ',0,54xxxxxxxx@unicom', # 校园网账号，前面的 0 表示设置类型， 54xxxxxxx是你的学号 @ 后面的是运营商，DDDDD这个参数可以在http请求报文中的 payload 中找到，替换成自己的即可
  "upass": 'xxxxxx', # 校园网的登录密码
  "R1": "0",
  "R2": "0",
  "R3": "0",
  "R6": "0",
  "para": "00",
  "OMKKey": "123456",
}

# 注意 header 字段中的数据，也替换成自己的 http post 请求的 header 字段
header = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "Cache-Control": "max-age=0",
  "Connection": "keep-alive",
  "Content-Type": "application/x-www-form-urlencoded",
  "Host": "10.168.6.10:801",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# 开始网络认证（相当于我们输入校园网的账号和密码点击认证这一步）
response = requests.post(post_url, data=post_data, headers=header)
# response = requests("POST", url, data, header=header)
# POST 方式向 URL 发送表单，同时获取状态码
print("状态码{}".format(response))  # 打印状态码

print(post_url)