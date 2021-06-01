def run ():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname": "Ernesto", "lastname": "Vera"}

    super_list_of_people = [
        {"firstname": "Ernesto", "lastname": "Vera"},
        {"firstname": "Pola", "lastname": "Vera"},
        {"firstname": "Martin", "lastname": "Vera"},
        {"firstname": "Filomena", "lastname": "Vera"},
        {"firstname": "Ernesto", "lastname": "Vera"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6],
        "integer_nums": [-1,-2,0,1,2],
        "Floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key,"-", value)

    for i in super_list_of_people:
	    print(i.items())

    for item in super_list_of_people:
        print(item["firstname"] , "-" , item["lastname"])

if __name__ == '__main__':
    run() #inicia la funcion run al correr el .py