class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(l,r):
            if l>=r:
                return 0
            mid = (l+r)//2
            count = merge(l,mid)+merge(mid+1,r)
            j = mid+1
            for i in range(l,mid+1):
                while j <=r and nums[i]>2*nums[j]:
                    j = j+1
                count = count+j-(mid+1)
            temp=[]
            i=l
            j = mid+1
            while i<=mid and j<=r:
                if nums[i]<nums[j]:
                    temp.append(nums[i])
                    i=i+1
                else:
                    temp.append(nums[j])
                    j = j+1
            while i<= mid:
                temp.append(nums[i])
                i=i+1
            while j<=r:
                    temp.append(nums[j])
                    j = j+1
            nums[l:r+1]=temp
            return count
        return merge(0,len(nums)-1)

                
        