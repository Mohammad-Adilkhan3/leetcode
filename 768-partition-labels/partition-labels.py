class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}  # Store last index of each character
        result = []
        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])  # Expand end to the farthest occurrence
            if i == end:  # Partition complete
                result.append(end - start + 1)
                start = i + 1  # Move start to next partition

        return result
