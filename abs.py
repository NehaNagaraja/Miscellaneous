"""import math
def abs(arr,key,cnt):
    cnt1 = 0
    mn = 0
    j=1
    res = {}
    r = math.ceil(cnt/2)
    print (r)
    for i in range(r):
        m = math.fabs(arr[key]-arr[key+j])
        n = math.fabs(arr[key] - arr[key -j])
        res[m]=arr[key+j]
        res[n] = arr[key - j]
        j += 1
    print (res)


arr = [1,3,5,6,8]
abs(arr,2,3)"""


print ord('5')