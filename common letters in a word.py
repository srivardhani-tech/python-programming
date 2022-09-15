s1=string(input("Enter first string:"))
s2=string(input("Enter second string:"))
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)

            
            #>>>>output:
        Enter first string:hi am apitha
Enter second string:hi am riya
The common letters are:
 
a
h
i
m

            
            
