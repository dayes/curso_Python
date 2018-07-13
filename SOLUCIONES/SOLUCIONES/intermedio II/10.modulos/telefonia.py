import Cliente,Factura,SMS,Call,CallInternational


if __name__=="__main__":
        # principal:
        cli = Cliente.Cliente("Juan Perez", 600998833, "56.777.888G")
        fact = Factura.Factura("30/09/2016","16/0001",cli)
        fact.addDetalle(SMS.SMS("1/09/2016","14:15",808585585,0.05))
        fact.addDetalle(SMS.SMS("10/09/2016","08:09",608585445,0.05))
        fact.addDetalle(SMS.SMS("12/09/2016","12:58",608564585,0.05))
        fact.addDetalle(SMS.SMS("19/09/2016","14:15",208585585,0.05))

        fact.addDetalle(Call.Call("9/09/2016","14:15",208585585,0.025, 0.023))
        fact.addDetalle(Call.Call("19/09/2016","4:15",208585585,0.025, 0.08))
        fact.addDetalle(Call.Call("29/09/2016","16:15",208555585,0.025, 0.12))

        fact.addDetalle(CallInternational.CallInternational("2/09/2016","09:15",208555585,0.025, 0.12, 1))

        fact.generar()


                        



        
