from checker import equivalent


def test_equivalent():
    # Test simple types
    assert equivalent(1, 1)
    assert equivalent(2.0, 2.0)
    assert equivalent(True, True)
    assert equivalent("hello", "hello")
    assert not equivalent(1, 2)
    assert not equivalent("hello", "world")
    assert not equivalent(True, False)
    assert not equivalent(1, "hello")

    # Test lists
    assert equivalent([], [])
    assert equivalent([1, 2, 3], [1, 2, 3])
    assert equivalent([1, [2, 3]], [1, [2, 3]])
    assert equivalent(["hello", [1, 2]], ["hello", [1, 2]])
    assert not equivalent([1, 2], [1, 2, 3])
    assert not equivalent([1, 2], [2, 1])
    assert not equivalent([1, [2, 3]], [1, [3, 2]])
    assert not equivalent([1, [2, 3]], [1, [2, 3], 4])
    assert not equivalent(["hello", [1, 2]], ["world", [1, 2]])

    # Test sets
    assert equivalent(set(), set())
    assert equivalent({1, 2, 3}, {1, 2, 3})
    assert equivalent({1, 2, 3}, {3, 2, 1})
    assert not equivalent({1, 2, 3}, {1, 2, 3, 4})
    assert not equivalent({1, 2, 3}, {1, 2})

    # Test dictionaries
    assert equivalent({}, {})
    assert equivalent({"a": 1, "b": 2}, {"a": 1, "b": 2})
    assert equivalent({"a": 1, "b": {"c": 2}}, {"a": 1, "b": {"c": 2}})
    assert equivalent({"a": 1, "b": [2, 3]}, {"a": 1, "b": [2, 3]})
    assert not equivalent({"a": 1, "b": 2}, {"a": 1, "b": 3})
    assert not equivalent({"a": 1, "b": 2}, {"a": 1, "c": 2})
    assert not equivalent({"a": 1, "b": {"c": 2}}, {"a": 1, "b": {"c": 3}})
    assert not equivalent({"a": 1, "b": [2, 3]}, {"a": 1, "b": [3, 2]})


if __name__ == "__main__":
    test_equivalent()
    print("All Tests Pass")
