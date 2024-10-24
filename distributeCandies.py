 def distributeCandies(self, candyType: List[int]) -> int:
        return int(len(candyType)/2) if len(set(candyType)) > int(len(candyType)/2) else len(set(candyType))
