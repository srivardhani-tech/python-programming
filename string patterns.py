import re
s = input("enter the first string")
p = input("enter the second string")
p = r"{}".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")
>>>> output:-
enter the first string :- "aa" 
enter the second string :- "a"
false
.......
enter the first stringaa
enter the second stringa*
true
