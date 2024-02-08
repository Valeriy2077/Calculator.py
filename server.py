import socket
import queue
import threading

class CalculatorServer:
    def __init__(self, port):
        self.server_address = '127.0.0.1'
        self.server_port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.server_address, self.server_port))
        self.result = 0
        self.operation_queue = queue.Queue()

    def handle_client_request(self, data, client_address):
        try:
            result = self.calculate(data)
            self.result = result
            message = f"Результат: {result}"
        except ValueError as ve:
            message = f"Ошибка: {ve}"

        self.server_socket.sendto(message.encode('utf-8'), client_address)

    def calculate(self, expression):
        # Ваш код для вычисления выражения
        while(True):
            print()
    try:
        nums = int(input("How many numbers you want to calculate?\n"))
    # x = float(input("Enter the first number: "))
    # y = float(input("Enter the second number: "))
    # z = float(input("Enter the third number: "))
    # w = float(input("Enter the forth number: "))
    # v = float(input("Enter the fifth number: "))

        if nums == 2:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y)
            if func == 2:
                print(x-y)
            if func == 3:
                print(x*y)
            if func == 4:
                print(x/y)
        if nums == 3:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z)
            if func == 2:
                print(x-y-z)
            if func == 3:
                print(x*y*z)
            if func == 4:
                print(x/y/z)
        if nums == 4:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            w = float(input("Enter the forth number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z+w)
            if func == 2:
                print(x-y-z-w)
            if func == 3:
                print(x*y*z*w)
            if func == 4:
                print(x/y/z/w)
        if nums == 5:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            z = float(input("Enter the third number: "))
            w = float(input("Enter the forth number: "))
            v = float(input("Enter the fifth number: "))
            print()
            func = int(input('''What do you want to do?
            1 to add
            2 to subtract
            3 to multiply
            4 to divide
            '''))
            if func == 1:
                print(x+y+z+w+v)
            if func == 2:
                print(x-y-z-w-v)
            if func == 3:
                print(x*y*z*w*v)
            if func == 4:
                print(x/y/z/w/v)
        if nums > 5:
            print("The calculator handles 5 numbers maximum!")
    except(ZeroDivisionError):
        print("You can never divide by Zero!")
    except(ValueError):
        print("Check your input.")
        
         # Ваш код для вычисления выражения

        pass

    def process_operation_queue(self):
        while True:
            if not self.operation_queue.empty():
                data, client_address = self.operation_queue.get()
                self.handle_client_request(data, client_address)

    def start_server(self):
        print(f"Сервер запущен на {self.server_address}:{self.server_port}")

        # Запуск потока для обработки очереди операций
        threading.Thread(target=self.process_operation_queue, daemon=True).start()

        while True:
            data, client_address = self.server_socket.recvfrom(1024)
            data = data.decode('utf-8')

            if data.lower() == 'exit':
                break

            # Добавление операции в очередь для обработки
            self.operation_queue.put((data, client_address))

        self.server_socket.close()

def main():
    server_port = 12345  # Порт сервера (замените на тот, который вы выбрали в клиенте)
    calculator_server = CalculatorServer(server_port)
    calculator_server.start_server()

if __name__ == "__main__":
    main()
