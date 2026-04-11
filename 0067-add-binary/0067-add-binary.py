class Solution:
    
    def addBinary(self, A: str,B: str) -> str:
        i,j,carry,sum=len(A)-1,len(B)-1,0,0
        result = []
        while i>=0 or j>=0 or carry:
           sum = carry
           if i>=0 :
              sum+=int(A[i])
              i-=1
           if j>=0 :
               sum+=int(B[j])
               j-=1
           carry= sum//2
           sum=sum%2
           result.append(str(sum))
        return ''.join(reversed(result))
    
        