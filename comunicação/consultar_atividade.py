import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://172.19.7.4:9053')

print(s.getTarefa())