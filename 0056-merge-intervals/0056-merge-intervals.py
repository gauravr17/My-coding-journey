class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            
            if start <= last_end:
                # overlapping, merge by extending the end
                result[-1][1] = max(last_end, end)
            else:
                # no overlap, start a new interval
                result.append([start, end])
        
        return result