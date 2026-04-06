def is_almost_sorted(arr):
    """
    Checks if an array can be fully sorted by swapping at most one pair of elements.
    """
    sorted_arr = sorted(arr)
    mismatches = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            mismatches.append(i)
    
    if len(mismatches) == 0:
        return True
    
    if len(mismatches) == 2:
        return True
        
    return False

def sort_students(students):
    """
    Sorts student records (name, grade, age):
    1. Grade descending
    2. Age ascending
    3. Name ascending
    """
    return sorted(students, key=lambda x: (-x[1], x[2], x[0]))

def insertion_sort(arr):
    """
    Standard stable insertion sort.
    """
    arr_copy = list(arr)
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j][0] > key[0]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

def quick_sort(arr):
    """
    In-place quicksort using Lomuto partition (unstable).
    """
    def partition(arr, low, high):
        pivot = arr[high][0]
        i = low - 1
        for j in range(low, high):
            if arr[j][0] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[j][0] == pivot:
                # To demonstrate instability, we swap even if equal
                # or just follow standard Lomuto which is unstable.
                pass
        
        # Standard Lomuto implementation
        i = low - 1
        for j in range(low, high):
            if arr[j][0] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    arr_copy = list(arr)
    _quick_sort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy

def test_almost_sorted():
    print("--- Testing Almost Sorted ---")
    test_cases = [([1, 2, 3, 4, 5], True), ([1, 5, 3, 4, 2], True), ([1, 5, 4, 3, 2], False)]
    for arr, expected in test_cases:
        result = is_almost_sorted(arr)
        print(f"Array: {arr} | {'PASS' if result == expected else 'FAIL'}")

def test_student_sorting():
    print("\n--- Testing Student Sorting ---")
    students = [("Alice", 90, 20), ("Bob", 90, 19), ("Charlie", 85, 22), ("David", 90, 20)]
    sorted_students = sort_students(students)
    for student in sorted_students:
        print(student)

def test_stability():
    print("\n--- Testing Stability ---")
    data = [(4, 'a'), (3, 'b'), (4, 'c'), (1, 'd')]
    print(f"Original Data: {data}")
    
    ins_sorted = insertion_sort(data)
    print(f"Insertion Sort (Stable): {ins_sorted}")
    
    q_sorted = quick_sort(data)
    print(f"Quick Sort (Often Unstable): {q_sorted}")
    
    # Check stability: (4, 'a') should come before (4, 'c')
    stable_check = ins_sorted.index((4, 'a')) < ins_sorted.index((4, 'c'))
    print(f"Insertion Sort Stable? {stable_check}")
    
    q_stable_check = q_sorted.index((4, 'a')) < q_sorted.index((4, 'c'))
    print(f"Quick Sort Stable? {q_stable_check}")

def kth_smallest(arr, k):
    """
    Finds the kth smallest element in an array using Quickselect.
    k is 1-indexed (e.g., k=1 is the smallest element).
    """
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def select(arr, low, high, k_idx):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k_idx == pivot_index:
            return arr[k_idx]
        elif k_idx < pivot_index:
            return select(arr, low, pivot_index - 1, k_idx)
        else:
            return select(arr, pivot_index + 1, high, k_idx)

    # Convert k to 0-indexed
    return select(list(arr), 0, len(arr) - 1, k - 1)

def test_kth_smallest():
    print("\n--- Testing kth_smallest (Quickselect) ---")
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    result = kth_smallest(arr, k)
    print(f"Array: {arr}, k: {k}")
    print(f"Result: {result} | {'PASS' if result == 7 else 'FAIL'}")

def merge_sort(arr):
    """
    Standard Merge Sort implementation.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
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

def test_performance():
    import time
    import random
    
    print("\n--- Performance Comparison (Merge Sort vs. sorted()) ---")
    sizes = [1000, 5000, 10000]
    print(f"{'Size':<10} | {'Merge Sort (s)':<15} | {'Built-in sorted() (s)':<20}")
    print("-" * 55)
    
    for n in sizes:
        arr = [random.randint(0, 100000) for _ in range(n)]
        
        # Time Merge Sort
        start = time.perf_counter()
        merge_sort(arr)
        ms_time = time.perf_counter() - start
        
        # Time built-in sorted
        start = time.perf_counter()
        sorted(arr)
        builtin_time = time.perf_counter() - start
        
        print(f"{n:<10} | {ms_time:<15.6f} | {builtin_time:<20.6f}")

if __name__ == "__main__":
    test_almost_sorted()
    test_student_sorting()
    test_stability()
    test_kth_smallest()
    test_performance()
