class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max1=0
        max2=0
        for i in range(len(arr)):
            if arr[i]>max1:
                max1=arr[i]
        for i in range(len(arr)):
            if arr[i]>max2 and arr[i]!=max1:
                max2=arr[i]
        if max2==0:
            return -1
        else:
            return max2
            
