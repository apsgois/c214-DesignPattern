def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data)//2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


class SortContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        self.strategy(data)


data = [7, 2, 5, 1, 8, 3]
context = SortContext(bubble_sort)
print("Dados iniciais:", data)
context.sort(data)
print("Ordenado por bolha:", data)
context.set_strategy(insertion_sort)
context.sort(data)
print("Ordenado por inserção:", data)
context.set_strategy(selection_sort)
context.sort(data)
print("Ordenado por seleção:", data)
context.set_strategy(merge_sort)
context.sort(data)
print("Ordenado por merge:", data)
context.set_strategy(quick_sort)
context.sort(data)
print("Ordenado por Quick:", data)