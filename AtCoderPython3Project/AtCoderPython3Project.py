import copy
 
a = input()
ret = ""
for i in range((6 // len(a))):
  ret += a
  
print(ret)