import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://10.155.2.32:9053')

s.set_password('jose', '123')
s.set_password('paulo', '321')
s.set_password('ana', '456')
s.set_password('maria', '654')

