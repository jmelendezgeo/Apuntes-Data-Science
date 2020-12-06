from borracho import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada


from bokeh.plotting import figure, show



def caminata(campo,borracho,pasos):
    inicio= campo.obtener_coordenada(borracho)
    
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))



def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
#Esta funcion es independiente del tipo de borracho. Esta vez estamos trabajando con BorrachoTradicional
    borracho= tipo_de_borracho(nombre='David') #Con esto inicializamos el tipo de borracho de BorrachoTradicional pasandole el nombre
  
    origen= Coordenada(0,0)
    distancia = []
    
    
    for _ in range(numero_de_intentos):
        # El _ se utiliza para indicar que no usaremos la variable. Nos importa
        # es el numero de intentos que usaremos el loop
        
        
        campo = Campo() # Inicializamos el campo
        campo.anadir_borracho(borracho,origen) #Pasamos los parametros al metodo de campo
        simulacion_caminata = caminata(campo,borracho,pasos)
        distancia.append(round(simulacion_caminata,1))
        
    return distancia
                                        

def graficar(x,y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x,y, legend='distancia media')

    show(grafica)


    
    

def main(distancia_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata =[]    


    for pasos in distancia_de_caminata: 
        distancias= simular_caminata(pasos,numero_de_intentos, tipo_de_borracho) #Al simular la caminata obtendremos las distancias que se recorrieron
        distancia_media = round(sum(distancias)/ len(distancias),4)
        distancia_maxima = max(distancias)
        distancia_minima= min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        
        
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media= {distancia_media}')
        print(f'Max= {distancia_maxima}')
        print(f'Min= {distancia_minima}')

    graficar(distancia_de_caminata, distancias_media_por_caminata)




if __name__ == '__main__':
    
    distancia_de_caminata=[10,100,1000,10000] #Haremos simulaciones de distintas cantidades de pasos
    numero_de_intentos= 100 #Las simulaciones usualmente las corremos mas de una vez y tomamos promedios
    
    
    
    #Llamamos a la funcion main enviandole distancia a recorrer, intentos y el borracho que queremos
    main(distancia_de_caminata,numero_de_intentos,BorrachoTradicional) 
