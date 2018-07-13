d1 = {'a':1,'b':2,'c':3}
d2 = {'b':22,'c':33,'d':44,'e':5}
d1.update(d2)
print(d1)


"""
Referencias o copias
"""
L1=[0,10,12,13]
#L2 = L1
L2 = L1.copy()
L2[0] = 1000
print ("L1: ",L1)
print ("L2: ",L2)