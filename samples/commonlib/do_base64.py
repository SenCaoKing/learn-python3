import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s) # b'5ZyoUHl0aG9u5Lit5L2/55SoQkFTRSA2NOe8lueggQ=='
d = base64.b64decode(s).decode('utf--8')
print(d) # 在Python中使用BASE 64编码

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s) # b'5ZyoUHl0aG9u5Lit5L2_55SoQkFTRSA2NOe8lueggQ=='
d = base64.urlsafe_b64decode(s).decode(('utf-8'))
print(d) # 在Python中使用BASE 64编码
