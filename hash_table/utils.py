import sys
from hash_table.hashtable import HashTable


def print_distribution(hashtable: HashTable, graphic=False):
    """
    Debugging function to visualise the number of elements across the buckets in
    the HashTable - useful to validate how the hash function is distributing the elements

    :param hashtable: HashTable instance to which you want to visualise its distribution
    :param graphic: When set to True, it will print a representation of the nodes across buckets.
    If set to False (default) it just prints the number of nodes in the smallest and largest buckets
    """
    maxl = 0
    minl = sys.maxsize
    for i in range(len(hashtable.table)):
        current = hashtable.table[i]
        if current is not None:
            length = len(current)
            minl = length if length < minl else minl
            maxl = length if length > maxl else maxl

            if graphic:
                print(f"[pos {i:2d} - {length:2d}]", '#' * length)
        else:
            if graphic:
                print(f"[pos {i:2d} -  0]")

    print(f"Smallest bucket: {minl}")
    print(f"Largest bucket: {maxl}")
