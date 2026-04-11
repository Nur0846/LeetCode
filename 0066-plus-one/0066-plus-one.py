class Solution:
        def plusOne(self,num):
           carry=1
           for i in range(len(num)-1,-1,-1):
               new_value=num[i]+carry

               if new_value==10:
                 num[i]=0
                 carry=1
               else:
                  num[i]=new_value
                  carry=0
                  break
           if carry:
            num.insert(0,1)
           return num
        

        