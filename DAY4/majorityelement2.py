class Solution:
    def findMajority(self, arr):
        
        # code here
        res=[]
        b={}
        arr.sort()
        for x in arr:
            if x not in b:
                b[x]=1
            else:
                b[x]+=1
        
        for x in b:
            if b[x]>len(arr)//3:
                res.append(x)
        return res
