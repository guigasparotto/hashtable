from typing import List, Optional

from hash_table.bucket import Bucket, Node


class HashTable:
    """
    HashTable class implements a basic hashtable data structure with string keys and any type of values.
    """

    def __init__(self, capacity: int = 1000):
        """
        Initializes a HashTable with the specified capacity.

        :param capacity: The size of the hash table.
        """
        self.table: List[Optional[Bucket]] = [None] * capacity
        self.length = 0

    def __getitem__(self, key: str):
        """
        Retrieves the value associated with the provided key.

        :param key: The key for the item to retrieve.
        :raises KeyError: If the key does not exist in the hash table.
        """
        pos = self._hash(key) % len(self.table)

        if self.table[pos] is not None:
            current: Optional[Node] = self.table[pos].first
            while current is not None:
                if current.key == key:
                    return current.value
                else:
                    current = current.next

        raise KeyError(f"Key '{key}' not found in hashtable")

    def __len__(self) -> int:
        """
        Returns the number of items in the hash table.
        """
        return self.length

    def __str__(self) -> str:
        """
        Returns a string representation of the hash table.
        """
        buckets = []
        for bucket in self.table:
            buckets.append(str(bucket))
        return '\n'.join(buckets)

    def insert(self, key: str, value) -> None:
        """
        Inserts a new item into the hash table. If an item with the same key exists, its value is updated.

        :param key: The key of the item to insert or update.
        :param value: The value of the item to insert or update.
        """
        self._validate_key(key)
        pos = self._hash(key) % len(self.table)

        if self.table[pos] is not None:
            current: Optional[Node] = self.table[pos].get_node(key)
            if current is None:
                self.table[pos].append(key, value)
                self.length += 1
            else:
                current.value = value
        else:
            self.table[pos] = Bucket()
            self.table[pos].append(key, value)
            self.length += 1

    def remove(self, key: str) -> bool:
        """
        Removes an item from the hash table.

        :param key: The key of the item to remove.
        :returns: True if the item was found and removed, False otherwise.
        """
        pos = self._hash(key) % len(self.table)
        bucket = self.table[pos]

        removed = False if bucket is None else bucket.remove(key)
        if removed:
            self.length -= 1

        return removed

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        elif key == "":
            raise ValueError("Key cannot be an empty string")

    @staticmethod
    def _hash(value: str) -> int:
        """
        Generates a hash for a given value using a simple hash function.
        Note: In a real-world scenario, Python's built-in hash function should be used.

        :param value: The value to hash.
        :returns: The generated hash value.
        """
        string = str(value)

        hash_value = 0
        for i, c in enumerate(string, start=1):
            hash_value = hash_value * 31 + ord(c.lower())

        return hash_value
