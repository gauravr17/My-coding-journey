class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        num_distinct_types = len(set(candyType))
        max_she_can_eat = n // 2

        return min(num_distinct_types, max_she_can_eat)