def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise NameError
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Se debe ingresar un numero")
    except NameError:
        print('No se pueden ingresar numeros negativos')

if __name__ == '__main__':
    run()