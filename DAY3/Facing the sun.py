#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        sum=0
        mh=0
        n=len(height)
        for i in range(n):
            if height[i]>mh:
                sum+=1
                mh=height[i]
                
        return sum
