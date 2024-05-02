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


def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    assert Arrays.two_sum(nums, target) == [0, 1]


def test_group_anagrams():
    input_string_list = ["eat", "tea", "tan", "ate", "nat", "bat", "eta"]
    expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "eta", "tea"]]
    output = Arrays.group_anagrams(input_string_list)
    for group in output:
        assert sorted(group) in expected_output
