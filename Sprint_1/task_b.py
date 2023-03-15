# https://contest.yandex.ru/contest/22450/run-report/82255098/

from collections import Counter

def trainer(k: int, train: list) -> int:

    count = Counter(train)

    del count['.']

    return sum(x <= 2 * k for x in count.values())



def main() -> None:

    k = int(input())
    train = []

    for _ in range(4):
        train.extend(list(input()))
    
    print(trainer(k, train))



if __name__ == '__main__':
    main()