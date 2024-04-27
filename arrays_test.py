import pytest

from arrays import Arrays


@pytest.mark.parametrize("nums", [[1, 2, 3, 1], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]])
def test_contains_duplicate1(nums):
    assert Arrays.contains_duplicate1(nums)


@pytest.mark.parametrize("nums", [[1, 2, 3, 7], [1, 2, 3, 6, 9, 0]])
def test_contains_duplicate1_expect_false(nums):
    assert Arrays.contains_duplicate1(nums) is False


@pytest.mark.parametrize("negative", [[1, 2, 3, 7], [1, 2, 3, 6, 9, 0]])
@pytest.mark.parametrize("positive", [[1, 2, 3, 1], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]])
def test_contains_duplicate2_expect_false(negative, positive):
    assert Arrays.contains_duplicate2(negative) is False
    assert Arrays.contains_duplicate2(positive)
