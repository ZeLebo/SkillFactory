import random


def binary_search(a: list, left, right, n: int):
    if left == right:
        return left if a[left] >= n else left + 1

    elif len(a) == 2:
        return 0 if a[0] < n else 1

    elif right > left:
        mid = left + (right - 1) // 2
        if a[mid] == n:
            while a[mid - 1] == n:
                mid -= 1
            return mid
        elif a[mid] > n:
            return binary_search(a, left, mid - 1, n)
        else:
            return binary_search(a, mid + 1, right, n)

    else:
        return -1


def my_sort(a: list):
    if a:
        pivot = a[random.choice(range(0, len(a)))]
        less = my_sort([i for i in a if i < pivot])
        greater = my_sort([i for i in a if i > pivot])
        return less + [i for i in a if i == pivot] + greater
    else:
        return a


def main():
    try:
        a = my_sort(list(map(int, input("Give me the list of numbers:\n").split())))
        n = int(input("Give me the number to find:\n"))
    except ValueError:
        print("It's not a decimal number")
    else:
        print((lambda x: x if x != -1 else "No such position")(binary_search(a, 0, len(a) - 1, n)))


if __name__ == '__main__':
    main()
