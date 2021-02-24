def par_impar(numero):
    resto = numero % 2
    if resto == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    numero = int(input())
    resultado = par_impar(numero)
