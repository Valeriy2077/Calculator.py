import socket

def get_user_input():
    user_input = input("Введите числа и операции (например, 3 + 5 * 2): ")
    return user_input.strip()

def send_data_to_server(data, server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.sendto(data.encode('utf-8'), (server_address, server_port))

def receive_result_from_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        data, _ = client_socket.recvfrom(1024)
        result = data.decode('utf-8')
        return result

def main():
    server_address = '127.0.0.1'  # Адрес сервера
    server_port = 12345  # Порт сервера (замените на выбранный порт)

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'exit':
            break

        send_data_to_server(user_input, server_address, server_port)

        result = receive_result_from_server()
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
