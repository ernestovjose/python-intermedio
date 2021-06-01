def run ():
    #resolveremos lo mismo con list comprehensions
    comprehension = [i for i in range(1, 99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(comprehension)


if __name__ == '__main__':
    run() #inicia la funcion run al correr el .py