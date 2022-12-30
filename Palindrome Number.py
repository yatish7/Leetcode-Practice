class Solution(object):
    def isPalindrome(self, x):
        if x==0:
            return True
        else:
            w=x
            c=0
            while x>0:
                r=x%10
                c=c*10+r
                x=x//10
            if c==w:
                return True
            else:
                return False
                