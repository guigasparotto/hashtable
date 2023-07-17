def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "retrieve: tests to validate getting elements from HashTable and Bucket instances"
    )
    config.addinivalue_line(
        "markers",
        "append: tests to validate appending and inserting elements into HashTable and Bucket instances"
    )
    config.addinivalue_line(
        "markers",
        "remove: tests to validate removing elements from HashTable and Bucket instances"
    )
    config.addinivalue_line(
        "markers",
        "magic: tests to validate overridden magic methods"
    )