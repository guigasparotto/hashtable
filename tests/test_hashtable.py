import string
import random
from time import perf_counter

import pytest
from unittest.mock import patch, Mock, MagicMock

from hash_table.bucket import Bucket, Node
from hash_table.hashtable import HashTable

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


@pytest.mark.append
def test_insert_increases_table_length(populated_hashtable):
    populated_hashtable.insert("HashTable", 2023)
    assert len(populated_hashtable) == 11


@pytest.mark.append
def test_insert_same_key_updates_existing_value(populated_hashtable):
    new_value = 111111
    populated_hashtable.insert(test_key1, new_value)
    assert populated_hashtable[test_key1] == new_value


@pytest.mark.append
@pytest.mark.parametrize('key', [None, 100, True])
def test_insert_with_incorrect_type_key_raises_type_error(empty_hashtable, key):
    with pytest.raises(TypeError):
        empty_hashtable.insert(key, "value")


@pytest.mark.append
def test_insert_with_empty_string_key_raises_value_error(empty_hashtable):
    with pytest.raises(ValueError):
        empty_hashtable.insert("", "value")


@pytest.mark.retrieve
def test_get_key_returns_correct_value(populated_hashtable):
    result = populated_hashtable[test_key1]
    assert result == test_values[test_key1]


@pytest.mark.retrieve
def test_get_key_returns_key_error_when_key_does_not_exist(populated_hashtable):
    with pytest.raises(KeyError):
        result = populated_hashtable[long_key]


# This test is to validate the case where the result is not the first
# node in the bucket, so the function needs to iterate through it
@pytest.mark.retrieve
def test_get_key_returns_correct_value_from_bucket_with_collisions(empty_hashtable):
    return_node = Node(test_key1, test_values[test_key1])
    return_node.next = Node(test_key2, test_values[test_key2])

    mock_bucket = MagicMock()
    mock_bucket.first = return_node

    # Patch self.table to return the mock_instance
    with patch.object(empty_hashtable, 'table',
                      new=[mock_bucket] * len(empty_hashtable.table)):
        result = empty_hashtable[test_key2]
        assert result == test_values[test_key2]


@pytest.mark.remove
def test_remove_returns_true_and_correct_length(populated_hashtable):
    r2 = populated_hashtable.remove(test_key2)
    r1 = populated_hashtable.remove(test_key1)
    assert r1 is True and r2 is True
    assert len(populated_hashtable) == 8


@pytest.mark.remove
def test_remove_from_empty_hashtable_returns_false_and_correct_length(empty_hashtable):
    result = empty_hashtable.remove(test_key1)
    assert result is False
    assert len(empty_hashtable) == 0


def test_hash_function_is_case_insensitive():
    h1 = HashTable._hash(test_key1)
    h2 = HashTable._hash(test_key1.lower())
    h3 = HashTable._hash(test_key1.upper())
    assert h1 == h2 == h3


@pytest.mark.magic
def test_str_returns_formatted_text():
    table = HashTable(2)
    keys = ["key1", "key2"]
    values = [123456789, 123456790]

    table.insert(keys[0], values[0])
    table.insert(keys[1], values[1])

    expected_string = f"[{keys[0]}: {values[0]}]\n[{keys[1]}: {values[1]}]"
    assert str(table) == expected_string


@pytest.mark.skip("Example test to measure the time taken to retrieve a record, remove mark if required")
def test_hashtable_handles_large_number_of_records():
    table = HashTable()
    string_size = 10
    records = 100000

    for i in range(records):
        table.insert(get_random_string(string_size), random.randint(10000, 99999))

    table.insert(test_key1, test_values[test_key1])

    before = perf_counter()
    result = table[test_key1]
    after = perf_counter() - before
    assert result == test_values[test_key1]
    assert after < 0.00005


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
