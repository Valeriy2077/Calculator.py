import socket
import re

def calculate_result(expression):
    if not re.match(r'^[\d\s\+\-\*/]+$', expression):
        raise ValueError("Некорректное выражение!")

    tokens = re.findall(r'(\d+|\S)', expression)
    numbers = [int(token) for token in tokens if token.isdigit()]
    operators = [token for token in tokens if token in {'+', '-', '*', '/'}]

    result = numbers[0]
    for i in range(len(operators)):
        operator = operators[i]
        number = numbers[i + 1]

        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == '*':
            result *= number
        elif operator == '/':
            if number == 0:
                return "division_by_zero_error"
            result /= number

    return result

LOCALHOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((LOCALHOST, PORT))
    print("Сервер запущен")

    try:
        while True:
            data, client_address = server.recvfrom(1024)
            print("Выражение получено", client_address)

            msg = data.decode()

            if msg == 'stop':
                print("Сервер остановлен")
                break

            try:
                result = calculate_result(msg)
                output = str(result)
                server.sendto(output.encode(), client_address)
            except ValueError as ve:
                server.sendto(str(ve).encode(), client_address)
    except KeyboardInterrupt:
        print("Сервер прерван пользователем")
    finally:
        server.close()
