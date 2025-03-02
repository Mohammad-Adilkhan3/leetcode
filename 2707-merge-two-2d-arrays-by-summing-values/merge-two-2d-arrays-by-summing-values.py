class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        merged_dict = defaultdict(int)
        for id1, val1 in nums1:
            merged_dict[id1] += val1
        for id2, val2 in nums2:
            merged_dict[id2] += val2
        return sorted(merged_dict.items())