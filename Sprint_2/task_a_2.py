# https://contest.yandex.ru/contest/22781/run-report/82737063/

''' Принцип работы:
В данной задаче неоходимо реализовать структуру данных "дек".
Так как изначально во входных данных задается максимальный размер дека,
наилучшим вариантом решения является реализация на кольцевом буфере.
Изначально создается массив, содержащий None, его длина равна максимальному
размеру дека (n). В пустом деке голова и хвост находятся в индексе [0].
Хвост (tail) всегда указывается на свободную ячейку в конце списка, голова
(head) на элемент, добавленный в список раньше всех остальных.
При добавлении элементов изменяются значения индексов tail и head.
Значения индексов tail и head берутся по модулю, таким образом массив
"закольцовывается" при переходе через максимальный индекс.

Доказательство корректности:
Структура данных дек должна поддерживать добавление и удаление элементов
с двух сторон, при этом порядок элементов должен быть сохранен.
В данном случае реализовано добавление в начало дека (push_front) и удаление
из начала (pop_front), также добавление в конец дека (push_back) и удаление 
с конца (pop_back). Все эти операции производятся по индексам, которые 
фиксирусются в self.head и self.tail, и изменяются при добавлении элемента.

Временная сложность:
Каждая операция выполняется за О(1), т.к. размер дека фиксированный, 
при каждой операции не нужно снова выделять память, также нет вставки/
удаления элементов из середины массива.

Пространственная сложность:
Расходуется O(n) памяти для хранения самих элементов. '''

class Deque:
    def __init__(self, n):
        self.deque = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0 

    def is_empty(self):
        return self.size == 0
  
    def push_back(self, x):
        if self.size != self.max_n:
            self.deque[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1 
        
        else: print('error')

    def push_front(self, x):
        if self.size != self.max_n:
            self.head = (self.head - 1) % self.max_n 
            self.deque[self.head] = x
            self.size += 1
        
        else: print('error')

    def pop_front(self):
        if self.is_empty():
            print('error')

        else:
            x = self.deque[self.head]
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(x)
 
    
    def pop_back(self):
        if self.is_empty():
            print('error')
        
        else:
            self.tail = (self.tail - 1) % self.max_n
            x = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1 
            print(x)
        


def main() -> None:

    comm = int(input())
    n = int(input())

    q = Deque(n)

    for _ in range(comm):
        cmd = input().split()
        getattr(q, cmd[0])(*cmd[1:])

if __name__ == '__main__':
    main()