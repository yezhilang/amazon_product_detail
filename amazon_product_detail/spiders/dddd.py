# encoding:utf-8
import qrcode
img = qrcode.make("https://www.sogou.com/tx?ie=utf-8&hdq=sogou-clse-60a70bb05b08d6cd&query=IOError%3A%20%5BErrno%2013%5D%20Permission%20denied%3A")
img.save("h.png")


