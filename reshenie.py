input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
data = input_data.read()
a = 1
x = 1
N = int(data) # преобразование строки в число
while x < N:
    a = a * (x + 1)
    x = x + 1
output_data = open('output.txt', 'w') # созпдние и открытие файла для вывода ответа
output_data.write(str(a)) # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода