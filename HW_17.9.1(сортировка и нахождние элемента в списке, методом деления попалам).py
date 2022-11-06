def my_sort(array):  # сортировка методом вставки
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):  # поиск нужно элемента
    if left > right or element <= array[0] or element > array[-1]:
        return 'В введенной последовательности нет нужного нам элемента'

    if right - left == 1:  # промежуток , где находится наш элемент
        return left

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине
        while array[middle] == element:  # проходим влево повторяющиеся числа
            middle -= 1
        return middle
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle)
    else:  # иначе в правой
        return binary_search(array, element, middle, right)


while True:  # проверка правильности ввода последовательности
    try:
        array = list(map(float, input('Введите последовательность чисел через пробел:\n').split()))
        break
    except ValueError:
        print('Вы ввели последовательность не соответствующую требованиям!')

print('Наш список:\n', array)
print('Отсортированный список:\n', my_sort(array))

while True:  # проверка правильности ввода числа
    try:
        element = float(input('Введите любое число:\n '))
        break
    except ValueError:
        print('Вы ввели  не число!')

print('Индекс искомого числа:\n', binary_search(array, element, 0, len(array) - 1))
