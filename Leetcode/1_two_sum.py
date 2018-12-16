class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        arr = []
        for index, each in enumerate(nums):
            diff = target - each
            if each in map.keys():
                arr.append(map[each])
                arr.append(index)
            else:
                map[diff] = index
        print (map)
        return arr