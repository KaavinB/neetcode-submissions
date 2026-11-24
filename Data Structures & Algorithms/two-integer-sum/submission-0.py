class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i in range(len(nums)):
            if nums[i] not in seen_map:
                seen_map[target - nums[i]] = i
            else:
                return [seen_map[nums[i]], i]