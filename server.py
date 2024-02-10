import socket
import re
from queue import LifoQueue

class CalculatorServer:
    def __init__(self):
        self.previous_result = None

    def process_request(self, expression):
        try:
            if expression.lower() == 'mem':
                return str(self.previous_result)

            if 'mem' in expression.lower():
                expression = expression.replace('mem', str(self.previous_result))

            rpn_expression = self.infix_to_rpn(expression)
            result = self.calculate_result(rpn_expression)

            self.previous_result = result
            return str(result)
        except ValueError as ve:
            return str(ve)

    def infix_to_rpn(self, infix_expression):
        output = []
        stack = LifoQueue()
        operators = {'+': 1, '-': 1, '*': 2, '/': 2}

        for token in re.findall(r'(\d+|\S)', infix_expression):
            if token.isdigit():
                output.append(token)
            elif token in operators:
                while stack.qsize() > 0 and stack.queue[-1] in operators and operators[stack.queue[-1]] >= operators[token]:
                    output.append(stack.get())
                stack.put(token)
            elif token == '(':
                stack.put(token)
            elif token == ')':
                while stack.qsize() > 0 and stack.queue[-1] != '(':
                    output.append(stack.get())
                stack.get()

        while stack.qsize() > 0:
            output.append(stack.get())

        return ' '.join(output)

    def calculate_result(self, rpn_expression):
        stack = LifoQueue()
        
        if not re.match(r'^[\d\s\+\-\*/]+$',rpn_expression):
            raise ValueError("Некорректное выражение!")

        for token in rpn_expression.split():
            if token.isdigit():
                stack.put(int(token))
            elif token in {'+', '-', '*', '/'}:
                operand2 = stack.get()
                operand1 = stack.get()
                result = self.apply_operator(token, operand1, operand2)
                stack.put(result)

        return stack.get()

    def apply_operator(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                
                raise ValueError("Деление на ноль!")
            return operand1 / operand2

    def run_server(self):
        LOCALHOST = "127.0.0.1"
        PORT = 8000

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
            server.bind((LOCALHOST, PORT))
            print("Сервер запущен")

            try:
                while True:
                    data, client_address = server.recvfrom(1024)
                    msg = data.decode()
                    print(f"Клиент: {client_address} | Получено выражение: {msg}")

                   
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
