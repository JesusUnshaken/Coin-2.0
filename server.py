#---------------------------------------------
#=-------------=> 🪙 COIN 2.0 <=-------------=
#---------------------------------------------







import socket
import threading

from colorama import Fore, Style, init
init()

from cryptography.fernet import Fernet


shared_key = b'r-H1L2uA4b9XzD_T4jA1y3Z_qJkYwP0mN8vL5cV7eRk='


def receive_messages(server):
    while True:
        try:
            ddata = server.recv(1024)
            plain_data = Fernet(shared_key).decrypt(ddata).decode('utf-8')
            if not ddata or ddata.lower() == 'exit':
                print(Fore.LIGHTRED_EX + "\n[!]🔌⛔ Client disconnected." + Style.RESET_ALL)
                break
            print(Fore.YELLOW + f"[Client]: {plain_data}" + Style.RESET_ALL)
            print("(server): ", end="")
        except:
            break



      


def start_chatting(server):
    print("\n--- Chat Started (Type 'exit' to stop) ---")
    
    recv_thread = threading.Thread(target=receive_messages, args=(server,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        
        cipher_suite = Fernet(shared_key)


        reply = input(Fore.GREEN +"✅(server): " + Style.RESET_ALL )
        encoded_reply = reply.encode('utf-8')

        chipher_text = cipher_suite.encrypt(encoded_reply)
        server.send(chipher_text)
        if reply.lower() == 'exit':
            break


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(1)
print(Fore.LIGHTCYAN_EX + "Waiting for connection....." + Style.RESET_ALL)
conn, addr = server_socket.accept()
print(Fore.LIGHTGREEN_EX + f"Connected to {addr}✅✅" + Style.RESET_ALL)


while True:
    print("\n1. Start Chatting")
    print("0. Exit Program")
    choice = input("Enter your choice: ")

    if choice == '1':
        start_chatting(conn)
    elif choice == '0':
        print("Closing server...")
        break
    else:
        print("Try-hard🤡")

conn.close()







