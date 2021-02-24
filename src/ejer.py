
def showNumbers:
    number = input("Introduce numero: ")
    for i in range(0, number+1)
        print(i + "\n")
    

def par_impar(numero):
    resto = numero % 2
    if resto == 1:
        return 1
    else:
        return 0
