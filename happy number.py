def ispalindrome(s):
    rev=''.join(reversed(s))
    if(s==rev):
        return True
    return False
s=input("enter the word")
ans=ispalindrome(s)
if(ans):
    print("no")
else:
    print("yes")
    
    
#>>output:

enter the word19
yes


    
    
