def iso(a,b):
    if(len(a)!=len(b)):
        return False
    x=[a.count(char1) for char1 in a]
    y=[b.count(char1) for char1 in b]
    return x==y
string1=input("input string1..")
string2=input("input string2..")
print(iso(string1,string2))

>>>output:
  input string1..egg
input string2..add
True
