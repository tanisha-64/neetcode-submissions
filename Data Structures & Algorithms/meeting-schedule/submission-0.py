"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Step 1: Sort the intervals based on their start times
        intervals.sort(key=lambda x: x.start)
        
        # Step 2: Check adjacent intervals for an overlap
        for i in range(1, len(intervals)):
            # If the current meeting starts before the previous one ends, there's a conflict
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True