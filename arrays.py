from collections import defaultdict


class Arrays:
    @staticmethod
    def contains_duplicate1(nums: list[int]) -> bool:
        """
        Given an integer array nums:
         - return true if any value appears at least twice in the array,
         - return false if every element is distinct.
        Checks for duplicates using count() list method
        :param: array of integers
        :return: True or False
        """
        x: int
        for x in nums:
            if nums.count(x) > 1:
                return True
        return False

    @staticmethod
    def contains_duplicate2(nums: list[int]) -> bool:
        """
        Given an integer array nums:
         - return true if any value appears at least twice in the array,
         - return false if every element is distinct.
        Checks duplicates in array by leveraging a hashset
        :param: array of integers
        :return: True or False
        """
        hashset: set[int] = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False

    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        value_index_map: dict = dict()
        for index, value in enumerate(nums):
            difference = target - value
            if difference in value_index_map.keys():
                return [value_index_map[difference], index]
            value_index_map[value] = index
        return []

    @staticmethod
    def group_anagrams(strs: list[str]) -> list[list[str]]:
        anagram_hashmap = defaultdict(list)
        results: list[list[str]] = []
        for s in strs:
            ss = tuple(sorted(s))
            anagram_hashmap[ss].append(s)

        for anagram_group in anagram_hashmap.values():
            results.append(anagram_group)

        return results
