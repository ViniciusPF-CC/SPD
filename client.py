import Pyro4

def main():
    # Localize o objeto Pyro4 remoto do servidor com o nome 'server'
    uri = Pyro4.locateNS().lookup('server')
    server = Pyro4.Proxy(uri)

    # Envie uma mensagem para o servidor
    message = input("Digite uma mensagem para enviar ao servidor: ")
    server.receive_message(message)

if __name__ == '__main__':
    main()