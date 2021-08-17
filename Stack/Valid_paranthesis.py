class Solution(object):
    def check(self,a,b):
        print(a,b)
        if(a=='{'and b=='}'):
            return True
        elif(a=='('and b==')'):
            return True
        elif(a=='['and b==']'):
            return True
        else:
            return False
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in range(len(s)):
            if(s[i]=='{'or s[i]=='['or s[i]=='('):
                stack.append(s[i])
            else:
                if(len(stack)>0):
                    # print(stack[-1],s[i])
                    if self.check(stack[-1],s[i]) == False:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
        
        