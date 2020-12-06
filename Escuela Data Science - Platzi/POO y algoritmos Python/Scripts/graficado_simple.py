from bokeh.plotting import figure,output_file,show


if __name__ == '__main__':
    output_file('graficado_simple.html') #especificamos el archivo de salida
    fig = figure() #Creamos un objeto figura
    
    total_vals=int(input('Cuantos valores quieres graficar?: '))
    x_vals=list(range(total_vals))
    y_vals=[]
    
    for x in x_vals:
        val = int(input(f'Valor y para {x}: '))
        y_vals.append(val)
                        
                        
    fig.line(x_vals,y_vals,line_width=2) #Creamos un grafixo y vs x con ancho de linea 2
    show(fig) #Mostrar la grafica                
    


