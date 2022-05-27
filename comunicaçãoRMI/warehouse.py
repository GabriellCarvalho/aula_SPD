import Pyro4

@Pyro4.expose
class Warehouse(object):
    
    def __init__(self):
        self.contents = ["cadeira", "bike", "lampada", "laptop", "caneta"]
    
    def list_contents(self):
        return self.contents
    
    def take(self, name, item):
        self.contents.remove(item)
        print(name, " retirou ", item)
    
    def store(self, name, item):
        self.contents.append(item)
        print(name, " armazenou ", item)

def main():
    custom_daemon = Pyro4.Daemon(host="192.168.137.94", port=9090)
    Pyro4.Daemon.serveSimple({ Warehouse: "example.warehouse"}, daemon = custom_daemon, ns=False)

if __name__ == "__main__":
    main()