from person import Person
import Pyro4


#uri = input("Entre o uri do armazem: ")
warehouse = Pyro4.Proxy('PYRO:example.warehouse@192.168.137.94:9090')
#warehouse = Pyro4.Proxy("PYRONAME:example.warehouse")

janet = Person("Janet")
henry = Person("Henry")

janet.visit(warehouse)
henry.visit(warehouse)
