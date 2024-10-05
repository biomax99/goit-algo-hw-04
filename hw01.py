import timeit
import random

# Реалізація алгоритму злиття (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація алгоритму вставок (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Порівняння ефективності
def compare_sorts():
    sizes = [100, 1000, 5000]  # Різні розміри масивів
    for size in sizes:
        arr = random.sample(range(size * 10), size)

        # Копії для кожного алгоритму
        arr_merge = arr.copy()
        arr_insertion = arr.copy()
        arr_tim_sort = arr.copy()

        # Вимірювання часу для Merge Sort
        merge_time = timeit.timeit(lambda: merge_sort(arr_merge), number=1)
        print(f"Merge Sort для {size} елементів: {merge_time:.5f} секунд")

        # Вимірювання часу для Insertion Sort
        insertion_time = timeit.timeit(lambda: insertion_sort(arr_insertion), number=1)
        print(f"Insertion Sort для {size} елементів: {insertion_time:.5f} секунд")

        # Вимірювання часу для вбудованого сортування Timsort (використовується у sorted())
        timsort_time = timeit.timeit(lambda: sorted(arr_tim_sort), number=1)
        print(f"Timsort для {size} елементів: {timsort_time:.5f} секунд")
        print("-" * 40)

if __name__ == "__main__":
    compare_sorts()
