from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("192.168.0.103", 9050), allow_none=True)
users = []
passwords = []

def set_password(user, password):
    users.append(user)
    passwords.append(password)

def get_passwords():
    return passwords

def update_password(password, pos):
    del(passwords[pos])
    passwords.insert(pos, password)
    save_password()

def get_users_passwords():
    users_passwords = dict(zip(users, passwords))
    return users_passwords

def save_password():
    user_password = dict(zip(users, passwords))
    try:
        with open('arquivo.txt', 'w') as file:
            for key,value in user_password.items():
                file.write('user:%s, password:%s\n'%(key,value))
            file.close()
    except FileNotFoundError as erro:
        print("Erro: ", erro)

server.register_function(set_password)
server.register_function(get_passwords)
server.register_function(update_password)
server.register_function(get_users_passwords)
server.register_function(save_password)

server.register_introspection_functions()
server.serve_forever()