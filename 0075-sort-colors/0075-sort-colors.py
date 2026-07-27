class Solution:
    def sortColors(self, nums: List[int]) -> None:
     """
     Do not return anything, modify nums in-place instead.
     """
     L=0
     C=0
     R=len(nums)-1

     while(C<=R):
        if(nums[C]==0):
            nums[C],nums[L]=nums[L],nums[C]
            L+=1
            C+=1
        elif(nums[C]==1):
            C+=1
        else:
            nums[C],nums[R]=nums[R],nums[C]
            R-=1
        