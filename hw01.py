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

# Функція для створення різних типів наборів даних
def create_test_data(size):
    # Несортований масив
    unsorted_data = random.sample(range(size * 10), size)

    # Напівсортований масив
    half_sorted_data = sorted(unsorted_data[:size//2]) + unsorted_data[size//2:]

    # Майже відсортований масив
    nearly_sorted_data = sorted(unsorted_data)
    nearly_sorted_data[-1], nearly_sorted_data[-2] = nearly_sorted_data[-2], nearly_sorted_data[-1]  # Змінюємо два останні елементи

    return unsorted_data, half_sorted_data, nearly_sorted_data

# Порівняння ефективності
def compare_sorts():
    sizes = [10, 100, 1000]  # Розміри масивів
    for size in sizes:
        unsorted, half_sorted, nearly_sorted = create_test_data(size)

        print(f"\nРозмір масиву: {size}")

        for data, data_type in zip([unsorted, half_sorted, nearly_sorted], ["несортований", "напівсортований", "майже відсортований"]):
            print(f"\nТестуємо {data_type} набір даних:")

            # Копії для кожного алгоритму
            arr_merge = data.copy()
            arr_insertion = data.copy()
            arr_tim_sort = data.copy()

            # Вимірювання часу для Merge Sort
            merge_time = timeit.timeit(lambda: merge_sort(arr_merge), number=1)
            print(f"Merge Sort: {merge_time:.5f} секунд")

            # Вимірювання часу для Insertion Sort
            insertion_time = timeit.timeit(lambda: insertion_sort(arr_insertion), number=1)
            print(f"Insertion Sort: {insertion_time:.5f} секунд")

            # Вимірювання часу для вбудованого сортування Timsort
            timsort_time = timeit.timeit(lambda: sorted(arr_tim_sort), number=1)
            print(f"Timsort: {timsort_time:.5f} секунд")
            print("-" * 40)

if __name__ == "__main__":
    compare_sorts()
