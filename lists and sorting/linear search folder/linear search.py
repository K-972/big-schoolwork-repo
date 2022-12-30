def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','a','i','l']
x = 'a'
print("element found at index "+str(linearsearch(arr,x)))
