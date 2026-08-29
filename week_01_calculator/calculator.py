history = []                                        #пустой список для сохранения строк с результатом

print("Вас приветсвует консольный калькулятор!")
print("Доступные операции: +, -, *, /")
print("Доступные команды: exit - выход из программы, history - просмотр истории операций")

while True:                                         # бесконечный цикл, программа будет работать, пока не встретит break

    command = input("Введите оперцию или команду: ").strip().lower()
    if command == "exit":
        print("До свидания!")
        break

    if command == "history":
        if len(history) == 0:
            print("История пока пуста.")
        else:
            print("\nИстория операций:")
            for operation in history:
                print(operation)
        continue            #continue завершает текущую итерацию цикла и возвращает программу к следующему вводу команды

    if command not in ["+", "-", "*", "/"]:
        print("Ошибка: неизвестная команда")
        continue

    first_number_text = input("Введите первое число: ").strip()
    second_number_text = input("Введите второе число: ").strip()

    first_number = float(first_number_text)
    second_number = float(second_number_text)

    if command == "+":
        result = first_number + second_number
    elif command == "-":
        result = first_number - second_number
    elif command == "*":
        result = first_number * second_number
    elif command == "/":
        if second_number == 0:
            print("Ошибка: делить на ноль нельзя!")
            continue
        result = first_number / second_number

    operation_text = (
        f"{first_number:g} {command} {second_number:g} = {result:g}"
    )

    history.append(operation_text)                      #добавление оперций в историю

    print(f"Результат: {operation_text}")
