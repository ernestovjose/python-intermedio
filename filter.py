def run ():

    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

    par = list(filter(lambda x: x%2 == 0, lista))

    print(par)


if __name__ == '__main__':
    run() #inicia la funcion run al correr el .py