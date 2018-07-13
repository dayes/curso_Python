L=[1,2,4,5,6,7,7,7,-8]

orden = True
for i in range(0,len(L)-1):
        if L[i] > L[i+1]:
                orden = False;

if orden:
        print ("Esta ordenado")
else:
        print ("NO ordenado")
        
