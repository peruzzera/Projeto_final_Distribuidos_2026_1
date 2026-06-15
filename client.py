import socket
import sys

server_address = "127.0.0.1"
port = 40000

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

catalogo = [
    Produto("coxinha", 6,00),
    Produto("bolinho", 4,00),
    Produto("rocambole", 12,00)
]

def main():
    sock = try_connection()
    connected = True
    listen()

    menu()
    menu_admin()

def try_connection() -> socket:
    #tenta conectar a porta
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_address, port))
        return sock
    except (ConnectionRefusedError,TimeoutError):
        print("couldnt connect to server")
        sys.exit(1)

def listen():
    #escuta o servidor
    global sock
    global connected
    while connected:
        try:    
            data = sock.recv(4096)
            if not data:
                #encerra a escuta se o servidor interrompe a conexao
                not connected
                break

            packet = data.decode('utf-8', errors='replace').strip()
            #necessario decidirmos o que fazer com os pacotes recebidos

        except:
            #essa execao acontece quando o socket do client fecha
            not connected
            break

def menu():
    while connected:
        print("\n\nEscolha a opcao:\n")
        print("[1] fazer um pedido\n")
        print("[2] depositar creditos\n")
        print("[3] historico de pedidos\n")
        print("[0] sair\n")

        op = input()
        match op:
            case "1":
                pedido()

            case "2":

            case "3":

            case "0":
                sock.sendall(b"CLOSECONNECTION")
                sock.close
                not connected
                break

            case __:
                print("opcao invalida")

def pedido():
    carrinho=[]
    while (True):
        for item in catalogo:
            print ("[", catalogo.index(item), "] ", item.nome, "    R$", item.valor)
        print("\nSelecione o item para adicionar ao carrinho, digite [voltar] para cancelar e [finalizar] para prosseguir com o pagamento\n")
        op = input()

        if op=="finalizar":
            pagamento(carrinho)

        if op == "voltar" or op == "finalizar":
            break

        carrinho.append(op)

def pagamento(carrinho):
    for item in carrinho:
        for item in catalogo:
            if carrinho.item == catalogo.index(item):
                carrinho.item = catalogo.item

    sock.sendall("LISTADEITENS")

    for item in carrinho:
        sock.sendall(item.nome)

def deposito():

def menu_admin():

if __name__ == "__main__":
    main()