class Solution(object):
    def twoSum(self, a, target):
       for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                return [i,j]