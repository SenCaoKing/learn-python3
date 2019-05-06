import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
# $ nslookup www.python.org
# Server:		192.168.19.4
# Address:	192.168.19.4#53

# Non-authoritative answer:
# www.python.org	canonical name = python.map.fastly.net.
# Name:	python.map.fastly.net
# Address: 199.27.79.223

# Exit code: 0

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
# $ nslookup
# Server:		192.168.19.4
# Address:	192.168.19.4#53

# Non-authoritative answer:
# python.org	mail exchanger = 50 mail.python.org.

# Authoritative answers can be found from:
# mail.python.org	internet address = 82.94.164.166
# mail.python.org	has AAAA address 2001:888:2000:d::a6


# Exit code: 0