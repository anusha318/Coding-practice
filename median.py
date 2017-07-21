#function to find median of a given list a
def localMedian(a):
  n=len(a)
  if(n%2==0):
    return [a[int(n/2)-1],a[int(n/2)]]
  else:
    return [a[int(n/2)]]
#function to find median of 2 lists given  
def getMedian(a1,a2,n):
  if(n<=0):
    return []
  if(n==1):
    return [a1[0],a2[0]]
  if(n==2):
    return [max(a1[0],a2[0]),min(a1[1],a2[1])]
  m1=localMedian(a1)
  m2=localMedian(a2)
  #Median of both lists are equal
  if(sum(m1)/len(m1) == sum(m2)/len(m1)):
    if(n%2==0):
      return [max(m1[0],m2[0]),max(m1[1],m2[1])]
    return [m1[0],m2[0]]
  #Median of list a1 is less than median of list a2 - if a1=[..,m1,m2,...n] and a2=[1....m1,m2,...] then take find median of a1=[m1..n] and a2=[1..m2]
  elif(sum(m1)/len(m1) < sum(m2)/len(m2)):
    if(n%2==0):
      return getMedian(a1[int(n/2)-1:],a2[0:int(n/2)+1],int(n/2)+1)
    else:
      return getMedian(a1[int(n/2):],a2[0:int(n/2)+1],int(n/2)+1)
  #Median of list a2 is less than median of list a1
  else:
    if(n%2==0):
      return getMedian(a1[0:int(n/2)+1],a2[int(n/2)-1:],int(n/2)+1)
    else:
      return getMedian(a1[0:int(n/2)+1],a2[int(n/2):],int(n/2)+1)
  
#helper function - returns median of two given lists 
def getMedian_helper(array_int1, array_int2):
  median = []
  if(len(array_int1)==len(array_int2)):
    median=getMedian(array_int1,array_int2,len(array_int1))
    median.sort()
  return median

#assert to check if the median returned is correct
assert(getMedian_helper([],[]) == [])
assert(getMedian_helper([],[1]) == [])
assert(getMedian_helper([1],[]) == [])
assert(getMedian_helper([1],[1]) == [1,1])
assert(getMedian_helper([1,2],[3,4]) == [2,3])
assert(getMedian_helper([1,1,1],[1,1,1]) == [1,1])
assert(getMedian_helper([1,2,3],[1,2]) == [])
assert(getMedian_helper([1,2,3],[4,5,6]) == [3,4])
assert(getMedian_helper([1,3,5],[2,4,6]) == [3,4])
assert(getMedian_helper([1,2,3],[3,4,5]) == [3,3])
assert(getMedian_helper([1,2,4,10,20,34],[30,32,34,40,45,50]) == [30,32])
assert(getMedian_helper([30,32,34,40,45,50],[1,2,4,10,20,34]) == [30,32])
assert(getMedian_helper([1, 10, 20, 30, 40, 50], [11,12,13,14,15,16]) == [14,15])
assert(getMedian_helper([1, 10, 15, 30, 40, 50], [11,12,13,14,16,17]) == [14,15])
