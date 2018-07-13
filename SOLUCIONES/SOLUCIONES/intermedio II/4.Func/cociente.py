def cociente(n1, n2):
        if n1 >= n2:
                return 1 + cociente(n1-n2, n2)
        else:
                return 0



print (cociente(8,2))
print (cociente(3,3))
print (cociente(7,2))
