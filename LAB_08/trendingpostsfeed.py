import heapq
import time
import random

class TrendingHeap:
    def __init__(self):
        self._heap   = []
        self._pos    = {}      
        self._entry  = {}    

    def push(self, post_id, likes, timestamp):
        if post_id in self._entry:
            self.update_likes(post_id, likes, timestamp)
            return
        entry = [-likes, post_id, timestamp]
        self._entry[post_id] = entry
        self._heap.append(entry)
        idx = len(self._heap) - 1
        self._pos[post_id] = idx
        self._bubble_up(idx)

    def pop_max(self):
        if not self._heap:
            return None
        self._swap(0, len(self._heap) - 1)
        entry = self._heap.pop()
        del self._pos[entry[1]]
        del self._entry[entry[1]]
        if self._heap:
            self._bubble_down(0)
        return (-entry[0], entry[1], entry[2])

    def peek_max(self):
        if not self._heap:
            return None
        e = self._heap[0]
        return (-e[0], e[1], e[2])

    def get_top_k(self, k):
        import copy
        temp = TrendingHeap()
        temp._heap  = copy.deepcopy(self._heap)
        temp._pos   = dict(self._pos)
        temp._entry = copy.deepcopy(self._entry)
        result = []
        for _ in range(min(k, len(temp._heap))):
            result.append(temp.pop_max())
        return result

    def update_likes(self, post_id, new_likes, timestamp):
        if post_id not in self._entry:
            return
        idx = self._pos[post_id]
        old_likes = -self._heap[idx][0]
        self._heap[idx][0] = -new_likes
        self._heap[idx][2] = timestamp
        if new_likes > old_likes:
            self._bubble_up(idx)
        else:
            self._bubble_down(idx)

    def size(self):
        return len(self._heap)

    def _swap(self, i, j):
        self._pos[self._heap[i][1]] = j
        self._pos[self._heap[j][1]] = i
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._heap[i][0] < self._heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self._heap)
        while True:
            largest = i
            left    = 2 * i + 1
            right   = 2 * i + 2
            if left  < n and self._heap[left][0]  < self._heap[largest][0]:
                largest = left
            if right < n and self._heap[right][0] < self._heap[largest][0]:
                largest = right
            if largest == i:
                break
            self._swap(i, largest)
            i = largest

    def is_valid_heap(self):
        for i in range(1, len(self._heap)):
            parent = (i - 1) // 2
            if self._heap[i][0] < self._heap[parent][0]:
                return False
        return True

    def get_height(self):
        if not self._heap:
            return 0
        import math
        return math.floor(math.log2(len(self._heap))) + 1

    def get_level_order(self):
        result = []
        i, level_size = 0, 1
        while i < len(self._heap):
            level = [(-e[0], e[1]) for e in self._heap[i:i+level_size]]
            result.append(level)
            i += level_size
            level_size *= 2
        return result

    def simulate_trending(self):
        print("=== Trending Feed Simulation ===")
        for pid in range(100):
            self.push(pid, random.randint(0, 1000), time.time())

        total_time = 0
        for update_num in range(1, 10001):
            pid       = random.randint(0, 99)
            new_likes = random.randint(0, 10000)
            t0 = time.perf_counter()
            self.update_likes(pid, new_likes, time.time())
            total_time += time.perf_counter() - t0

            if update_num % 1000 == 0:
                top5 = self.get_top_k(5)
                print(f"\nAfter {update_num} updates — Top 5:")
                for likes, pid, _ in top5:
                    print(f"  Post {pid}: {likes} likes")

        avg_ms = (total_time / 10000) * 1000
        print(f"\nAverage time per update: {avg_ms:.4f} ms")

def test_exercise2():
    h = TrendingHeap()

    h.push(1, 100, 0)
    h.push(2, 200, 1)
    h.push(3, 150, 2)
    assert h.peek_max() == (200, 2, 1)
    assert h.size() == 3

    top = h.pop_max()
    assert top[0] == 200
    assert h.size() == 2
    assert h.peek_max()[0] == 150

    h.push(4, 50, 3)
    h.update_likes(4, 500, 4)
    assert h.peek_max()[0] == 500
    assert h.peek_max()[1] == 4

    h.update_likes(4, 10, 5)
    assert h.peek_max()[0] == 150

    h2 = TrendingHeap()
    for pid, likes in [(1,300),(2,100),(3,500),(4,200),(5,400)]:
        h2.push(pid, likes, 0)
    top3 = h2.get_top_k(3)
    assert [t[0] for t in top3] == [500, 400, 300]
    assert h2.size() == 5  

    top10 = h2.get_top_k(10)
    assert len(top10) == 5

    assert h2.is_valid_heap() == True

    empty = TrendingHeap()
    assert empty.pop_max() is None
    assert empty.peek_max() is None

    h2.update_likes(999, 1000, 0) 
    assert h2.size() == 5

    assert h2.get_height() == 3 

    print("Exercise 2: ALL TESTS PASSED")

test_exercise2()