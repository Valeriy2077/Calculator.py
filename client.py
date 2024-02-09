import socket

SERVER = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    try:
        while True:
            print("\n-Нельзя делить на 0\n-Вводите только числа\n-Введите stop,либо Ctrl+C чтобы остановить\nПример: 5+8*7")
            inp = input("Введите выражение: ")

            if inp == "stop":
                break

            client.sendto(inp.encode(), (SERVER, PORT))
            result, _ = client.recvfrom(1024)

            if result.decode() == "division_by_zero_error":
                print("Ошибка: Нельзя делить на ноль!")
            elif "Некорректное выражение!" in result.decode():
                print(f"Ошибка: {result.decode()}")
            else:
                print("Result:", result.decode())
    except KeyboardInterrupt:
        print("Клиент прерван пользователем")
