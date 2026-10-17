# Завдання 3:
# Python має дві вбудовані функції сортування: sorted і sort. 
# Вони відрізняються тим, що sorted повертає новий відсортований список, а sort сортує список на місці.
# Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

import random
import timeit


 # Сортування вставками
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Рекурсивне сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Вбудоване сортування Python
def timsort(arr):
    return sorted(arr)


# Допоміжна функція - генерує набори даних різних типів
def generate_data(size, data_type):
    data = [random.randint(0, size * 10) for _ in range(size)]

    if data_type == "Випадкові":
        return data
    elif data_type == "Відсортовані":
        return sorted(data)
    elif data_type == "Зворотні":
        return sorted(data, reverse=True)
    elif data_type == "Майже відсортовані":
        data.sort()
        swaps = max(1, size // 100)
        for _ in range(swaps):
            i = random.randrange(size)
            j = random.randrange(size)
            data[i], data[j] = data[j], data[i]
        return data

    return data


# Допоміжна функція - повертає найкращий час із кількох вимірювань
def measure_time(function, data, repeats=3):
    times = timeit.repeat(
        stmt=lambda: function(data),
        repeat=repeats,
        number=1
    )
    return min(times)


def main():
    random.seed(42)

    data_types = [
        "Випадкові",
        "Відсортовані",
        "Зворотні",
        "Майже відсортовані"
    ]

    # Сортування вставками має квадратичну складність
    # на випадкових і зворотно відсортованих даних.
    sizes = [100, 500, 1000, 2000, 5000, 10000]

    algorithms = [
        ("Insertion sort", insertion_sort),
        ("Merge sort", merge_sort),
        ("Timsort (sorted)", timsort)
    ]

    print(f"{'Тип даних':<24} {'Розмір':>8} "
          f"{'Алгоритм':<22} {'Час (сек)':>12}")
    print("-" * 70)

    for data_type in data_types:
        for size in sizes:
            data = generate_data(size, data_type)

            for name, algorithm in algorithms:
                # Обмежуємо часомісткі тести вставок
                if name == "Insertion sort" and size > 2000:
                    continue

                # Перевіряємо правильність результату
                result = algorithm(data)
                assert result == sorted(data), (
                    f"Помилка сортування: {name}"
                )

                elapsed = measure_time(algorithm, data)

                print(
                    f"{data_type:<24} {size:>8} "
                    f"{name:<22} {elapsed:>12.6f}"
                )


if __name__ == "__main__":
    main()

'''
Тип даних                  Розмір Алгоритм                  Час (сек)
----------------------------------------------------------------------
Випадкові                     100 Insertion sort             0.000132
Випадкові                     100 Merge sort                 0.000125
Випадкові                     100 Timsort (sorted)           0.000004
Випадкові                     500 Insertion sort             0.003700
Випадкові                     500 Merge sort                 0.000736
Випадкові                     500 Timsort (sorted)           0.000030
Випадкові                    1000 Insertion sort             0.016280
Випадкові                    1000 Merge sort                 0.001603
Випадкові                    1000 Timsort (sorted)           0.000111
Випадкові                    2000 Insertion sort             0.068314
Випадкові                    2000 Merge sort                 0.003540
Випадкові                    2000 Timsort (sorted)           0.000164
Випадкові                    5000 Merge sort                 0.009803
Випадкові                    5000 Timsort (sorted)           0.000442
Випадкові                   10000 Merge sort                 0.022965
Випадкові                   10000 Timsort (sorted)           0.001159
Відсортовані                  100 Insertion sort             0.000008
Відсортовані                  100 Merge sort                 0.000165
Відсортовані                  100 Timsort (sorted)           0.000002
Відсортовані                  500 Insertion sort             0.000050
Відсортовані                  500 Merge sort                 0.000928
Відсортовані                  500 Timsort (sorted)           0.000005
Відсортовані                 1000 Insertion sort             0.000156
Відсортовані                 1000 Merge sort                 0.002130
Відсортовані                 1000 Timsort (sorted)           0.000009
Відсортовані                 2000 Insertion sort             0.000318
Відсортовані                 2000 Merge sort                 0.004900
Відсортовані                 2000 Timsort (sorted)           0.000018
Відсортовані                 5000 Merge sort                 0.010541
Відсортовані                 5000 Timsort (sorted)           0.000042
Відсортовані                10000 Merge sort                 0.018421
Відсортовані                10000 Timsort (sorted)           0.000070
Зворотні                      100 Insertion sort             0.000275
Зворотні                      100 Merge sort                 0.000102
Зворотні                      100 Timsort (sorted)           0.000001
Зворотні                      500 Insertion sort             0.008267
Зворотні                      500 Merge sort                 0.000570
Зворотні                      500 Timsort (sorted)           0.000004
Зворотні                     1000 Insertion sort             0.036548
Зворотні                     1000 Merge sort                 0.001208
Зворотні                     1000 Timsort (sorted)           0.000011
Зворотні                     2000 Insertion sort             0.135618
Зворотні                     2000 Merge sort                 0.002605
Зворотні                     2000 Timsort (sorted)           0.000023
Зворотні                     5000 Merge sort                 0.007795
Зворотні                     5000 Timsort (sorted)           0.000040
Зворотні                    10000 Merge sort                 0.015753
Зворотні                    10000 Timsort (sorted)           0.000078
Майже відсортовані            100 Insertion sort             0.000016
Майже відсортовані            100 Merge sort                 0.000106
Майже відсортовані            100 Timsort (sorted)           0.000003
Майже відсортовані            500 Insertion sort             0.000089
Майже відсортовані            500 Merge sort                 0.000596
Майже відсортовані            500 Timsort (sorted)           0.000008
Майже відсортовані           1000 Insertion sort             0.000392
Майже відсортовані           1000 Merge sort                 0.001349
Майже відсортовані           1000 Timsort (sorted)           0.000012
Майже відсортовані           2000 Insertion sort             0.001985
Майже відсортовані           2000 Merge sort                 0.003566
Майже відсортовані           2000 Timsort (sorted)           0.000027
Майже відсортовані           5000 Merge sort                 0.009534
Майже відсортовані           5000 Timsort (sorted)           0.000123
Майже відсортовані          10000 Merge sort                 0.039810
Майже відсортовані          10000 Timsort (sorted)           0.000272
'''