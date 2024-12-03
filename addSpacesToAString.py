class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        n = len(s)

        for i in range(n):
            # If the current index matches a space index, insert a space
            if space_index < len(spaces) and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])

        return ''.join(result)
