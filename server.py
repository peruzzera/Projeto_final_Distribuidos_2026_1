import socket
import sys

host_address = "127.0.0.1"
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
    sock = socket_start()

def socket_start() -> socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind((host_address, port))
        return sock
    except OSError as exc:
        print(
            f"[SERVER] Não foi possível usar {host_address}:{port} ({exc}).",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
    
def listen():
    global sock
    sock.listen(5)

    print(f"[SERVER] Escutando em {host_address}:{port}", flush=True)
    print(
        "[SERVER] Aguardando cliente (fica parado aqui até um connect) — é normal.",
        flush=True,
    )
    print("[SERVER] Ctrl+C encerra o processo inteiro.\n", flush=True)

    try:
        while True:
            conn, endereco = sock.accept()
            print(f"[SERVER] Cliente conectado: {endereco}")

            try:
                while True:
                    data = conn.recv(4096)
                    print("conferiu dados")
                    if not data:
                        print("nao recebeu dados")
                        print("[SERVER] Cliente fechou a conexão.")
                        break

                    texto = data.decode("utf-8", errors="replace").strip()

                    if exit_request(texto):
                        conn.sendall(b"OK: sessao encerrada no servidor.\n")
                        print("[SERVER] Encerramento pedido pelo cliente.")
                        break

                    resposta = f"DEMO_TCP_OK: recebi sua linha ({len(texto)} caracteres)\n"
                    conn.sendall(resposta.encode("utf-8"))
            finally:
                conn.close()
                print("[SERVER] Socket deste cliente fechado.\n")

    except KeyboardInterrupt:
        print("\n[SERVER] Encerrado.")
    finally:
        sock.close()

def exit_request(texto: str) -> bool:
    t = texto.strip()
    if t.upper() == "CLOSECONNECTION":
        return True
    if "|" in t:
        _, resto = t.split("|", 1)
        if resto.strip().upper() == "CLOSECONNECTION":
            return True
    return False

if __name__ == "__main__":
    main()
