class CajeroException(Exception):

        def __init__(self, valor):
                self.valor = valor

        def __str__(self):
                return "ERROR: " + str(self.valor)
        
        
class Cajero:

        def __init__(self, billetes=[500,200,100,50,20,10]):
                self.__billetes = billetes

        def getBilletes(self):
                return self.__billetes

        def sacarDinero(self, importe):
                if importe % 10 != 0:
                        raise CajeroException("El importe debe ser multiplo de 10")

                if importe <= 0:
                        raise CajeroException("El importe debe > 0")
                
                desglose={}
                
                
                i = 0
                while importe > 0:                                       
                        if importe >= self.__billetes[i]:
                                numBilletes = importe // self.__billetes[i]
                                desglose[self.__billetes[i]] = numBilletes
                                importe -= self.__billetes[i] * numBilletes
                        i+=1                

                
                return desglose

try:                    
        cajero = Cajero()
        print (cajero.sacarDinero(50))
        
except CajeroException as e:
        print (e)


