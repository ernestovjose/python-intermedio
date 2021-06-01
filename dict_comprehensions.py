def run ():
    # dict = {}
    # for i in range(1, 101):
    #     dict[i] = i**3
    # print(dict)


    cubic_comprehension = {i : i**3 for i in range(1, 101) if i % 3 != 0}
    print(cubic_comprehension)


if __name__ == '__main__':
    run() #inicia la funcion run al correr el .py