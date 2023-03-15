# https://contest.yandex.ru/contest/23815/run-report/83825006/

''' Принцип работы:
В данной задаче необходимо реализовать алгоритм быстрой
сортировки, который не затрачивает дополнительную оперативную
память (in-place quick sort).
В функции change_values происходит преобразование исходных значений
для дальнейшего сравнения, возвращается список значений.
В функции partition происходит выбор опорного элемента pivot,
далее вместо разделения элементов на группы (именно этот этап обычно 
требует дополнительную память) используются два указателя start и end,
которые непосредственно в самом массиве указывают на левый и правый 
его концы. Start - это опорный элемент pivot. Если элмент в левой части
массива меньше, чем pivot, то он остается на месте, если элемент в 
правой части массива больше, чем pivot он тоже остается на месте,
в противном случае элементы меняются местами.
В функции quick_sort вызывается функция partition, затем рекурсивно
quick_sort для левой и правой частей. 

Доказательство корректности:
Все манипуляции с элементами массива происходят в самом массиве,
соответственно не создается дополнительных массивов, не требуется
дополнительная оперативная память.

Временная сложность:
Для быстрой сортировки O(n log n) в среднем, O(n^2) в худшем случае.
Если всего O(n log n) сравнений, но в сравнении участвуют строки, то
учитывая их размер получается O(m * n * log n), где m - длина строки.

Пространственная сложность:
Так как это рекурсивная сортировка, необходимо пространство для 
выполнения рекурсивных вызовов (необходимо учитывать объем стека
вызовов). В среднем случае - O(log n), в худшем - O(n).
'''


def change_values(vals: list) -> list:
    vals[1] = - int(vals[1])
    vals[2] = int(vals[2])
    return (vals[1], vals[2], vals[0])

def partition(values: list, start: int, end: int) -> int:
    pivot = values[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and values[i] <= pivot):
            i = i + 1
        while (i <= j and values[j] >= pivot):
            j = j - 1
 
        if i <= j:
            values[i], values[j] = values[j], values[i]
        else:
            values[start], values[j] = values[j], values[start]
            return j
            
def quick_sort(values: list, left: int, right: int) -> None:
    if ((right - left) > 1):
        p = partition(values, left, right)
        quick_sort(values, left, p)
        quick_sort(values, p + 1, right)

def main() -> None:
    n = int(input())
    values_list = [change_values(input().split()) for _ in range(n)]
    quick_sort(values_list, 0, len(values_list))
    print(*[i[2] for i in values_list], sep='\n')

        

if __name__ == '__main__':
    main()