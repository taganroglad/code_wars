def is_narcissistic_number(num):
    # здесь мы приводим число в текст (для дальнейшего счет букв)
    num_str = str(num)

    # Здесь мы как раз считаем сколько букв
    num_digits = len(num_str)

    # здесь мы оригинальным способом хотим получить сумму цифр*, где сумма цифровых чисел* возводится в степень числу
    # повторений цифр для цифровых чисел в строке текста
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)

    # проверяем прям в ретерне является ли сумма цифровых чисел номеру что мы внесли
    return digit_sum == num

print(is_narcissistic_number(535353))