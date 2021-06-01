def run ():
    squares = []
    for i in range(1, 101):
        squares.append(i**2)
    print(squares)

    squares_divisble_3 = []
    for i in range(1, 100):
        if i % 3 != 0:
            squares_divisble_3.append(i**2)
    print(squares_divisble_3)

    #resolveremos lo mismo con list comprehensions
    squares_comprehension = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares_comprehension)


if __name__ == '__main__':
    run() #inicia la funcion run al correr el .py