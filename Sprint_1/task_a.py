# https://contest.yandex.ru/contest/22450/run-report/82252624/

def nearest_null(n: int, numbers: list) -> list:

    res = [0] * n

    null_in = 0
    cnt = 0

    for i in range(n):
        if numbers[i] == 0:
            cnt = 0
            null_in = 1
        elif numbers[i] !=0 and null_in == 1:
            cnt += 1
            res[i] = cnt

    cnt = 0
    null_in = 0

    for i in range(n-1, -1, -1):
        if numbers[i] == 0:
            cnt = 0
            null_in = 1
        elif numbers[i] !=0 and null_in == 1:
            cnt += 1
            if res[i] < cnt and res[i] != 0:
                res[i]
            else:
                res[i] = cnt

    return(res)


def main() -> None:

    n = int(input())
    numbers = list(map(int, input().split()))

    print(*nearest_null(n, numbers))



if __name__ == '__main__':
    main()
