history = []

print("Вас приветствует консольный калькулятор!")
print("Доступные операции: +, -, *, /, **")
print(
    "Доступные команды: "
    "exit — выход, history — история, clear — очистка истории"
)

while True:
    command = input("\nВведите операцию или команду: ").strip().lower()

    if command == "exit":
        print("До свидания!")
        break

    if command == "history":
        if not history:
            print("История пока пуста.")
        else:
            print("\nИстория операций:")

            for number, operation in enumerate(history, start=1):
                print(f"{number}. {operation}")

        continue

    if command == "clear":
        history.clear()
        print("История очищена.")
        continue

    if command not in {"+", "-", "*", "/", "**"}:
        print("Ошибка: неизвестная команда.")
        continue

    try:
        first_number = float(
            input("Введите первое число: ").strip()
        )
        second_number = float(
            input("Введите второе число: ").strip()
        )
    except ValueError:
        print("Ошибка: необходимо ввести корректные числа.")
        continue

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
    else:
        try:
            result = first_number ** second_number
        except (OverflowError, ZeroDivisionError):
            print("Ошибка: невозможно выполнить возведение в степень.")
            continue

    operation_text = (
        f"{first_number:g} {command} "
        f"{second_number:g} = {result:g}"
    )

    history.append(operation_text)
    print(f"Результат: {result:g}")
