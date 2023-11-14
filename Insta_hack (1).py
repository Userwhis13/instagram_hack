import random

def random_characters():
    counter = 0
    while True:
        user_input = input("Привет, введите ник (пример: bars09): ")
        print(user_input)
        while True:
            random_length = random.randint(10, 20)  # Генерируем случайную длину для последовательности символов
            random_string = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()') for _ in range(random_length))  # Создаем случайную последовательность символов
            print(random_string)
            input("Для генерации следующей последовательности нажмите Enter.")
            counter += 1
            if counter == 30:
                print("KINGOFSEA - Sucessfully")
                return

random_characters()
x = input(" ENTER TO EXIT " )       
print(" ENTER TO EXIT, " + x)  
input(" ENTER TO EXIT ")
