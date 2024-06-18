def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую, значит элемент отсутствует
        return right  # и мы возвращаем искомый индекс

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

try:
    array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    element = int(input("Введите число: "))
except ValueError:
    print("Ай ай ввели не число, атата")
    exit()

print(sort(array)) # сортируем массив
#проверка входит ли введенное число в диапазон

if element<array[0] or element>array[-1]:
    print("Число выходит за диапазон")
else:
    print(binary_search(array, element, 0, len(array) - 1)) # и только после сортировки применяем функцию поиска
