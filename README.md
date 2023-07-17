# Python HashTable Implementation

This is a simple, educational project that demonstrates a basic implementation of a hashtable in Python. It's designed for learning and exploring data structures and their functionality.

## Overview

The hashtable uses a custom `Bucket` class to handle collisions, demonstrating a chaining collision resolution strategy.

The project includes the following main components:

- **Bucket Class:** This class represents a bucket in the hashtable. It contains a linked list of nodes, each of which holds a key-value pair. The `Bucket` class includes methods to append, remove, and retrieve nodes.

- **Node Class:** This class represents a node in the bucket. Each node contains a key-value pair and a pointer to the next node.

- **HashTable Class:** This class implements the hashtable. It includes methods to insert, remove, and retrieve key-value pairs. The hashtable includes a custom hash function to determine the index for each key and handles collisions by chaining.

- **Utils:** The `print_distribution` function in the `utils.py` file was created for debugging purposes. It prints the number of keys in each bucket, allowing you to visualize the distribution of keys in the hashtable.

## Getting Started

### Cloning the Project

1. Open Terminal.

2. Change the current working directory to the location where you want the cloned directory.

3. Type `git clone`, and then paste the URL of this repo.

    ```
    git clone https://github.com/guigasparotto/hashtable.git
    ```

4. Press Enter to create your local clone.

### Running the Project in PyCharm

1. Open PyCharm.

2. Click on "Open".

3. Navigate to the directory where you cloned the project.

4. Select the directory and click "OK".

5. Once the project is open, you can run the tests by right-clicking in the test file you want to run and selecting "Run". Pytest must be installed.

### Running Tests Via Command Line

You can run tests via the command line using `pytest`. Pytest has several options you can use, see some of them below:

- `-v` or `--verbose`: increases verbosity.

    ```
    pytest -v
    ```

- `-k`: to run tests which match the given keyword expression.

    ```
    pytest -k "test_keyword"
    ```

- `-x`: to stop testing after the first failure.

    ```
    pytest -x
    ```

## Pytest Marks

Pytest markers have been used to categorize the tests based on their purpose:

- **retrieve:** Tests to validate getting elements from HashTable and Bucket instances.
- **append:** Tests to validate appending and inserting elements into HashTable and Bucket instances.
- **remove:** Tests to validate removing elements from HashTable and Bucket instances.
- **magic:** Tests to validate overridden magic methods.

You can run a specific category of tests by using the `-m` or `--marker` flag with `pytest` and specifying the relevant marker. Here are some examples:

```bash
# Run all 'append' tests
pytest -m append

# Run all 'retrieve' tests
pytest -m retrieve

# Run all 'remove' tests
pytest -m remove

# Run all 'magic' tests
pytest -m magic
```

## Documentation

Docstrings were added to all classes and methods for consistency and educational purposes. This approach may make the project more verbose than necessary in a real-world application, but it serves to clarify the purpose and functionality of each component for learning purposes.

## Disclaimer

This project is for educational purposes only and may not be suitable for production environments without further modification and testing.