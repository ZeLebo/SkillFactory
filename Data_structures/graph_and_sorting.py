class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_child = BinaryTree(value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_child = BinaryTree(value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value, end=' ')

        if self.left_child is not None:
            self.left_child.pre_order()

        if self.right_child is not None:
            self.right_child.pre_order()

    def post_order(self):

        if self.left_child is not None:
            self.left_child.post_order()

        if self.right_child is not None:
            self.right_child.post_order()

        print(self.value, end=' ')

    def in_order(self):
        if self.left_child is not None:
            self.left_child.in_order()

        print(self.value)

        if self.right_child is not None:
            self.right_child.in_order()


class Node:
    def __init__(self, value=None, next_=None):
        self.next = next_
        self.value = value

    def __str__(self):
        return f"Node value = {self.value}"


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def clear(self):
        self.__init__()

    def __str__(self):
        result = ''

        pointer = self.first
        while pointer is not None:
            result += f"{pointer.value}"
            pointer = pointer.next
            if pointer is not None:
                result += ' '
        return result

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            node = self.current
            self.current = self.current.next
            return node

    def __len__(self):
        length = 0
        pointer = self.first
        while pointer is not None:
            length += 1
            pointer = pointer.next
        return length

    def push_left(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            self.first = Node(value, self.first)

    def push_right(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            last_node = Node(value)
            self.last.next = last_node
            self.last = last_node

# for linked list normal working
    def pop_left(self):
        if self.first is None:
            return None
        elif self.first == self.last:
            node = self.first
            self.__init__()
            return node
        else:
            node = self.first
            self.first = self.first.next
            return node

    def pop_right(self):
        if self.first is None:
            return None
        elif self.first == self.last:
            node = self.last
            self.__init__()
            return node
        else:
            node = self.last
            pointer = self.first
            while pointer.next is not node:
                pointer = pointer.next
            pointer.next = None
            self.last = pointer
            return Node


def stations_task():
    stations = {
        "Адмиралтейская":
            {
                "Садовая": 4
            },
        "Садовая":
            {
                "Сенная площадь": 3,
                "Спасская": 3,
                "Адмиралтейская": 4,
                "Звенигородская": 5},
        "Сенная площадь":
            {
                "Садовая": 3,
                "Спасская": 3
            },
        "Спасская":
            {
                "Садовая": 3,
                "Сенная площадь": 3,
                "Достоевская": 4
            },
        "Звенигородская":
            {
                "Пушкинская": 3,
                "Садовая": 5
            },
        "Пушкинская":
            {
                "Звенигородская": 3,
                "Владимирская": 4
            },
        "Владимирская":
            {
                "Достоевская": 3,
                "Пушкинская": 4
            },
        "Достоевская":
            {
                "Владимирская": 3,
                "Спасская": 4
            }
    }
    distance = {k: 100 for k in stations.keys()}
    start_k = 'Адмиралтейская'
    distance[start_k] = 0
    is_visited = {k: False for k in stations.keys()}
    parent = {k: None for k in stations.keys()}

    for _ in range(len(distance)):
        min_k = min([k for k in is_visited.keys() if not is_visited[k]], key=lambda x: distance[x])

        for v in stations[min_k].keys():
            if distance[v] > distance[min_k] + stations[min_k][v]:
                distance[v] = distance[min_k] + stations[min_k][v]
                parent[v] = min_k
        is_visited[min_k] = True

    pointer = 'Владимирская'
    while pointer is not None:
        print(pointer, end=',')
        pointer = parent[pointer]


def tree_checker():
    node_root = BinaryTree(2)
    node_root.insert_left(7).insert_right(5)\
        .left_child.insert_left(2).insert_right(6)\
        .right_child.insert_left(5).insert_right(11)\
        .right_child.insert_right(9)\
        .right_child.insert_left(4)
    node_root.in_order()


def linked_list():
    my_list = LinkedList()
    my_list.push_right(1)
    my_list.push_left(2)
    my_list.push_right(3)
    my_list.pop_right()
    my_list.push_left(4)
    my_list.push_right(5)
    my_list.pop_left()

    print(my_list)
    print(len(my_list) == my_list.__len__())


def count(arr: list, n):
    """
    :param arr: array in which to count
    :param n: the element to compare with
    :return: amount of repeated element in array
    """
    result = 0
    for i in arr:
        if i == n:
            result += 1
    return result


def b_search(arr: list, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if arr[middle] == element:
        return middle
    elif arr[middle] > element:
        b_search(arr, element, left, middle - 1)
    else:
        b_search(arr, element, middle + 1, right)


def selection_sort(arr: list):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i, len(arr)):
            if arr[i] < arr[idx_min]:
                idx_min = i
        if i != idx_min:
            arr[i], arr[idx_min] = arr[idx_min], arr[i]
    return arr


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        x = arr[i]
        idx = i
        while idx > 0 and arr[idx - 1] > x:
            arr[idx] = arr[idx - 1]
            idx -= 1
        arr[idx] = x
    return arr


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(arr: list):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def qsort(arr, left, right):
    middle = (left + right) // 2

    pivot = arr[middle]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        if j < left:
            qsort(arr, left, j)
        if i < right:
            qsort(arr, i, right)

    return arr


def main():
    check = '''Hello my dear friend'''
    print(check)


if __name__ == '__main__':
    main()
