class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()

        lo = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < lo[stack[-1]]:
                rem = stack.pop()
                seen.remove(rem)

            stack.append(char)
            seen.add(char)

        return "".join(stack)
