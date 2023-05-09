import Pyro4

@Pyro4.expose
class Server(object):
    def receive_message(self, message):
        print("Mensagem recebida: ", message)

def main():
    # Inicialize o daemon do Pyro4
    daemon = Pyro4.Daemon()

    # Registre o objeto Pyro4 com o nome 'server'
    server = Server()
    uri = daemon.register(server)
    ns = Pyro4.locateNS()
    ns.register('server', uri)

    # Aguarde conexões de clientes
    print("Servidor aguardando conexões...")
    daemon.requestLoop()

if __name__ == '__main__':
    main()