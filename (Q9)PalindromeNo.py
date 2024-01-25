class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        n=x
        counter=-1
        while(n!=0):
            n//=10
            counter+=1
        n=x
        sum=0
        while(n!=0):
            a=n%10
            a=a*(10**counter)
            counter-=1
            sum+=a
            n//=10
        if(sum==x):
            return True
        return False
        
            
