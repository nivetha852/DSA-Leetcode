from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks)
        freq = max(counts.values())
        count = sum(1 for c in counts.values() if c == freq)
        frame = (freq - 1) * (n + 1) + count
        return max(frame, len(tasks))

        