def convert_number(input_number, from_base, to_base):
    # Преобразование входного числа в десятичное
    if from_base == 10:
        decimal_number = int(input_number)
    else:
        decimal_number = int(input_number, from_base)
    
    # Преобразование десятичного числа в целевую систему счисления
    if to_base == 10:
        return str(decimal_number)
    else:
        # Массив для хранения символов результата
        symbols = "0123456789ABCDEF"
        result = ""
        while decimal_number > 0:
            remainder = decimal_number % to_base
            result += symbols[remainder]
            decimal_number //= to_base
        return result[::-1]  # Развернуть строку для правильного порядка

if __name__ == "__main__":
    # Пример использования:
    input_number = input("Введите число: ")
    from_base = int(input("Введите исходную систему счисления (например, 2, 8, 10, 16): "))
    to_base = int(input("Введите целевую систему счисления (например, 2, 8, 10, 16): "))

    try:
        result = convert_number(input_number, from_base, to_base)
        print(f"Результат: {result}")
    except ValueError as e:
        print("Ошибка, пожалуйста проверьте входные данные.")
