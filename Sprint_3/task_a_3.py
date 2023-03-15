# https://contest.yandex.ru/contest/23815/run-report/83315131/

''' Принцип работы:
В данной задаче необходимо реализовать алгоритм бинарного
поиска на циклически смещенном массиве.
В таком случае удобнее реализовать вариант, использующий
цикл while, вместо рекурсивного варианта.
На каждой итерации находится середина массива mid, 
сравнивается с искомым элементом target, если это он - то 
возвращается его индекс. В противном случае рассматривается
правая половина массива (от середины до крайнего правого
элемента), средний элемент сравнивается с крайним правым - 
проверяется "правильность" подмассива, если он правильно 
отсортирован, то проверятеся наличие в нем искомого элемента.
В случае если искомый элемент находится в границах этого 
подмассива, то на следющей итерации поиск будет происходить 
именно в нем (сдвигается левая граница до mid + 1), иначе в
правом подмассиве (смещается правая граница на mid - 1).
Если же изначально правый подмассив отсортирован неправильно, 
то проверяется наличие таргетного элемента в левом подмассиве, 
при наличии далее поиск в нем, при отсутсивии в правом подмассиве.

Доказательство корректности:
В целом это такой же алгоритм бинарного поиска (т.к. исходный массив
является частично отсортированным), с дополнительными проверками на
сортированность подмассива и на наличие элемента в
его границах.

Временная сложность:
O(log n)

Пространственная сложность:
O(n) для хранения исходного массива.
'''

def broken_search(nums, target):
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
    return -1

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6

