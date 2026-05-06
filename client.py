#---------------------------------------------
#=-------------=> 🪙 COIN 2.0 <=-------------=
#---------------------------------------------









import socket
import threading

from cryptography.fernet import Fernet
from colorama import init, Style, Fore

shared_key = b'r-H1L2uA4b9XzD_T4jA1y3Z_qJkYwP0mN8vL5cV7eRk='



def receive_messages(client):
    while True:
        try:


            data = client.recv(1024)
            plain_data = Fernet(shared_key).decrypt(data).decode('utf-8')   
            if not data or data.lower() == 'exit':
                print(Fore.LIGHTGREEN_EX + "\n[!]🔌⛔ Server disconnected." + Style.RESET_ALL)
                break
            print(Fore.RED + f"\n[Server]: {plain_data}" + Style.RESET_ALL)
            print("client: ", end="")
        except:
            break





def start_chatting(client):
    print("\n--- Chat Started (Type 'exit' to stop) ---")
    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:

        cipher_suite = Fernet(shared_key)

        message = input(Fore.YELLOW + "✅client: " + Style.RESET_ALL)
        Encoded_message = message.encode('utf-8')

        cipher_text = cipher_suite.encrypt(Encoded_message)

        client.send(cipher_text)
        print("--> تم خروج الرسالة من الكلاينت بنجاح!")
        if message.lower() == 'exit' :
            break






client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))
print("Connected to Server!✅✅")





while True:
    print("\n1. Start Chatting")
    print("0. Exit Program")
    choice = input("Enter your choice: ")

    if choice == '1':
        start_chatting(client_socket)
    elif choice == '0':
        break
    else:
        print("Try-hard🤡")






client_socket.close()










