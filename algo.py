 #PArt 1
class HeapSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        self.build_heap()
        for i in range(len(self.array) - 1, 0, -1):
            self.swap(0, i)
            self.heapify(0, i)

    def build_heap(self):
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i, n)

    def heapify(self, root_index, heap_size):
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2

        if left_child < heap_size and self.array[left_child] > self.array[largest]:
            largest = left_child
        
        if right_child < heap_size and self.array[right_child] > self.array[largest]:
            largest = right_child

        if largest != root_index:
            self.swap(root_index, largest)
            self.heapify(largest, heap_size)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def get_sorted_array(self):
        return self.array


# usage:
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    heap_sort = HeapSort(array)
    heap_sort.sort()
    print("Sorted array is:", heap_sort.get_sorted_array())


#Part 2
class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])  # Path compression
        return self.root[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.root[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.root[root_u] = root_v
            else:
                self.root[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # x[2] is the weight of the edge
    uf = UnionFind(vertices)
    mst_edges = []
    mst_cost = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            mst_cost += weight

    return mst_edges, mst_cost

# usage
if __name__ == "__main__":
    # Define the number of vertices and the edges (u, v, weight)
    vertices = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4),
    ]

    mst_edges, mst_cost = kruskal(vertices, edges)
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"{u} - {v}: {weight}")
    print(f"Total cost of MST: {mst_cost}")
