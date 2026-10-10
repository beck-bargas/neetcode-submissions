class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1] = [min(res[-1][0], intervals[i][0]), min(res[-1][1], intervals[i][1])]
        return len(intervals) - len(res)

        