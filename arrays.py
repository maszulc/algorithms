class Arrays:
    @staticmethod
    def contains_duplicate1(nums: list[int]) -> bool:
        """
        Given an integer array nums:
         - return true if any value appears at least twice in the array,
         - return false if every element is distinct.
        :param nums:
        :return boolean:
        """
        x: int
        for x in nums:
            if nums.count(x) > 1:
                return True
        return False

    @staticmethod
    def contains_duplicate2(nums: list[int]) -> bool:
        """
        Checks duplicates in array by leveraging a hashset
        :param nums:
        :return:
        """
        hashset: set[int] = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
