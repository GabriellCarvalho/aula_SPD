import xmlrpc.client
from tkinter import messagebox

try:
    s = xmlrpc.client.ServerProxy('http://192.168.0.103:9050')
    passwords = s.get_users_passwords()
    try:
        with open('senhas.txt', 'w') as file:
            file.write(passwords)
        file.close()
    except FileNotFoundError as erro:
        print("Não foi possivel abrir o arquivo, Erro: ", erro)    
except:
    messagebox.showerror('Erro', "Não foi possível conectar ao servidor...")
