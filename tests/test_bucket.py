import string
import random
import pytest

from hashtable.bucket import Bucket

test_key1 = "Dummy1test"
test_key2 = "Dummy2test"
test_values = {test_key1: 123456, test_key2: 123457}

keys_len = 10
long_key = "this key is not in the bucket"


@pytest.fixture
def empty_hashtable():
    return Bucket()


@pytest.fixture
def populated_bucket():
    """Initialises the bucket with 10 values, of which 8 are random"""
    test_bucket = Bucket()
    test_bucket.append(test_key1, test_values[test_key1])
    test_bucket.append(test_key2, test_values[test_key2])

    letters = string.ascii_lowercase
    for _ in range(8):
        name = ''.join(random.choice(letters) for _ in range(keys_len))
        number = random.randint(100000, 999999)
        test_bucket.append(name, number)
    return test_bucket


def test_append_returns_correct_length(populated_bucket):
    populated_bucket.append("HashTable", 2023)
    assert len(populated_bucket) == 11


def test_remove_returns_true_and_correct_length(populated_bucket):
    r2 = populated_bucket.remove(test_key2)
    r1 = populated_bucket.remove(test_key1)
    assert r1 is True and r2 is True
    assert len(populated_bucket) == 8


def test_remove_from_empty_bucket_returns_false_and_correct_length(empty_hashtable):
    result = empty_hashtable.remove(test_key1)
    assert result is False
    assert len(empty_hashtable) == 0


def test_get_key_returns_correct_value(populated_bucket):
    result = populated_bucket[test_key1]
    assert result == test_values[test_key1]


def test_get_key_returns_none_when_key_does_not_exist(populated_bucket):
    result = populated_bucket[long_key]
    assert result is None


def test_get_node_returns_correct_node_when_it_exists(populated_bucket):
    result_node = populated_bucket.get_node(test_key1)
    assert result_node.key == test_key1


def test_get_node_returns_none_when_node_does_not_exist(populated_bucket):
    result_node = populated_bucket.get_node(long_key)
    assert result_node is None


def test_str_returns_formatted_text(empty_hashtable):
    keys = ["key1", "key2"]
    values = [123456789, 123456790]
    empty_hashtable.append(keys[0], values[0])
    empty_hashtable.append(keys[1], values[1])

    expected_string = f"[{keys[0]}: {values[0]}], [{keys[1]}: {values[1]}]"
    assert str(empty_hashtable) == expected_string
