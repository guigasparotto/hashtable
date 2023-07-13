from typing import Optional


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Optional[Node] = None

    def __str__(self):
        return f"[{self.key}: {self.value}]"


class Bucket:
    def __init__(self):
        self.first = None
        self.length = 0

    def __getitem__(self, key):
        return None if self.get_node(key) is None else self.get_node(key).value

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        nodes = []
        current = self.first
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return ', '.join(nodes)

    def append(self, key, value) -> None:
        if self.first is None:
            self.first = Node(key, value)
        else:
            current = self.first
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)
        self.length += 1

    def remove(self, key) -> bool:
        previous: Optional[Node] = None
        current = self.first

        while current is not None:
            if current.key == key:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.first = current.next
                self.length -= 1
                return True
            else:
                previous = current
                current = current.next
        return False

    def get_node(self, key) -> Optional[Node]:
        if self.first is not None:
            current = self.first
            while current is not None:
                if current.key == key:
                    return current
                else:
                    current = current.next
        return None
