s = "hola que tal"
histo = {}

for i in s:
        if i in histo.keys():
                histo[i]+=1
        else:
                histo[i]=1

print (histo)                
