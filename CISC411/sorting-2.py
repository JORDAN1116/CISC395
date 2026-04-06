from random import randint

"""bubble sort O(n^2)stable"""
def bubble_sort(seq):
    n = len(seq) # number of elements, length of seq
    for i in range(n-1): # passes
        for j in range(n-i-1): # compare adjacent pairs
            if seq[j] > seq[j+1]: # if wrong order
                seq[j], seq[j+1] = seq[j+1], seq[j] # swap them
    return seq
                

"""selection sort O(n^2) unstable"""
def selection_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min = i # min is index of the minimum element
        for j in range(i+1, n):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]
    return seq


"""insertion sort O(n^2) stable """
def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n): # from second element to the last element
        marked = seq[i]
        j = i
        while j >= 1 and seq[j-1] > marked: # shift elements greater than marked right
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = marked
    return seq

"""shell sort is optimization of insertion sort
this allows sorting elements far apart using an interval"""
def shell_sort(seq):
    n = len(seq)
    interval = n // 2 
    while interval > 0: # reduce the interval
        # apply insertion sort on each subsequence
        for i in range(interval, n):
            temp = seq[i]
            j = i
            while j >= interval and seq[j-interval] > temp:
                seq[j] = seq[j-interval]
                j -= interval
            seq[j] = temp
        interval //= 2
    return seq
        
def partition(seq, start, end):
    pivot = seq[end]
    left = start
    right = end - 1
    while left <= right:
        while seq[left] <= pivot and left <= right:
            left += 1
        while seq[right] >= pivot and left <= right:
            right -= 1
        if left <= right:
            seq[left], seq[right] = seq[right], seq[left]
            left += 1
            right -= 1
    seq[left], seq[end] = seq[end], seq[left]
    return left 

def quick_sort(seq, start, end):
    if start >= end:
        return seq
    left = partition(seq, start, end)
    quick_sort(seq, start, left-1)
    quick_sort(seq, left+1, end)
    return seq

def merge_sort(seq):
    n = len(seq)
    if n < 2:
        return seq
    s1 = seq[:n//2]
    s2 = seq[n//2:]
    merge_sort(s1)
    merge_sort(s2)
    seq = merge(seq, s1, s2)
    return seq 

def merge(s, s1, s2):
    i = 0
    j = 0
    while i + j < len(s):
        if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
    return s

def heap_sort(seq):
    n = len(seq)
    for i in range(n,-1,-1):
        heapify(seq, n, i)
    for j in range(n-1, 0, -1):
        seq[j], seq[0] = seq[0], seq[j]
        heapify(seq, j, 0)
    return seq

def heapify(seq, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and seq[i] < seq[l]:
        max = l
    if r < n and seq[max] < seq[r]:
        max = r
    if max != i:
        seq[i], seq[max] = seq[max], seq[i]
        heapify(seq, n, max)
    
            
# test case
seq = [randint(1,10) for i in range(20)]
print(seq)
#print('bubble', bubble_sort(seq))
#print('selection', selection_sort(seq))
#print('insertion', insertion_sort(seq))
#print('shell', shell_sort(seq))
#print('quick', quick_sort(seq, 0, len(seq)-1))
#print('merge', merge_sort(seq))
print('heap', heap_sort(seq))
