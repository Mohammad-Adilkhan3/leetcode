class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        n = len(nums)
        count = 0
        for i in range(n):
            subarray_counts = Counter()
            distinct_in_subarray = 0
            for j in range(i, n):
                subarray_counts[nums[j]] += 1
                if subarray_counts[nums[j]] == 1:
                    distinct_in_subarray += 1
                if distinct_in_subarray == distinct_count:
                    count += 1
        return count

