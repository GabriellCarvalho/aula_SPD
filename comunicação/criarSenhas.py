import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.0.103:9050')

s.set_password('jose', '123')
s.set_password('paulo', '321')
s.set_password('ana', '456')
s.set_password('maria', '654')

s.save_password()

