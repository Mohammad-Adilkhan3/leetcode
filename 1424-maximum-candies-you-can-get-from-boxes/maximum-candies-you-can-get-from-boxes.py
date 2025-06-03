class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        queue = deque()
        have_box = set(initialBoxes)
        have_key = set()
        visited = set()
        res = 0

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)

        while queue:
            box = queue.popleft()
            if box in visited:
                continue
            visited.add(box)
            res += candies[box]

            # Add new keys
            for key in keys[box]:
                if key not in have_key:
                    have_key.add(key)
                    if key in have_box and key not in visited:
                        queue.append(key)

            # Add contained boxes
            for contained in containedBoxes[box]:
                if contained not in have_box:
                    have_box.add(contained)
                if status[contained] == 1 or contained in have_key:
                    if contained not in visited:
                        queue.append(contained)

        return res