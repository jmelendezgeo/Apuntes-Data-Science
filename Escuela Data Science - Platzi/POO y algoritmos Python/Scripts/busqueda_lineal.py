"""busqueda_lineal.py"""

import random

def busqueda_lineal(lista,objetivo):
    match=False 
    
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño es la lista?'))
    objetivo=int(input('Que numero quieres encontrar?'))
    
    lista = [random.randint(0,100) for i in range(tamano_de_lista)] #Llenar una lista de numeros aleatorios entre 0-100
    
    encontrado= busqueda_lineal(lista,objetivo)
    
    print(lista)    
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #Operadores ternarios. Podemos generar if Else en linea de codigo
