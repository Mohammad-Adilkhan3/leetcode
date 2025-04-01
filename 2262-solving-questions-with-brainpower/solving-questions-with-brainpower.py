class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # Extra space for boundary condition

        for i in range(n - 1, -1, -1):  # Traverse from right to left
            points, brainpower = questions[i]
            next_q = i + brainpower + 1
            
            # Solve or skip the question
            dp[i] = max(points + (dp[next_q] if next_q < n else 0), dp[i + 1])

        return dp[0]