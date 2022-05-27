class Person(object):
    
    def __init__(self, name):
        self.name = name
    
    def visit(self, warehouse):
        print("Aqui eh ", self.name)
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Obrigado e volte sempre! ")
    
    def deposit(self, warehouse):
        print("O armazem contem: ", warehouse.list_contents())
        item = input("Entre com um item a ser armazenado (ou deixe em branco)" )
        if item:
            warehouse.store(self.name, item)
    
    def retrieve(self, warehouse):
        print("O armazem contem: ", warehouse.list_contents())
        item = input("Qual item deseja retirar (ou deixe em branco): ")
        if item:
            warehouse.take(self.name, item)

    