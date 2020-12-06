class Persona:
    
    def __init__(self,nombre):
        self.nombre= nombre
        
    def avanza(self):
        print('Ando caminando')
        
class Ciclista(Persona):
    
    def __init__(self,nombre):
        super().__init__(nombre) #Esta es nuestra referencia a Persona (a la superclase que especificamos)
   
    ##Inicio del polimorfismo 
    def avanza(self):
        print('Ando avanzando en mi bici')
        
        
def main():
    persona= Persona('David')
    persona.avanza()
    
    ciclista= Ciclista('Jesus')
    ciclista.avanza()
if __name__ == '__main__':
    main()