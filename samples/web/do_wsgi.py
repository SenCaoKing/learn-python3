# 从wsgiref模块导入：
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数：
from hello import application

# 创建一个服务器，IP地址为localhost，端口是8000，处理函数时application
httpd = make_server('localhost', 12345, application)
print('Serving HTTP on port 12345...')
# 开始监听HTTP请求：
httpd.serve_forever()