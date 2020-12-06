class Rectangulo:
    
    def __init__(self,base,altura):
        #Inicializamos variables de instancia
        self.base = base #
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
class Cuadrado(Rectangulo): #De esta forma tenemos Cuadrado que extiende a Rectangulo (heredar comportamiento)
    
    def __init__(self,lado):
        super().__init__(lado,lado) #super() nos permite obtener referencia directa de la clase Padre
        
if __name__ == '__main__':
    rectangulo= Rectangulo(base=3, altura=4)
    print(rectangulo.area())
    
    cuadrado= Cuadrado(lado=5)
    print(cuadrado.area()) #Utilizamos area aunque no haya sido definido en cuadrado (pero lo heredó)