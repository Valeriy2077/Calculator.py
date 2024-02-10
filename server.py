import socket
import re
from queue import Queue, PriorityQueue

class CalculatorServer:
    def __init__(self):
        self.operations_queue = Queue() 
        self.priority_queue = PriorityQueue() 
        self.previous_result = None

    def calculate_result(self, expression):
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

    def process_request(self, expression):
        try:
            if expression.lower() == 'mem':
                return self.previous_result

            
            if 'mem' in expression.lower():
                expression = expression.replace('mem', str(self.previous_result))

            result = self.calculate_result(expression)
            self.previous_result = result
            return result
        except ValueError as ve:
            return str(ve)

    def run_server(self):
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

                    if msg.lower() == 'stop':
                        print("Сервер остановлен")
                        break

                    result = self.process_request(msg)
                    output = str(result)
                    server.sendto(output.encode(), client_address)
            except KeyboardInterrupt:
                print("Сервер прерван пользователем")
            finally:
                server.close()

if __name__ == "__main__":
    server = CalculatorServer()
    server.run_server()
