class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        l,r = 0,len(height)-1
        leftmax,right_max = height[l],height[r] 
        rest = 0
        while l<r:
            if leftmax<right_max:
                l = l+1
                leftmax = max(leftmax,height[l])
                rest = rest+leftmax-height[l]
            else:
                r=r-1
                right_max= max(right_max,height[r])
                rest = rest+right_max - height[r]
        return rest