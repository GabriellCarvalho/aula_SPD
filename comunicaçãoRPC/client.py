import xmlrpc.client
from tkinter import messagebox

try:
    s = xmlrpc.client.ServerProxy('http://10.155.2.32:9053')
    passwords = s.get_users_passwords()
    try:
        with open('senhas.txt', 'w') as file:
            file.write(passwords)
        file.close()
        messagebox.showinfo('Senha', "Senhas salvas")
    except FileNotFoundError as erro:
        print("Não foi possivel abrir o arquivo, Erro: ", erro)    
except:
    messagebox.showerror('Erro', "Não foi possível conectar ao servidor...")
