import numpy as np
from matplotlib import pyplot as pt

m =[]

a= int(input("Enter the first term : "))
r = int(input("Enter the common ratio : "))
n = int(input("Enter the number of terms : "))
y = np.linspace(1,n,n,dtype=int)

print("GP series is :")

i =1 

while(i<=n):
    cr = a*(r**(i-1))
    m.append(cr)
    i = i+1
    print(cr)

print(m)

pt.plot(y,m,'ro')
pt.xlabel('position of terms')
pt.ylabel('values of terms')
pt.title("Grpah of the GP Series")
pt.show()