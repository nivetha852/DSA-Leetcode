class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack =[]
        maxarea=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                h = heights[stack.pop()]
                if stack:
                    width = i-stack[-1]-1
                else:
                    width =i
                area = h*width
                if area>maxarea:
                    maxarea=area
            stack.append(i)
        return maxarea

        