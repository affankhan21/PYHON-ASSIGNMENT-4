

# assignment question b

""" OUTPUT
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

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print() 

for i in range(1,5):
    for j in range(4,i-1,-1):
        print("*",end="")
    print() 
print()       