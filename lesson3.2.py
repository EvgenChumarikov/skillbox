while True:
  command = input('Выберете операцию: ')
  if command in "+-*/":
    break
  print('Ошибка: такой операции не существует.Попробуйте еще раз.')

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = 0
if command == "+":
    result = a + b
elif command == "-":
    result = a - b
elif command == "*":
    result = a * b
elif command == "/":
    result = a / b

print(f"{a} {command} {b} = {result}")