class Solution:
  def maxScoreSightseeingPair(values):
      max_score = 0
      max_i = values[0]  # Initial value of `values[i] + i`
      
      for j in range(1, len(values)):
          # Calculate the score for the pair (i, j)
          max_score = max(max_score, max_i + values[j] - j)
          # Update max_i for the next iteration
          max_i = max(max_i, values[j] + j)
      
      return max_score
