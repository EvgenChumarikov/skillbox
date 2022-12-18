while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

n = int(input('Введите количество операндов: '))
if n >= 0:
 
  for i in range(1, n + 1):
    a = int(input(f'Введите число {i}: '))
    result = 0
    if command == "+":
      result += a
     
    elif command == "-":
      result -= a
      
    elif command == "*":
      result *= a
      
    elif command == "/":
      result /= a
      
  print(f'{a} {command} = {result}')
else:
  print('Количество должно быть больше нуля')