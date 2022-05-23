import xmlrpc.client


def main():
    try:
        s = xmlrpc.client.ServerProxy('http://192.168.0.103:9050')
        passwords = s.get_users_passwords()
        try:
            with open('senhas.txt', 'w') as file:
                for key, value in passwords.items():
                    file.write('user:%s, password:%s\n' % (key, value))
                file.close()
        except FileNotFoundError as erro:
            print("Não foi possivel abrir o arquivo, Erro: ", erro)

    except:
        print("Não foi possível conectar ao servidor...")

if __name__ == '__main__':
    main()
