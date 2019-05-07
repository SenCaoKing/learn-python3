import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in  python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # 5eea39134bbdda26ebcfae1c6a1171f7

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest()) # 2c76b57293ce30acef38d98f6046927161b46a44