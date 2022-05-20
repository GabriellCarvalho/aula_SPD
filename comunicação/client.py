import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.0.103:9050')

print (s.system.listMethods())
s.set_password('joao','123')
s.set_password('pedro','321')
s.set_password('ze','213')
s.set_password('maria','senha123')
s.set_password('ana','admin')
print(s.get_passwords())
s.update_password('admin123', 2)
print(s.get_passwords())

s.save_password()

