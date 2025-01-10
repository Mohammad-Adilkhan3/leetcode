from collections import Counter

def wordSubsets(words1, words2):
    # Step 1: Combine the requirements from words2
    target = Counter()
    for word in words2:
        target |= Counter(word)  # Combine maximum requirements using "|=" (union with max)
    
    # Step 2: Check universal property for words1
    return [word for word in words1 if not target - Counter(word)]

# Example Usage
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
print(wordSubsets(words1, words2))  # Output: ["facebook", "google", "leetcode"]

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]
print(wordSubsets(words1, words2))  # Output: ["apple", "google", "leetcode"]
