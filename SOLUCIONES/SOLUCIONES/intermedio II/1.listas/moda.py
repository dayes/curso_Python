# calcular la moda de una lista de enteros

L = [3,4,5,6,7,8,8,9,8,8,2,1,9]
conteo={}

for i in L:
        if i in conteo.keys():                       
                conteo[i]+=1
        else:
                conteo[i]=1

print (conteo)
valor = max(conteo.values())


elementos = list(conteo.items())
print("Elementos: \n",elementos, "\ntype:", type(elementos))

#Con el parametro key definimos una funcion que nos indica, cual es la clave:
elementos.sort(key=lambda x:x[1],reverse=True)

print(elementos)
print ("La moda es el: ",elementos[0][0], " con ",elementos[0][1]," repeticiones ...")


