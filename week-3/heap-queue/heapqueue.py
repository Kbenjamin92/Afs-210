import heapq

def find_three_largest_numbers(heap):
    find_largest = heapq.nlargest(3, heap)
    return find_largest


result = find_three_largest_numbers([34, 12, 90, 1, 3, 10, 2])
print(result)