def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    num = input('Ingresa un número: ')
    # assert num.isnumeric(), 'No se ingreso un numero'
    assert int(num) > 0, 'No se puede ingresar un numero negativo'
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()