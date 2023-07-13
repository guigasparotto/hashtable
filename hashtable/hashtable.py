import sys
from typing import List, Optional

from hashtable.bucket import Bucket, Node


class HashTable:
    def __init__(self, capacity: int = 1000):
        self.table: List[Optional[Bucket]] = [None] * capacity
        self.length = 0

    def __getitem__(self, key):
        pos = self._hash(key) % len(self.table)

        if self.table[pos] is not None:
            current: Optional[Node] = self.table[pos].first
            while current is not None:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
        return None

    def __len__(self):
        return self.length

    def __str__(self):
        buckets = []
        for bucket in self.table:
            buckets.append(str(bucket))
        return '\n'.join(buckets)

    def insert(self, key, value):
        pos = self._hash(key) % len(self.table)

        if self.table[pos] is None:
            self.table[pos] = Bucket()
            self.table[pos].append(key, value)
            self.length += 1
        else:
            bucket = self.table[pos]
            current: Optional[Node] = bucket.get_node(key)
            if current is None:
                self.table[pos].append(key, value)
                self.length += 1
            else:
                current.value = value

    def remove(self, key):
        pos = self._hash(key) % len(self.table)
        bucket = self.table[pos]
        return bucket.remove(key)

    def print_distribution(self, graphic=False):
        maxl = 0
        minl = sys.maxsize
        for i in range(len(self.table)):
            current = self.table[i]
            if current is not None:
                length = len(current)
                minl = length if length < minl else minl
                maxl = length if length > maxl else maxl

                if (graphic):
                    print(f"[pos {i:2d} - {length:2d}]", '#' * length)
            else:
                if (graphic):
                    print(f"[pos {i:2d} -  0]")

        print(f"Smallest bucket: {minl}")
        print(f"Largest bucket: {maxl}")

    @staticmethod
    def _hash(value) -> int:
        string = str(value)

        hash_value = 0
        for i, c in enumerate(string, start=1):
            hash_value = hash_value * 31 + ord(c.lower()) * i

        return hash_value
