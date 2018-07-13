billetes = [500,200,100,50,20,10]
desglose = {}

importe = 0
while importe == 0 or importe % 10 != 0:
        print ("Teclear importe:")
        importe = int(input())

i = 0
while importe > 0:
        if importe >= billetes[i]:
                numBilletes = importe // billetes[i]
                desglose[billetes[i]]=numBilletes
                importe -= billetes[i] * numBilletes
        i+=1                


LL2 = list(desglose.items())
LL2.sort(reverse=True)
for a,b in LL2:
        print (b, " billetes de ", a)
