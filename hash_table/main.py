import random
import string
from time import perf_counter

from hash_table.hashtable import HashTable
from hash_table.utils import print_distribution


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


table_size = 20
hashtable = HashTable(table_size)
hashtable.insert("Test1", 123458679)
hashtable.insert("Test2", 123458679)
hashtable.insert("Test1", 111111111)

for i in range(200):
    hashtable.insert(get_random_string(10), random.randint(1000000, 50000000))


before = perf_counter()
print(hashtable["Test2"])
print(f"Time: {perf_counter() - before}")

print_distribution(hashtable, True)