"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = set()
        for i in intervals:
            for t in range(i.start, i.end):
                if t in times:
                    return False
                times.add(t)
        return True


