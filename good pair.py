def solve(nums):
   count=0
   n=len(nums)
   for i in range(n):
      for j in range(i+1,n):
         if nums[i] == nums[j]:
            count+=1
   return count
nums=[]
m=int(input("Number of elements in array:"))
for i in range(0,m):
   l=int(input())
   nums.append(l)
print(nums)
print(solve(nums))


#>>output:
Number of elements in array:6
1
2
3
1
1
3
[1, 2, 3, 1, 1, 3]
4
