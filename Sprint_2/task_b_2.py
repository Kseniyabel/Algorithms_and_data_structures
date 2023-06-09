# https://contest.yandex.ru/contest/22781/run-report/82567881/

''' Принцип работы:
Данную задачу лучше всего решать при помощи стека.
Стек работает по принципу LIFO. В данном случае стек реализован
с помощью массива. 
На вход подается строка, элементы в ней считываются слева на право.
Для каждого элемента выполняется проверка является ли он числом или 
знаком операции. Если элемемент является числом, он помещается на
стек. Если же элемент является знаком операции, то данная операция
выполняется на двух элементах взятых из стека (в операции элементы
участвуют в порядке добавления). Результат выполененой операции 
помещается на стек. Таким образом итоговый реултат оказывается
на вершине стека.

Доказательство корректности:
Стек работает по принципу LIFO, таким образом на вершине стека всегда
находится либо число, либо результат предыдущих вычислений. Итоговый 
резульат после всех выполеных вычислений всегда будет на вершине стека
и может быть поулчен при помощи stack.pop().

Временная сложность:
Добавление и извлечение элементов из стека выполняется за О(1).
В данной задаче в стеке не находится более двух элементов, таким образом
исключается значительное увеличение длины массива stack.
Проход по всем элементам строки, поданой на вход, выполняется за O(n).

Пространственная сложность:
O(n) памяти для хранения n элементов строки, поданой на вход.
O(n) памяти для хранения n элементов стека.'''

from re import match

def stack_calc(s_list: list) -> int:

    stack = []
    operat = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x // y}
    
    for i in s_list:
        if match(r'^-?\d+$', i):
            stack.append(i)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(operat[i](int(y), int(x)))
    
    return(stack.pop())

def main() -> None:

    s_list = input().split()
    print(stack_calc(s_list))
    
if __name__ == '__main__':
    main()

