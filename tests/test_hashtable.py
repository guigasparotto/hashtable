import string
import random
import pytest
from unittest.mock import patch, Mock, MagicMock

from hashtable.bucket import Bucket, Node
from hashtable.hashtable import HashTable

test_key1 = "Dummy1test"
test_key2 = "Dummy2test"
test_values = {test_key1: 123456, test_key2: 123457}

keys_len = 10
long_key = "this key is not in the bucket"


@pytest.fixture
def empty_hashtable():
    return HashTable(10)


@pytest.fixture
def populated_hashtable():
    table = HashTable(100)
    table.insert(test_key1, test_values[test_key1])
    table.insert(test_key2, test_values[test_key2])

    letters = string.ascii_lowercase
    for _ in range(8):
        name = ''.join(random.choice(letters) for _ in range(keys_len))
        number = random.randint(100000, 999999)
        table.insert(name, number)
    return table


def test_insert_returns_correct_length(populated_hashtable):
    populated_hashtable.insert("HashTable", 2023)
    assert len(populated_hashtable) == 11


def test_insert_same_key_updates_existing_value(populated_hashtable):
    new_value = 111111
    populated_hashtable.insert(test_key1, new_value)
    assert populated_hashtable[test_key1] == new_value


def test_get_key_returns_correct_value(populated_hashtable):
    result = populated_hashtable[test_key1]
    assert result == test_values[test_key1]


def test_get_key_returns_none_when_key_does_not_exist(populated_hashtable):
    result = populated_hashtable[long_key]
    assert result is None


# This test is to validate the case where the result is not the first
# node in the bucket, so the function needs to iterate through it
def test_get_key_returns_correct_value_with_mock(empty_hashtable):
    return_node = Node("First Node", 111111)
    return_node.next = Node("Target Node", 222222)

    mock_bucket = MagicMock()
    mock_bucket.first = return_node

    # Patch self.table to return the mock_instance
    with patch.object(empty_hashtable, 'table',
                      new=[mock_bucket] * len(empty_hashtable.table)):
        result = empty_hashtable["Target Node"]
        assert result == 222222


def test_hash_function_is_case_insensitive():
    h1 = HashTable._hash(test_key1)
    h2 = HashTable._hash(test_key1.lower())
    h3 = HashTable._hash(test_key1.upper())
    assert h1 == h2 == h3
