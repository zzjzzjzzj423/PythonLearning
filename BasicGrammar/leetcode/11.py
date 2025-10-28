class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        sorted_citation = sorted(citations, reverse=True)
        h = 0;
        i = 0;
        n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h
