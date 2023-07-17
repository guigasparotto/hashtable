from typing import Optional


class Node:
    def __init__(self, key: str, value) -> None:
        """
        Initialize a new node with a key-value pair.
        """
        self.key = key
        self.value = value
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the node.
        """
        return f"[{self.key}: {self.value}]"


class Bucket:
    def __init__(self) -> None:
        """
        Initialize an empty bucket.
        """
        self.first: Optional[Node] = None
        self.length: int = 0

    def __getitem__(self, key: str):
        """
        Get the value associated with the given key.
        Raises KeyError if the key does not exist.
        """
        node = self.get_node(key)
        if node is None:
            raise KeyError(f"Key '{key}' not found in bucket")
        else:
            return node.value

    def __len__(self) -> int:
        """
        Return the number of nodes in the bucket.
        """
        return self.length

    def __str__(self) -> str:
        """
        Return a string representation of the bucket.
        """
        nodes = []
        current = self.first
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return ', '.join(nodes)

    def append(self, key: str, value) -> None:
        """
        Append a new node with the given key-value pair to the bucket.
        If a node with the given key already exists, update its value.
        """
        self._validate_key(key)

        current = self.get_node(key)
        if current is not None:
            current.value = value
        else:
            new_node = Node(key, value)
            if self.first is None:
                self.first = new_node
            else:
                current = self.first
                while current.next is not None:
                    current = current.next
                current.next = new_node
            self.length += 1

    def remove(self, key: str) -> bool:
        """
        Remove the node with the given key from the bucket, if it exists.
        Return True if the node was removed, False otherwise.
        """
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

    def get_node(self, key: str) -> Optional[Node]:
        """
        Return the node with the given key, if it exists.
        Return None if no such node exists.
        """
        if self.first is not None:
            current = self.first
            while current is not None:
                if current.key == key:
                    return current
                else:
                    current = current.next
        return None

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        elif key == "":
            raise ValueError("Key cannot be an empty string")
