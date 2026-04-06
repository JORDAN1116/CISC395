# build a segment tree
from math import log2, ceil

class SegmentTree:
    # for sum query
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        # size of segment tree
        size = 2 * 2 ** int(ceil(log2(self.n))) - 1
        self.segment_tree = [0] * size
        # whole arr to build segment start = 0, end = self.n - 1
        # start from the root of segment tree
        self.__build_helper(0, self.n-1, 0)

    # recursively build segment tree for sum queries
    def __build_helper(self, start, end, i):
        # i: index of element in segment tree
        # internal node = sum of its childrem
        # original elements in arr stored in leaf nodes
        # base case:  start ==  end
        if start == end: # leaf
            self.segment_tree[i] = self.arr[start]
            return self.segment_tree[i]
        mid = (start + end) // 2 # middle index
        # left child [start, mid]
        # right child [mid+1, end]
        self.segment_tree[i] = self.__build_helper(start, mid, 2 * i + 1) + \
                               self.__build_helper(mid+1, end, 2 * i + 2)
        return self.segment_tree[i]

if __name__ == '__main__':
    arr = [1,3,5,7,9,11]
    stree = SegmentTree(arr)

    
        
