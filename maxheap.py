'''
heappush, heappop, heapsort, heapify implementation
pos of element starts from one, to easily calculate, root, left child and right child elements
To access array element, just (pos - 1) will be used
'''

def heappush(heap, item):
    heap.append(item)
    _siftup(heap, len(heap))

def _siftup(heap, pos):
    # pos is starting from 1
    while pos > 1:
        root_pos = pos // 2
        if heap[pos - 1] > heap[root_pos - 1]:
            heap[pos - 1], heap[root_pos - 1] = heap[root_pos - 1], heap[pos - 1]
            pos = pos // 2
        else:
            break

def _siftdown(heap, pos):
    l = len(heap)
    while pos < l:
        left_pos = 2 * pos
        right_pos = left_pos + 1
        if left_pos <= l:
            left = heap[left_pos - 1]
        else:
            left = 0
        if right_pos <= l:
            right = heap[right_pos - 1]
        else:
            right = 0
        if heap[pos-1] < max(left, right):
            if left > right:
                heap[pos-1], heap[left_pos-1] = heap[left_pos - 1], heap[pos-1]
                pos = left_pos
            else:
                heap[pos - 1], heap[right_pos - 1] = heap[right_pos - 1], heap[pos - 1]
                pos = right_pos
        else:
            break

def heappop(heap):
    item = heap.pop()
    if not heap:
        return item
    root = heap[0]
    heap[0] = item
    _siftdown(heap, 1)
    return root

def heapify(tree):
    for i in range(len(tree),0, -1):
        _siftdown(tree, i)

def heapsort(heap):
    new_tree = []
    while heap:
        popped = heappop(heap)
        new_tree.append(popped)
    heap.extend(new_tree)


if __name__ == "__main__":
    heap = [50, 30, 20, 15, 10, 8, 16]
    print(f'Initial heap:\n{heap}')
    print('PUSH(12)')
    heappush(heap, 12)
    print(heap)
    print('PUSH(60)')
    heappush(heap, 60)
    print(heap)
    print('POP')
    heappop(heap)
    print(heap)
    print('POP')
    print(heap)
    heapsort(heap)
    print('Heap sort')
    print(heap)
    arr = [1, 2, 30, 20, 6, 5, 12, 9]
    print(f'New Arr:\n{arr}')
    heapify(arr)
    print(arr)
    arr = [8, 10]
    print(f'New Arr:\n{arr}')
    print('Heapified')
    heapify(arr)
    print(arr)
