"""
*
**
***
****
*****
****
***
**
*
"""
#Approach 1
star = "*"

for i in range(10):
    if i >=5:
        star = star[:-2]

    print(star) 
    star += "*"   

#Approach 2
    
star = "*"
for i in range(10):
    print(star)
    if i <4:
        star += "*"
    else:
        star = star[:-1]