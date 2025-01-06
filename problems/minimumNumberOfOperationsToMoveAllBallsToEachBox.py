class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        # Prefix pass
        count = 0  # Number of balls encountered so far
        operations = 0  # Cumulative operations
        for i in range(n):
            answer[i] += operations
            count += int(boxes[i])  # Update the ball count
            operations += count  # Add current balls to operations
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            count += int(boxes[i])  # Update the ball count
            operations += count  # Add current balls to operations
        return answer
