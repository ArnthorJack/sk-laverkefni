#import re
w_1 = str(input())
w_2 = str(input())
points = 1
for i in  range (len(w_1)):
    #print(i)
    if w_1[i] != w_2[i]:
        points += 1
    #stafur = w_1[i]
    #if i in w_2:
     #   points +=1
    #if stafur != w_2[i]:
        #points += 1

print(points)
