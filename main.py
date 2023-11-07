def unique_in_order(number_or_words):
    # Сначала создаем список пустой чтобы можно было все сохранять
    results = []
    # Называем переменную как угодно но она не должна допустить повторения порядка что будет при переборке
    notnotnot = None
    # Ищем некоторый item во всех входных на функции
    for item in number_or_words:
        # если вырезанный нами итем не равен ничему то.... (он потом будет равен текущему значению)
        if item != notnotnot:
            # добавляем к тому самому результату значения в список
            results.append(item)
            # теперь то ничто равно текущему значению
            notnotnot = item
    return results
print(unique_in_order('AAAABBBCCDAABBB'))