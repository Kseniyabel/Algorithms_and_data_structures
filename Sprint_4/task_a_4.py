# https://contest.yandex.ru/contest/24414/run-report/84643367/

''' Принцип работы:
В данной задаче необходимо реализовать простой вариант поисковой системы.
Такую задачу можно разделить на две части (в этом случае две функции).
1 - простроение так называемого "перевернутого индекса" (invert_index).
2 - собственно ответ на запрос (функция query).
Результатом функции invert_index является структура данных, в которой
каждому слову из документов сопоставляется документ, в котором оно встречается 
и количество вхождений. В данном случае использован defaultdict.
В функции query для каждого слова из запроса ищется ключ в полученном словаре.
В итоговый список по индексу номера документа добавляется количество вхождений
слова (переводится в отрицательное значение для удобства последующей сортировки).
Результатом выполнения функции является список из 5ти (или меньше) документов с
самым высоким содержанием слов из запроса.
При выполнении задания использованы следующие статьи:
https://habr.com/ru/post/263823/, https://habr.com/ru/post/263913/

Доказательство корректности:
В данной задаче разрешено использовать встроенные хеш-таблицы, использованы 
defaultdict, Counter, set.

Временная сложность:
Для формирования перевернутого индекса (функция invert_index) - O(n*m),
где n - количесвто документов, m - количество слов в документах.
Для выполнения самих запросов O(k*j*l), где k - число запросов, 
j - количество уникальных слов в запросе, l - количество документов в 
которых находится слово из запроса (количество ключей в словаре, который 
лежит по ключу для данного слова в invert_index).

Пространственная сложность:
Для хранения перевернутого индекса требуется O(n*m) памяти, где n - количество
уникальных слов в документах, m - длина словаря, который лежит по ключу для
каждого слова в inver_index. '''

from collections import Counter, defaultdict

def invert_index(docs: list) -> defaultdict:

    index = defaultdict(dict)
    for docname, words in enumerate(docs):
        for word, count in Counter(words).items():
            index[word][docname] = count
    return index


def query(index: defaultdict, sent: list, lim: int=5, n_docs: int=10**4) -> list:

    res = [0] * n_docs
    for word in set(sent):
        if word in index.keys():
            for docname, count in index[word].items():
                res[docname] -= count
    
    res = [(count, index) for index, count in enumerate(res) if count < 0]
    res.sort()
    return [index for count, index in res[:lim]]


def main() -> None:

    n = int(input())

    docs = [[]]
    docs.extend([input().split() for doc in range(n)])
    inv_ind = invert_index(docs)

    n_query = int(input())

    for _ in range(n_query):
        print(*query(inv_ind, input().split(), lim=5, n_docs=n+1))

if __name__ == '__main__':
    main()