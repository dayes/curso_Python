class Cajero:

        def __init__(self, billetes=[500,200,100,50,20,10]):
                self.__billetes = billetes

        def getBilletes(self):
                return self.__billetes

        def sacarDinero(self, importe):
                desglose={}
                if importe % 10 == 0 and importe > 0:
                        i = 0
                        while importe > 0:                                       
                                if importe >= self.__billetes[i]:
                                        numBilletes = importe // self.__billetes[i]
                                        desglose[self.__billetes[i]] = numBilletes
                                        importe -= self.__billetes[i] * numBilletes
                                i+=1                

                
                return desglose

                        
cajero = Cajero()
print (cajero.sacarDinero(230))


