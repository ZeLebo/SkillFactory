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
            if pointer is not None:
                result += ''
        return result

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


def main():
    node_root = BinaryTree(2)
    node_root.insert_left(7).insert_right(5)\
        .left_child.insert_left(2).insert_right(6)\
        .right_child.insert_left(5).insert_right(11)\
        .right_child.insert_right(9)\
        .right_child.insert_left(4)
    node_root.in_order()


if __name__ == '__main__':
    main()
