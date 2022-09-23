#MEAN MEDIAN MODE
import math

x=[2,3,4,5,6,7,89,90]
print("SUM=>",sum(x))
print("MEAN=>",sum(x)/len(x))
x.sort()
if len(x) %2==0:
     idx = len(x)//2
     value=x[idx]+x[idx+1]
     print("median=>",value/2)
else:
    value=x[len(x)//2]
    print("median=>",value/2)
